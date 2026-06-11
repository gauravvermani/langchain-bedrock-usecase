# ============================================================
# main.py — THE ENTRY POINT. Run this file to demo everything.
#
# Run with:
#   python src/main.py
#
# Or run any feature file directly, e.g.:
#   python src/simple_invoke.py
# ============================================================

from simple_invoke     import run_simple_invoke
from prompt_chain      import run_prompt_chain
from chat_memory       import run_chat_with_memory
from streaming         import run_streaming
from structured_output import run_structured_output
from summarizer        import run_summarizer


def main():
    """Run all 6 LangChain + Bedrock features in sequence."""

    print("\n" + "#"*60)
    print("#   LangChain + Amazon Bedrock — Full Feature Demo       #")
    print("#"*60)
    print("""
    Features:
      1. Simple LLM Invocation      — basic question/answer
      2. Prompt Templates + Chains  — dynamic, reusable prompts
      3. Multi-Turn Chat + Memory   — AI remembers the conversation
      4. Streaming Responses        — word-by-word output
      5. Structured / JSON Output   — typed Pydantic objects
      6. Text Summarization         — bullets + executive summary
    """)

    run_simple_invoke()       # Feature 1
    run_prompt_chain()        # Feature 2
    run_chat_with_memory()    # Feature 3
    run_streaming()           # Feature 4
    run_structured_output()   # Feature 5
    run_summarizer()          # Feature 6

    print("\n" + "#"*60)
    print("# All features completed successfully!")
    print("#"*60 + "\n")


if __name__ == "__main__":
    main()
