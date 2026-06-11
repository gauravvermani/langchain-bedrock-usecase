# ============================================================
# chat_memory.py — Feature 3: Multi-turn Conversation with Memory.
#
# A normal LLM call is "stateless" — it forgets everything
# after each response, like someone with amnesia.
#
# Memory lets the AI REMEMBER the conversation history so
# follow-up questions make sense. This is how real chatbots work.
#
# We use in-memory storage (a Python list) — no database needed.
# For production you'd replace this with Redis or DynamoDB.
# ============================================================

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from llm_client import get_llm


def run_chat_with_memory():
    """
    Simulate a multi-turn conversation where the AI remembers
    what was said earlier. Watch how it refers back to prior context.
    """

    print("\n" + "="*50)
    print("FEATURE 3: Multi-Turn Chat with Memory")
    print("="*50)

    # chat_history is our "memory bank" — a simple Python list.
    # We manually append each message after every turn.
    # HumanMessage = what we said | AIMessage = what the AI replied
    chat_history = []

    # MessagesPlaceholder("chat_history") injects the entire
    # conversation history at that position in the prompt.
    # Think of it as pasting the full chat log into the prompt.
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a helpful AWS cloud assistant. Be concise — "
            "keep each answer under 60 words."
        ),
        # Inject all previous messages right here
        MessagesPlaceholder(variable_name="chat_history"),
        # The latest question from the user
        ("human", "{question}")
    ])

    llm = get_llm(temperature=0.3)
    chain = prompt | llm | StrOutputParser()

    # Simulate a 3-turn conversation.
    # Each turn: send current history + new question, then save both to history.
    conversation = [
        "What is Amazon EC2?",
        "How is it different from Lambda?",      # Refers to EC2 — needs memory!
        "Which one should I use for a REST API?" # Refers to both — needs memory!
    ]

    for question in conversation:
        print(f"\nYou: {question}")

        answer = chain.invoke({
            "chat_history": chat_history,   # All prior messages
            "question": question            # The new question
        })

        print(f"AI:  {answer}")

        # Save this turn to memory so the next question has context
        chat_history.append(HumanMessage(content=question))
        chat_history.append(AIMessage(content=answer))

    print(f"\n[Memory contains {len(chat_history)} messages total]")


if __name__ == "__main__":
    run_chat_with_memory()
