import os

os.environ["OPENAI_API_KEY"] = "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"

from langchain.llms import OpenAI

llm = OpenAI(model_name="text-davinci-003", temperature = 0.8, max_tokens=200)


if __name__ == "__main__":
    text = llm.predict("请给我的花店起个名字")
    print(text)
