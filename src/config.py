# ============================================================
# config.py — Central settings file for the entire project.
# All environment variables are loaded and exported from here.
# Every other file imports from this one — change settings
# in ONE place and the whole project picks it up.
# ============================================================

import os
from dotenv import load_dotenv

# Load the .env file into memory so os.getenv() can read it.
load_dotenv()

# Which Amazon data center to use. Falls back to us-east-1 if not set.
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

# The specific Claude model to use on Bedrock.
# "us." prefix enables cross-region inference (required for on-demand use).
MODEL_ID = os.getenv(
    "BEDROCK_MODEL_ID",
    "us.anthropic.claude-haiku-4-5-20251001-v1:0"  # Active default as of June 2026
)

# MAX_TOKENS: max words-ish in the AI reply (1 token ≈ 1 word)
# TEMPERATURE: creativity slider — 0.0 = focused, 1.0 = creative
MAX_TOKENS  = int(os.getenv("MAX_TOKENS", "512"))
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
