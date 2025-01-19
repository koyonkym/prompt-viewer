# Prompt Viewer App

## English Version

### Live App
Access the deployed app here: [Prompt Viewer App on Streamlit](https://prompt-viewer-s5qc4jcsvrfkspnrtftqh4.streamlit.app/)

### Background
When doing prompt engineering, it’s convenient to use Microsoft Excel or Google Spreadsheet to manage prompt versions and their outputs. However, when it comes to viewing a specific prompt or output or comparing different prompts or outputs, these tools can be cumbersome. To address this, I developed a simple prompt viewer app using Streamlit.

### How to Use (Local Deployment)

1. **Make a Python virtual environment**
    ```bash
    python -m venv env
    ```

2. **Activate the virtual environment**
- On Windows:
  ```bash
  .\env\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source env/bin/activate
  ```

3. **Install the required packages**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**
    ```bash
    streamlit run app.py
    ```

5. **Copy the entire sheet from Excel or Spreadsheet and paste it at the top of the UI**

6. **Select the prompt or output you want to view using the selectbox**

<br>
<br>
<br>

## Japanese Version

### Live App
次のリンクからアプリにアクセスできます: [Prompt Viewer App on Streamlit](https://prompt-viewer-s5qc4jcsvrfkspnrtftqh4.streamlit.app/)

### 背景
プロンプトエンジニアリングを行う際、プロンプトのバージョンや出力結果を管理するために、Microsoft Excel や Google Spreadsheet は便利です。しかし、特定のプロンプトや出力結果を表示したり、比較したりする場合、これらのツールは使いづらいと感じることがあります。そこで、Streamlit を使ってシンプルな Prompt Viewer App を作成しました。

### 使い方 (ローカル実行)

1. **Python 仮想環境を作成する**
    ```bash
    python -m venv env
    ```

2. **仮想環境を有効化する**
- Windows の場合:
  ```bash
  .\env\Scripts\activate
  ```
- macOS/Linux の場合:
  ```bash
  source env/bin/activate
  ```

3. **必要なパッケージをインストールする**
    ```bash
    pip install -r requirements.txt
    ```

4. **アプリケーションを実行する**
    ```bash
    streamlit run app.py
    ```

5. **Excel または Spreadsheet からシート全体をコピーし、UI の上部に貼り付ける**

6. **表示したいプロンプトや出力結果を selectbox を使用して選択する**