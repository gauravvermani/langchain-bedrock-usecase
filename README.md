## Overview

A modular, production-patterned Python project that integrates **LangChain** 
with **Amazon Bedrock** to demonstrate the full spectrum of modern LLM 
application patterns — from simple invocations to stateful multi-turn 
conversations, real-time streaming, and schema-enforced structured output.

Built on **Claude Haiku 4.5** via AWS's Converse API, this project serves 
as both a reference implementation and a launchpad for enterprise-grade 
generative AI applications. Each module is independently executable and 
extensively commented for developer clarity.

## Why This Project

Most Bedrock examples stop at a basic `invoke_model()` call. This project 
goes further — demonstrating the full LangChain LCEL pipeline architecture 
that scales cleanly from prototype to production. The patterns here directly 
map to real-world use cases: chatbots, document pipelines, AI agents, and 
data extraction workflows.

## Feature Modules

| Module | Pattern | Real-World Use Case |
|--------|---------|---------------------|
| `simple_invoke.py`      | Direct LLM invocation          | Any single-turn Q&A |
| `prompt_chain.py`       | LCEL chains + prompt templates  | Dynamic content generation |
| `chat_memory.py`        | Stateful multi-turn memory      | Conversational AI assistants |
| `streaming.py`          | Token-level streaming output    | Real-time chat interfaces |
| `structured_output.py`  | Pydantic schema enforcement     | Data extraction pipelines |
| `summarizer.py`         | Multi-format summarization      | Document processing workflows |

## Tech Stack

- **LangChain 0.3+** — LCEL, prompt templates, memory, output parsers
- **langchain-aws** — `ChatBedrockConverse` (AWS Converse API)
- **Amazon Bedrock** — Claude Haiku 4.5 (`us.anthropic.claude-haiku-4-5-20251001-v1:0`)
- **Pydantic v2** — structured output schema validation
- **python-dotenv** — environment-based configuration management
