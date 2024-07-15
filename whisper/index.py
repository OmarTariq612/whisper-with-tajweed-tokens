#!/bin/python3

from base64 import b64encode
import shutil
from json import load

PATH = "./assets/multilingual.tiktoken"
OUT_PATH = "./assets/multilingual_new.tiktoken"

with open(PATH) as file:
    lines = file.readlines()
    lastline = lines[-1]
    _, last_token_id = lastline.split()
    last_token_id = int(last_token_id)

# 1. copy the tokens
shutil.copyfile(PATH, OUT_PATH)


# 2. insert new ones
with open("new_tokens.json") as new_tokens_file:
    new_tokens_json = load(new_tokens_file)

with open(OUT_PATH, "a") as file:
    new_tokens = new_tokens_json.keys()
    for new_token in new_tokens:
        last_token_id += 1
        file.write(f"{b64encode(new_token.encode()).decode('utf-8')} {last_token_id}\n")
