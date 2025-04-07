import json
import os
from . import utils
from dotenv import load_dotenv
from pathlib import Path

from langchain_openai import AzureChatOpenAI

load_dotenv()

def main():
    
    llm = AzureChatOpenAI(api_version="2024-05-01-preview",azure_deployment="")

    print("Welcome to chatbot \n Have a intresting journey \n Feel free to ask questions\n press /bye to quit")
    while True:
        user_input = input("User : ")
        if(user_input == '/bye'):
            break
        prompt = utils.construct_prompt(user_input)
        result = llm.invoke(prompt)
        utils.insert_history('assistant',result.content)
        print("Assistant : ",result.content)
