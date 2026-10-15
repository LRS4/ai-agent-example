from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

class ResearchResponse(BaseModel):
    topic: str = Field(description="The main subject of the research")
    summary: str = Field(description="A comprehensive summary of the findings")
    sources: list[str] = Field(description="List of URLs or citations used")
    tools_used: list[str] = Field(description="Names of the tools used in the process")

def get_research_prompt() -> ChatPromptTemplate:
    """Creates a chat prompt template for research tasks."""
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert research assistant. Your goal is to provide "
                "accurate, tool-backed information. "
                "ONLY use the 'save_to_txt' tool if the user explicitly asks to save, "
                "export, or download the results. Otherwise, just provide the "
                "final response in the required structured format."
            ),
            ("placeholder", "{chat_history}"),
            ("human", "{query}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )