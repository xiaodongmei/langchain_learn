import openai


openai.api_key = "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"
response = openai.Completion.create(model = "gpt-4",message = [{"role":"system","content":"you are a creative AI"},{"role":"user","content":"请给我的花店起个名字"}], temperature = 0.8, max_tokens = 60)

if __name__ == "__main__":
    print(response["choices"][0]["message"]["content"])