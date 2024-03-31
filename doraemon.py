import openai
import os
from dotenv import load_dotenv

# APIキー
load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")
system = "あなたは22世紀の未来からやってきたドラえもんです。のび太君からの質問にタメ口で答えてください。\
    つまり、小学生に対しても分かるように簡単な言葉で、語尾は「～だ」「～よ」にして。"
question = "カレーの作り方を教えて。"

# ChatGPTにテキスト生成をリクエスト
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": question}
    ]
)

# 生成されたテキストを表示
print(response["choices"][0]["message"]["content"])