# ============================================================
# streaming.py — Feature 4: Streaming Responses.
#
# Normally, .invoke() waits for the FULL reply before printing.
# For long answers this means staring at a blank screen.
#
# Streaming prints each word/token AS IT ARRIVES from the AI,
# just like ChatGPT's typing effect. It feels much more alive!
#
# Under the hood, AWS Bedrock sends back small "chunks" of text
# over time. We print each chunk immediately using end="" + flush=True.
# ============================================================

from langchain_core.prompts import ChatPromptTemplate
from llm_client import get_llm


def run_streaming():
    """
    Stream a long AI response token-by-token to the terminal.
    Watch the answer appear word-by-word in real time.
    """

    print("\n" + "="*50)
    print("FEATURE 4: Streaming Response")
    print("="*50)

    llm = get_llm(max_tokens=300)  # Allow a longer answer to see the effect clearly

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a cloud architecture expert."),
        ("human",  "{question}")
    ])

    # Build the chain — no StrOutputParser since we need raw chunks for streaming
    chain = prompt | llm

    question = "List 5 AWS services every developer should know, with one sentence each."
    print(f"\nQ: {question}")
    print("\nA: ", end="", flush=True)

    # .stream() returns a generator that yields chunks as they arrive.
    # Each chunk is an AIMessageChunk with a .content string fragment.
    for chunk in chain.stream({"question": question}):
        # end=""     → don't add a newline after each chunk (keep on same line)
        # flush=True → force Python to print immediately (don't buffer)
        print(chunk.content, end="", flush=True)

    print("\n")   # Final newline to tidy up after streaming is done


if __name__ == "__main__":
    run_streaming()
