import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from chatgpt_automation.chatgpt_automation import ChatGPTAutomation

chat = ChatGPTAutomation()


import pathlib
file_path = pathlib.Path("setup.py").parent.resolve().joinpath('setup.py').__str__()
file_path

chat.upload_file_for_prompt(file_path)

chat.send_prompt_to_chatgpt("can you explain this file?")


print(chat.return_last_response())