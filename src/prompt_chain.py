# ============================================================
# prompt_chain.py — Feature 2: Prompt Templates + LCEL Chains.
#
# Instead of hard-coding questions, we build a TEMPLATE with
# placeholders (like a Mad Lib form). We fill in the blanks
# at runtime to create dynamic, reusable prompts.
#
# LCEL = LangChain Expression Language.
# It uses the pipe operator | to connect steps together:
#   prompt | llm | output_parser
# Each step's output feeds the next — like a Unix pipe.
# ============================================================

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llm_client import get_llm


def run_prompt_chain():
    """
    Demonstrate prompt templates and LCEL chains.
    Build a reusable 'explain this topic' chain and run it
    for two different topics to show it works dynamically.
    """

    print("\n" + "="*50)
    print("FEATURE 2: Prompt Templates & LCEL Chains")
    print("="*50)

    # Build a prompt template with {placeholders}.
    # system message = sets the AI's persona/role.
    # human message  = the actual question with a {topic} slot.
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a friendly tech teacher who explains complex topics "
            "in simple, beginner-friendly language. Use analogies and "
            "avoid jargon. Keep answers under 100 words."
        ),
        (
            "human",
            "Explain {topic} like I'm a beginner."   # {topic} filled in at runtime
        )
    ])

    # StrOutputParser extracts the plain text string from the AIMessage object.
    # It's like unwrapping a gift — we only want what's inside.
    output_parser = StrOutputParser()

    # Build the chain using the pipe | operator:
    #   1. prompt  → fills in the template with our input values
    #   2. llm     → sends it to Claude and gets a response
    #   3. parser  → extracts the plain text from the response
    llm = get_llm(temperature=0.5)
    chain = prompt | llm | output_parser

    # Run the chain with two different topics.
    # .invoke() takes a dict matching the template's placeholders.
    topics = ["Amazon S3", "LangChain"]

    for topic in topics:
        print(f"\nQ: Explain {topic} like I'm a beginner.")
        result = chain.invoke({"topic": topic})
        print(f"\nA: {result}")
        print("-" * 40)


if __name__ == "__main__":
    run_prompt_chain()
