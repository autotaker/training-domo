# Day 1: Python開発環境構築

# 開発環境構築
## 0. Requirements
以下のツールがインストールされていることを前提にしています。
インストールしていない人は事前にインストールしておいてください。

- [git for windows](https://gitforwindows.org/)
- [VS Code](https://code.visualstudio.com/)

## 1. Clone Repository
このレポジトリを適当なディレクトリにcloneしてください。

```bash
git clone https://github.com/autotaker/training-domo.git
```

## 2. Install Python

1. [Microsoft Store](https://www.microsoft.com/ja-jp/p/python-310/9pjpw5ldxlz5)からPython 3.10をインストールしてください。
   - Windows以外の場合は [Python公式](https://www.python.org/downloads/release/python-3102/)からダウンロードしてください。
1. Powershellを開き、Pythonのバージョンを確認してください。`3.10.2`が表示されればOKです。

   ```
   python --version
   >>> Python 3.10.2
   ```

## 3. Install Pipenv
Pipenvをインストールします。

1. Powershellを開き、以下のコマンドで`pipenv`をインストールします。

   ```bash
   pip install --user pipenv
   ```

   - 社内プロキシ等を使っている場合、SSLの証明書エラーが発生することがあります。
     その場合はルート証明書をPEM形式で保存し、以下のコマンドでpipの`global.cert`オプションを設定してください。
     
     ```bash
     pip config --user set global.cert {ルート証明書へのパス}
     ```
2. 以下のコマンドでバージョンを確認してください。

   ```
   pipenv --version
   >>> pipenv, version 2022.1.8
   ```

## 4. Install dependencies
pipenvを使って依存ライブラリをダウンロードします。

1. このレポジトリ直下(`Pipefile`が存在するディレクトリ)で以下のコマンドを実行して依存ライブラリをインストールしてください。

   ```
   pipenv install
   ```
2. `day1/hello.py`を実行して、アスキーアートが表示されることを確認してください。

   ```
   pipenv run python day1/hello.py
   ```

   ![hello](./img/hello.png)

## 5. Install VSCode Extension
VSCode用Python Extension(`ms-python.python`)をインストールします。

1. [VSCode用Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)を開き、インストールボタンを教えてインストールしてください。
2. VSCode左側のExtensionsアイコン（四角が４つあるやつ）をクリックしてインストール済みExtension一覧に`Python`があることを確認してください。

   ![List of Extensions](./img/extensions-list.png)

## 6. Configure VS Code Workspace
1. レポジトリのディレクトリをVSCodeで開いてください
2. 画面左下に表示されているPythonのバージョンをクリックし、インタープリタ選択画面から(`'training-domo-...': pipenv`)を選択してください。
   
   ![Select Interpreter](./img/select-interpreter.png)
3. `day1/hello.py`をVSCodeで開き、赤線が表示されないことを確認してください。

   - 正しく設定できている場合

     ![OK](./img/correct-interpreter.png)

   - 設定が間違っている場合

     ![NG](./img/wrong-interpreter.png)

     設定が間違っている場合は、
     - インタプリタ選択画面が正しいか
     - `pipenv install`が成功しているか
     
     を確認してください
4. VSCodeからターミナルを開き、`python day1/hello.py`が実行できることを確認してください。
   
   ```Powershell
   pythton day1/hello.py
   ```

   もしPowershellスクリプトを実行できないエラーが表示された場合、実行ポリシーを変更してください。

   ```powerhsell
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
   ```

