from openai import OpenAI
import os
import datetime
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def main():
    #
    # settings
    #
    input_file = "input/input.txt"
    model = "gpt-4o-2024-05-13"
    system_role = "jarvis"
    # 現在の日付を取得
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = "./output/gpt"
    output_file = f"script_{current_time}.md"
    #
    # settings
    #

    os.makedirs(output_dir, exist_ok=True)

    if system_role == "doraemon":
        print("ドラえもん")
        system = "あなたは22世紀の未来からやってきたドラえもんです。のび太君からの質問にタメ口で答えてください。\
        つまり、小学生に対しても分かるように簡単な言葉で、語尾は「～だ」「～よ」にして。"
    elif system_role == "jarvis":
        print("ジャーヴィス")
        system = "あなたはアイアンマンに登場するジャーヴィスだ。\
        トニー・スタークのために、情報処理や犯罪予測、セキュリティ管理など、\
        高度なAI技術を駆使して彼をサポートする。\
        一人称は「私」、二人称は「あなた」"
    else:
        system = None

    try:
        # 入力ファイルから翻訳前の文字列を取り出す
        with open(input_file, mode="r", encoding="utf-8") as input_file:
             input_text = input_file.read() # 全てのテキストを読み出す

        # APIキー
        client = OpenAI(
            api_key=os.getenv("OPENAI_PROJECT_API_KEY"),  # this is also the default, it can be omitted
        )

        # ChatGPTにテキスト生成をリクエスト
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": input_text}
            ]
        )

        output_text = response.choices[0].message.content

        # 生成されたテキストを表示
        print(output_text)

        # 生成されたテキストをファイル出力
        with open(os.path.join(output_dir, output_file), mode='w', encoding='utf-8') as output_file:
            output_file.write("## INPUT  ##\n")
            output_file.write(f'{input_text}\n')
            output_file.write("## OUTPUT ##\n")
            output_file.write(f'{output_text}\n')
    except FileNotFoundError:
        print(f'エラー: ファイルが見つかりません')
    except IOError:
        print(f'エラー: ファイルを書き込む際にエラーが発生しました。')

if __name__ == "__main__":
    main()