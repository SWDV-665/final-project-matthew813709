import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write an essay on penguins "}])
print(completion.choices[0].message.content)