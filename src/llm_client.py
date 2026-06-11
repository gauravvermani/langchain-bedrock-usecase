# ============================================================
# llm_client.py — Builds and returns the LangChain LLM object.
#
# Think of this as a "factory" — one place that creates the AI
# model object. Every other file just imports get_llm() and
# uses it without worrying about setup details.
#
# We use ChatBedrockConverse (modern recommended class) instead
# of the older ChatBedrock. The Converse API is AWS's unified
# interface that works the same way for ALL models.
# ============================================================

import boto3
from langchain_aws import ChatBedrockConverse
from config import AWS_REGION, MODEL_ID, MAX_TOKENS, TEMPERATURE


def get_llm(temperature: float = TEMPERATURE, max_tokens: int = MAX_TOKENS):
    """
    Create and return a LangChain ChatBedrockConverse LLM instance.

    Parameters:
        temperature  → how creative/random the AI answers are (0.0-1.0)
        max_tokens   → the max length of the AI response

    Returns:
        A ready-to-use LangChain chat model object.
    """

    # Create a raw boto3 client for the Bedrock Runtime service.
    # LangChain uses this under the hood to make the actual API calls.
    bedrock_client = boto3.client(
        "bedrock-runtime",
        region_name=AWS_REGION
    )

    # Build the LangChain LLM wrapper around the boto3 client.
    # ChatBedrockConverse uses AWS Converse API — works for all models uniformly.
    llm = ChatBedrockConverse(
        client=bedrock_client,    # The boto3 connection we built above
        model=MODEL_ID,           # Which AI brain to use
        temperature=temperature,  # Creativity level
        max_tokens=max_tokens     # Max response length
    )

    return llm
