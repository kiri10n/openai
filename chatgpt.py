from openai import OpenAI
import os
from dotenv import load_dotenv

# APIキー
load_dotenv()
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)
question = """
"""

client = OpenAI()

# ChatGPTにテキスト生成をリクエスト
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": question}
    ]
)

# 生成されたテキストを表示
print(response.choices[0].message.content)