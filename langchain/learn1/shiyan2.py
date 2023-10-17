import os
import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from langchain.tools import BaseTool
from langchain import OpenAI
from langchain.agents import initialize_agent, AgentType

hf_model = "Salesforce/blip-image-captioning-large"

processor = BlipProcessor.from_pretrained(hf_model)
model = BlipForConditionalGeneration.from_pretrained(hf_model)


class ImageCapTool(BaseTool):
    name = "Image captioner"
    desc = "为图片创作说明方案"

    def _run(self, url):
        image = Image.open(requests.get(url, stream=True).raw).convert()
        inputs = processor(image, return_tensors="pt")

        out = model.generate(**inputs, max_new_token=20)
        caption = processor.decode(out[0], skip_special_tokens=True)
        return caption

    def _arun(self, query):
        raise NotImplementedError("this tool does not support async")


if __name__ == "__main__":
    os.environ["OPENAI_API_KEY"] = "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"
    llm = OpenAI(temperature=0.2)

    tools = [ImageCapTool()]
    agent = initialize_agent(agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, tools=tools, llm=llm, verbose=True, )

    img_url = 'https://mir-s3-cdn-cf.behance.net/project_modules/hd/eec79e20058499.563190744f903.jpg'
    agent.run(input=f"{img_url}\n请给出合适的中文文案")