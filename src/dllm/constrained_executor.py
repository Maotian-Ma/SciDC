from src.dllm.dllm import SciDC
from config import DLLM_MODEL_PATH, KNOWLEDGE, USER_TASK
from src.gllm.code_generator import generate_code

def exec_code():
    code = generate_code()
    lm = SciDC(model_name=DLLM_MODEL_PATH)

    lm.clear_context()
    lm._extra_data = {}

    system_prompt = "<|im_start|>system\nYou are a scientific expert. Please answer questions strictly in accordance with the provided domain knowledge.<|im_end|>\n"
    lm.set_context(system_prompt + "<|im_start|>user\n" + "Domain Knowledge: " + KNOWLEDGE + "\nTask: " + USER_TASK + "<|im_end|>\n")
    exec(code)
    return str(lm)
