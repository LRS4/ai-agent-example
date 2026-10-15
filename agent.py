from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from services.tools_service import tools
from services.prompt_service import ResearchResponse, get_research_prompt
from services.openai_client_service import get_azure_openai_client
from dotenv import load_dotenv

load_dotenv()

azure_openai_client = get_azure_openai_client()
prompt_template = get_research_prompt()
system_message_content = prompt_template.messages[0].prompt.template

agent = create_agent(
    model=azure_openai_client, 
    tools=tools,
    system_prompt=system_message_content,
    response_format=ToolStrategy(ResearchResponse),
    debug=False
)

query = input("What can I research for you? ")

result = agent.invoke({
    "messages": [{"role": "user", "content": query}]
})

print("Topic:", result["structured_response"].topic)
print("Summary:", result["structured_response"].summary)
print("Sources:", result["structured_response"].sources)
print("Tools used:", result["structured_response"].tools_used)
