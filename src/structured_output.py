# ============================================================
# structured_output.py — Feature 5: Structured / JSON Output.
#
# By default the AI returns a free-form text paragraph.
# Sometimes you need clean, machine-readable data — like JSON —
# that you can parse and use in your application logic.
#
# We use Pydantic models to define the exact shape of the output.
# Pydantic is like a contract that says:
#   "I expect a dict with exactly these fields and types."
# LangChain + Claude will honor that contract in the response.
# ============================================================

from pydantic import BaseModel, Field
from typing import List
from langchain_core.prompts import ChatPromptTemplate
from llm_client import get_llm


# ------------------------------------------------------------------
# Define the data shape using Pydantic.
# Think of this as a form with specific required fields.
# Field() descriptions help the AI understand what to put in each slot.
# ------------------------------------------------------------------
class AWSServiceInfo(BaseModel):
    """Structured information about an AWS service."""

    name: str = Field(description="The full name of the AWS service")
    description: str = Field(description="A one-sentence plain English description")
    use_cases: List[str] = Field(description="2-3 main use cases for this service")
    pricing_model: str = Field(description="How pricing works, e.g. per-request, per-GB, per-hour")


def run_structured_output():
    """
    Ask Claude about an AWS service and get back a clean,
    structured Python object instead of a raw text paragraph.
    """

    print("\n" + "="*50)
    print("FEATURE 5: Structured JSON Output")
    print("="*50)

    llm = get_llm(temperature=0.1)   # Low temp = reliable, consistent structure

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an AWS documentation expert. Always respond with accurate information."),
        ("human",  "Give me structured information about the AWS service: {service_name}")
    ])

    # .with_structured_output() wraps the LLM so it returns a Pydantic object.
    # LangChain tells Claude to respond in JSON matching our schema.
    # The result is already parsed — no json.loads() needed!
    structured_llm = llm.with_structured_output(AWSServiceInfo)
    chain = prompt | structured_llm

    services = ["Amazon DynamoDB", "AWS Lambda"]

    for service in services:
        print(f"\n--- {service} ---")

        # .invoke() returns an AWSServiceInfo object (not a string!)
        result: AWSServiceInfo = chain.invoke({"service_name": service})

        # Access fields like normal Python object attributes
        print(f"Name:          {result.name}")
        print(f"Description:   {result.description}")
        print(f"Use Cases:")
        for use_case in result.use_cases:
            print(f"  • {use_case}")
        print(f"Pricing Model: {result.pricing_model}")


if __name__ == "__main__":
    run_structured_output()
