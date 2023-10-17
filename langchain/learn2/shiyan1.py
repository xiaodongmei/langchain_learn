import openai


openai.api_key = "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"
response = openai.Completion.create(model = "text-davinci-003",temperature = 0.5, max_tokens = 100,
                                    prompt = "请给我的蛋糕店起个名字")

if __name__ == "__main__":
    print(response.choices[0].text.strip())