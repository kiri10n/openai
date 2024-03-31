## ChatGPT API のテストなど
### 使い方
#### APIキーの取得
OpenAIのAPIキーを取得する。```.env```ファイルを作成し、  
```
OPENAI_API_KEY = "your API key"
```  
のように記載する。

#### ライブラリ
```
python -m venv .venv
```
で仮想環境を作った後、  
Windowsなら最初に一度だけ
```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```
をした後、
```
.venv\Scripts\Activate.ps1
```
MacOSなら
```
. .venv/bin/activate
```
を打つ。これで仮想環境に入れる。  
(.venv)がターミナルのパスの前につくはず。  
この状態で
```
pip install python-dotenv
pip install openai
```
でライブラリをインストールできる

#### 実行
```input```フォルダおよび```output```フォルダを作成し、```input```フォルダ内に```input.txt```を入れる。
```input.txt```の中に、ChatGPTに入力するプロンプトを書き込む。
下のようになる
```
./
  ├ .venv/
  ├ input/
  │   └input.txt
  ├ output/
  ├ .env
  └ chatgpt.py
```

ChatGPTで使うモデルは、```chatgpt.py```の中の```model```を変える。

ChatGPTに質問するときは、  
```
python chatgpt.py
```  
とする。

出力は```output```フォルダに溜まっていく。日付つきなので、連続で出力させてもファイルは上書きされない。
