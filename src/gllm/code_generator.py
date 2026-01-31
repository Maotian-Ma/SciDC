from .api_client import asking_api
from config import CODE_GEN_PROMPT, KNOWLEDGE, USER_TASK, COT_PROMPT, API_MODEL

def generate_cot():
    full_prompt = COT_PROMPT.format(domain_doc=KNOWLEDGE, _user_prompt=USER_TASK)
    cot = asking_api(full_prompt, model=API_MODEL)
    return cot

def generate_code():
    cot = generate_cot()

    prompt = CODE_GEN_PROMPT + "###Input \nDomain Knowledge: " + KNOWLEDGE + "\nUser Task: " + USER_TASK + "\nChain of Thought: " + cot
    code = asking_api(prompt, model=API_MODEL)
    return code



