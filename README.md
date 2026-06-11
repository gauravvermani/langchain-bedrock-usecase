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

# LangChain + Amazon Bedrock — Full Feature Project

A beginner-friendly Python project demonstrating 6 key LangChain patterns
using Claude on Amazon Bedrock. Every line of code is heavily commented.

## Project Structure

```
langchain-bedrock-project/
├── src/
│   ├── main.py               ← RUN THIS — demos all features
│   ├── config.py             ← settings loaded from .env
│   ├── llm_client.py         ← builds the LangChain LLM object
│   ├── simple_invoke.py      ← Feature 1: basic Q&A
│   ├── prompt_chain.py       ← Feature 2: prompt templates + LCEL chains
│   ├── chat_memory.py        ← Feature 3: multi-turn chat with memory
│   ├── streaming.py          ← Feature 4: streaming word-by-word output
│   ├── structured_output.py  ← Feature 5: typed JSON/Pydantic output
│   └── summarizer.py         ← Feature 6: text summarization
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Quick Start

```bash
# 1. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # Mac/Linux
# .venv\Scripts\activate         # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env if needed (defaults are already set)

# 4. Configure AWS credentials (if not already done)
aws configure

# 5. Enable model access in AWS Console
# Bedrock → Model catalog → Claude Haiku 4.5 → Enable

# 6. Run the full demo
python src/main.py

# Or run a single feature
python src/simple_invoke.py
python src/chat_memory.py
python src/streaming.py
```

## Features

| # | File | What It Shows |
|---|------|---------------|
| 1 | simple_invoke.py      | Basic LLM call — send a question, get an answer |
| 2 | prompt_chain.py       | Prompt templates with {placeholders} + LCEL | chains |
| 3 | chat_memory.py        | Multi-turn chat — AI remembers prior messages |
| 4 | streaming.py          | Word-by-word streaming output |
| 5 | structured_output.py  | Returns a Pydantic object instead of raw text |
| 6 | summarizer.py         | Summarizes text in bullet or paragraph format |

## Model

`us.anthropic.claude-haiku-4-5-20251001-v1:0` — Active as of June 2026.
Fast, affordable, excellent for all these use cases.
