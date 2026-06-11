# ============================================================
# summarizer.py — Feature 6: Text Summarization Chain.
#
# A very common real-world use case: feed in a long block of
# text and ask the AI to produce a shorter summary.
#
# We demonstrate two modes:
#   - Bullet-point summary (great for quick scanning)
#   - Executive summary (one dense paragraph)
# ============================================================

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llm_client import get_llm

# Sample text to summarize. In real use, load from a file, DB, or API.
SAMPLE_TEXT = """
Amazon Bedrock is a fully managed service from AWS that provides access to
high-performing foundation models (FMs) from leading AI companies including
Anthropic, AI21 Labs, Cohere, Meta, Mistral AI, Stability AI, and Amazon itself.
It allows developers to build and scale generative AI applications using
these models through a unified API without managing any infrastructure.

Key features include model fine-tuning with your own data, Retrieval Augmented
Generation (RAG) for grounding responses in your documents, AI agents that can
take multi-step actions, and guardrails for responsible AI use.
Bedrock is serverless — you pay only for what you use, and AWS handles all
the compute, scaling, and security behind the scenes.

Since its general availability in late 2023, Bedrock has become one of the
fastest-growing AWS services, used by enterprises to build customer service bots,
code assistants, data analysis pipelines, and content generation tools.
"""


def run_summarizer():
    """
    Summarize a block of text in two styles:
    1. Bullet points  — fast to scan
    2. Executive paragraph — dense, formal
    """

    print("\n" + "="*50)
    print("FEATURE 6: Text Summarization")
    print("="*50)

    llm = get_llm(temperature=0.3, max_tokens=300)
    parser = StrOutputParser()

    # {format_instructions} lets us swap output style without changing the chain
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a professional technical writer. "
            "Summarize the provided text according to the format requested."
        ),
        (
            "human",
            "Text to summarize:\n\n{text}\n\nFormat: {format_instructions}"
        )
    ])

    chain = prompt | llm | parser

    # --- Bullet points ---
    print("\n[ Bullet-Point Summary ]")
    bullets = chain.invoke({
        "text": SAMPLE_TEXT,
        "format_instructions": "3-4 concise bullet points. Start each with •"
    })
    print(bullets)

    # --- Executive summary ---
    print("\n[ Executive Summary ]")
    exec_summary = chain.invoke({
        "text": SAMPLE_TEXT,
        "format_instructions": "One dense executive summary paragraph, max 50 words."
    })
    print(exec_summary)


if __name__ == "__main__":
    run_summarizer()
