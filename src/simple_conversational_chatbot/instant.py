from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

from langchain_core.messages import AIMessage,HumanMessage,SystemMessage

llm = AzureOpenAI()

chat_history = []
chat_history.append({"role":"system","content":"You are an helpfull assistant"})

print("---- Welcome to chatbot ----")

while True:
    user_input = input("Users : ")
    if(user_input.lower()=="bye"):
        print("Have a nice day")
        break
    chat_history.append({"role":"user","content":user_input})
    response = llm.chat.completions.create(model="ssdi-dev-4o",messages=chat_history)
    chat_history.append({"role":"assistant","content":response.choices[0].message.content})
    print("Assistant : ",response.choices[0].message.content)
