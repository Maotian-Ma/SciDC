import torch
from typing import List, Optional, Any
from vllm import SamplingParams
from vllm import LLM as VLLM
from vllm.sampling_params import StructuredOutputsParams
from transformers import AutoTokenizer
import json


class SciDC:
    def __init__(
            self,
            model_name: str,
            device: str = "cuda",
            note: dict = {},
            **kwargs
    ):
        self._context = ""
        self._extra_data = {}
        self.note = note

        self.vllm_model = VLLM(
            model=model_name,
            gpu_memory_utilization=0.8,
            tensor_parallel_size=torch.cuda.device_count() if device == "cuda" else 1,
            trust_remote_code=True,
            **kwargs
        )

        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

    def __setitem__(self, key: str, value: Any):
        self._extra_data[key] = value

    def __getitem__(self, key: str) -> Any:
        return self._extra_data.get(key)

    def __str__(self) -> str:
        return self._context

    def __iadd__(self, text: str) -> "SciDC":
        self._context += text
        return self

    def set_context(self, text: str) -> None:
        self._context = text

    def gen(
            self,
            max_tokens: int = 512,
            stop: Optional[List[str]] = None,
            temperature: float = 0.7,
            top_p: float = 0.95,
            name: str = "",
            regex: str = "",
            **kwargs
    ) -> str:

        # 准备停止词
        stop_token_ids = []
        if stop:
            for word in stop:
                tokens = self.tokenizer.encode(word, add_special_tokens=False)
                if tokens:
                    stop_token_ids.append(tokens[0])

        stop_list = stop if stop else []


        structured_outputs = None
        if regex:
            clean_regex = regex.replace('^', '').replace('$', '')
            structured_outputs = StructuredOutputsParams(regex=clean_regex)


        sampling_params = SamplingParams(
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            stop=stop_list,
            stop_token_ids=stop_token_ids if stop_token_ids else None,
            structured_outputs=structured_outputs,
        )

        try:
            outputs = self.vllm_model.generate(
                self._context,
                sampling_params=sampling_params
            )
            generated_text = outputs[0].outputs[0].text
        except Exception as e:
            print(f"Generation error: {e}")
            import traceback
            traceback.print_exc()
            generated_text = ""

        self._context += generated_text
        if name != "":
            self[name] = generated_text

        print(f"Generated ({name}): {generated_text}")
        return generated_text

    def select(
            self,
            options: List[str],
            name: str = "",
    ) -> str:
        prompt = self._context

        structured_outputs = StructuredOutputsParams(choice=options)
        sampling_params = SamplingParams(
            temperature=0,
            structured_outputs=structured_outputs,
        )

        try:
            outputs = self.vllm_model.generate(
                prompt,
                sampling_params=sampling_params
            )
            generated_text = outputs[0].outputs[0].text
        except Exception as e:
            print(f"Select generation error: {e}")
            import traceback
            traceback.print_exc()
            generated_text = ""

        self._context += generated_text
        if name != "":
            self[name] = generated_text
        return generated_text

    def clear_context(self) -> None:
        self._context = ""