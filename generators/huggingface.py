#!/usr/bin/env python3

from transformers import pipeline
from colorama import Fore, Back, Style

class HFBaseGenerator:
    def __init__(self, name, do_sample=True, num_return_sequences=10):
        print('loading '+Style.RESET_ALL+Fore.LIGHTMAGENTA_EX+'generator'+Style.RESET_ALL+': HF', name)
        self.generator = pipeline(
            'text-generation', 
            model=name, 
            do_sample=do_sample,
            num_return_sequences=num_return_sequences,
            )

    def generate(self, prompt):
        raw_output = self.generator(
            prompt,
            pad_token_id=self.generator.tokenizer.eos_token_id,
            )
        return [i['generated_text'] for i in raw_output]