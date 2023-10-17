import os

"""
需要设置huggingfacehub_api_token 调试通过
"""
os.environ["OPENAI_API_KEY"] = "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"

from langchain import HuggingFaceHub

llm = HuggingFaceHub(repo_id="bigscience/bloom-1b7")


if __name__ == "__main__":
    text = llm.predict("请给我的花店起个名字")
    print(text)
