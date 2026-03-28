import json
import os
from typing import Sequence

from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage, message_to_dict, messages_from_dict

def get_history(session_id):
    return FileChatMessageHistory(session_id, "./chat_history")


class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self,session_id,storage_path):
        self.session_id=session_id
        self.storage_path=storage_path
        self.file_path=os.path.join(self.storage_path,self.session_id)

        os.makedirs(os.path.dirname(self.file_path),exist_ok=True)  #确保文件所在文件夹存在

    def add_messages(self, message: Sequence[BaseMessage]) -> None:

        all_message = list(self.messages)
        all_message.extend(message)

        new_message =[message_to_dict(message) for message in all_message]

        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump(new_message,f)

    @property
    def messages(self) -> list[BaseMessage]:
        try:
            with open(self.file_path,"r",encoding="utf-8") as f:
                message_data=json.load(f)
                return messages_from_dict(message_data)

        except FileNotFoundError:
            return []

    def clear(self) -> None:
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump([],f)



#
# dotenv.load_dotenv()
#
# model = ChatTongyi(model="qwen3-max",api_key=os.getenv("OPENAI_API_KEY"))
#
# prompt=ChatPromptTemplate.from_messages(
#     [
#         ("system","你需要根据会话历史来回答问题。历史："),
#         MessagesPlaceholder("chat_history"),
#         ("human","请回答如下问题：{input}")
#     ]
# )
# str_parser=StrOutputParser()
#
# def print_prompt(full_prompt):
#     print("="*20,full_prompt.to_string(),"="*20)
#     return full_prompt
#
# base_chain=prompt | print_prompt | model | str_parser
#
#

#
#
# #创建一个新练，对原有的练增强：自动附加历史消息
# conversation_chain=RunnableWithMessageHistory(
#     base_chain,  #被增强的练
#     get_history, #通过会话id获取inmemorychatmessagehistory类对象
#     input_messages_key="input",
#     history_messages_key="chat_history"
# )

if __name__=='__main__':
    pass
