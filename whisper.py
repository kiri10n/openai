import os
import datetime

from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def main():
    #
    # settings
    #
    input_file = "input/20240523.mp3"
    model = "whisper-1"
    dump = False
    # 現在の日付を取得
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"./output/script_{current_time}.md"
    #
    # settings
    #

    try:
        # APIキー
        client = OpenAI(
            api_key=os.getenv("OPENAI_PROJECT_API_KEY"),  # this is also the default, it can be omitted
        )

        with open(input_file, mode='rb') as input_file:
            transcription = client.audio.transcriptions.create(
                model=model,
                file=input_file
            )
        

        output_text = transcription.text

        # 生成されたテキストを表示
        print(output_text)

        if dump:
            # 生成されたテキストをファイル出力
            with open(output_file, mode='w', encoding='utf-8') as output_file:
                output_file.write("## OUTPUT ##\n")
                output_file.write(f'{output_text}\n')
    except FileNotFoundError:
        print(f'エラー: ファイルが見つかりません')
    except IOError:
        print(f'エラー: ファイルを書き込む際にエラーが発生しました。')

if __name__ == "__main__":
    main()