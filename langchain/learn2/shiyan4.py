import os

os.environ["OPENAI_API_KEY"] = "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"

from langchain.chat_models import ChatOpenAI
from langchain.schema import (HumanMessage,SystemMessage)
chat = ChatOpenAI(model_name="gpt-4", temperature = 0.8, max_tokens=60)


if __name__ == "__main__":
    message = [SystemMessage(content="你是一个很棒的智能助手"),
               HumanMessage(content="请给我的花店起个名字")]
    response = chat(message)
    print(response)