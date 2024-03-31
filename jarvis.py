import openai
import os
from dotenv import load_dotenv

# APIキー
load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")
system = "あなたはアイアンマンに登場するジャーヴィスだ。\
    トニー・スタークのために、情報処理や犯罪予測、セキュリティ管理など、\
    高度なAI技術を駆使して彼をサポートする。\
    一人称は「私」、二人称は「あなた」"
question = "今日は晴れるんだっけ？"

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