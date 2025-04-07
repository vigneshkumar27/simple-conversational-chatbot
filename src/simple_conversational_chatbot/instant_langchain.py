from langchain_openai import AzureChatOpenAI
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage

from dotenv import load_dotenv

load_dotenv()

llm = AzureChatOpenAI(model="")

chat_history = []

chat_history.append(SystemMessage(content="'You are an assistant"))

while True:
    user_input = input("User :: ")
    if(user_input.lower() == 'exit'):
        print(chat_history)
        print("Have a great day")
        break
    chat_history.append(HumanMessage(user_input))
    response = llm.invoke(chat_history)
    chat_history.append(AIMessage(response.content))
    print("Assistant :: ",response.content)
