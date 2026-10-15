import os
import pandas as pd
from pathlib import Path
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun, OpenWeatherMapQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from datetime import datetime

search_tool = DuckDuckGoSearchRun()

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1000)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

@tool
def save_to_txt(data: str, filename: str = "research_output.txt"):
    """
    Saves research data to the 'outputs/' folder.
    Wipes the 'outputs/' folder before saving to ensure only 
    the latest research result exists.
    """
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True) # Creates the folder if it doesn't exist

    for txt_file in output_dir.glob("*.txt"):
        try:
            txt_file.unlink()
        except Exception as e:
            print(f"Warning: Could not delete {txt_file.name}: {e}")

    save_path = output_dir / filename

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(save_path, "w", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Old outputs cleared. New data saved to {save_path}"

@tool
def check_opening_times(query: str):
    """
    Search opening_times.csv for site hours. 
    Query can be the site name (e.g., 'A', 'B', 'Site B').
    """
    file_path = "data/opening_times.csv"
    try:
        df = pd.read_csv(file_path, skipinitialspace=True)
        
        df = df.map(lambda x: str(x).strip() if pd.notnull(x) else x)
        search_term = query.strip().lower()
        
        mask = df['Sites'].str.lower().str.contains(search_term, na=False) | \
               df['Sites'].apply(lambda x: search_term in f"site {x}".lower())
        
        results = df[mask]

        if results.empty:
            available = ", ".join(df['Sites'].dropna().unique())
            return f"No info found for '{query}'. Available sites are: {available}"
        
        return results.to_string(index=False)
        
    except Exception as e:
        return f"Error: {str(e)}"

tools = [search_tool, wiki_tool, save_to_txt, check_opening_times]