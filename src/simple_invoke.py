# ============================================================
# simple_invoke.py — Feature 1: Basic LLM invocation.
#
# The simplest thing you can do: send a plain text question
# to the AI and print the answer. No frills.
#
# This replicates what the original boto3 project did,
# but now using LangChain's cleaner interface.
# ============================================================

from llm_client import get_llm


def run_simple_invoke():
    """
    Send a single question to Claude and print the response.
    This is the "Hello World" of LangChain + Bedrock.
    """

    print("\n" + "="*50)
    print("FEATURE 1: Simple LLM Invocation")
    print("="*50)

    # Get our LangChain LLM object (already connected to Bedrock)
    llm = get_llm()

    # .invoke() sends a message to the AI and waits for the full reply.
    # We pass a plain string — LangChain converts it to the right format.
    response = llm.invoke("Explain AWS Bedrock in simple terms")

    # response is a LangChain AIMessage object.
    # .content holds the actual text string we care about.
    print("\nQ: Explain AWS Bedrock in simple terms")
    print(f"\nA: {response.content}")


if __name__ == "__main__":
    run_simple_invoke()
