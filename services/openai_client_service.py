import os
from langchain_openai import AzureChatOpenAI
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()

# @lru_cache ensures this function is only run once.
# The same client instance will be returned on subsequent calls.
@lru_cache
def get_azure_openai_client() -> AzureChatOpenAI:
    """
    Creates and returns a single, reusable AzureChatOpenAI client.
    """
    print("Creating a new AzureChatOpenAI client...")

    base_url = os.getenv("APIM_BASE_URL")
    apim_subscription_key = os.getenv("APIM_SUBSCRIPTION_KEY")
    openai_completion_model = os.getenv("OPENAI_MODEL")
    openai_api_version = os.getenv("OPENAI_API_VERSION")

    return AzureChatOpenAI(
        azure_endpoint=base_url,
        openai_api_key=apim_subscription_key,
        azure_deployment=openai_completion_model,
        openai_api_version=openai_api_version,
        model=openai_completion_model,
    )