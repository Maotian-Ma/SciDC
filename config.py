"""
SciDC Global Configuration File
The user is required to complete all configuration items in this file.
"""

# ============================================================================
# API Config (GLLM - CoT & Constraint Code Generation)
# ============================================================================
API_KEY = '<KEY>'
API_BASE_URL = '<BASE>'
API_MODEL = '<GLLM_MODEL>'


# ============================================================================
# DLLM Config (Local Model - For Constraint Generation)
# ============================================================================
DLLM_MODEL_PATH = "<DLLM_MODEL_PATH>"


# ============================================================================
# Task Config (Domain Knowledge Doc & User Tasks)
# ============================================================================
KNOWLEDGE_BASE_PATH = "prompts/domain_knowledge.txt"
COT_PROMPT_PATH = "prompts/task_decomposition.txt"
CODE_GEN_PATH = "prompts/code_generation.txt"

with open(KNOWLEDGE_BASE_PATH, "r", encoding='utf-8') as f:
    KNOWLEDGE = f.read()

USER_TASK = "<USER_TASK>"

with open(COT_PROMPT_PATH, "r", encoding='utf-8') as f:
    COT_PROMPT = f.read()

with open(CODE_GEN_PATH, "r", encoding='utf-8') as f:
    CODE_GEN_PROMPT = f.read()


