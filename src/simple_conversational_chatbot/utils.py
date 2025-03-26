import json
import pathlib

history_file = pathlib.Path(__file__).resolve().parent /'history.json'
def read_history():
    with open(history_file,'r') as file:
        data = json.load(file)
    return data

def insert_history(role,content):
    with open(history_file,'r+') as file:
        data = json.load(file)
        data.append({"role":role,"content":content})
        file.seek(0)
        json.dump(data,file, indent=4)
        file.truncate()
    return

def construct_prompt(user_message):
    prompt = [('system','You are an assistant. You answer to queries respectfully')]
    insert_history('user',user_message)
    history = read_history()
    for item in history:
        # print(item)
        prompt.append((item['role'],item['content']))
    return prompt