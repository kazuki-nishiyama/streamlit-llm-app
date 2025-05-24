from dotenv import load_dotenv
from langchain.schema import SystemMessage, HumanMessage
import os
from openai import OpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain.chat_models import ChatOpenAI  # 追加

# .envファイルの読込み
load_dotenv()

#環境変数の取得
openai_key = os.getenv("OPENAI_API_KEY")
print(f"openai_key: {openai_key}")


client = OpenAI(api_key=openai_key)




import streamlit as st

st.title("課題アプリ: 選択した専門家からLLMにより回答を得るアプリです")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["仕事のなやみ", "プライベートの悩み"]
)

st.divider()

if selected_item == "仕事のなやみ":
    input_message = st.text_input(label="質問事項となるテキストを入力してください。")
    if input_message:
        llm = ChatOpenAI(
            openai_api_key=openai_key,
            model="gpt-4o-mini",
            temperature=0.5,
            max_tokens=1000,
        )
        messages = [
            {"role": "system", "content": "あなたは仕事の悩みを解決するプロのアシスタントです."},
            {"role": "user", "content": f"質問内容: {input_message}"},
        ]
        result = llm.invoke(messages)  # invokeを使う
        result_content = result.content
        st.write(result_content)
else:
    input_message = st.text_input(label="質問事項となるテキストを入力してください。")
    if input_message:
        llm = ChatOpenAI(
            openai_api_key=openai_key,
            model="gpt-4o-mini", 
            temperature=0.5,
            max_tokens=1000,
        )
        messages = [
            {"role": "system", "content": "あなたはプライベートの悩みを解決するプロのアシスタントです."},
            {"role": "user", "content": f"質問内容: {input_message}"},
        ]
        result = llm.invoke(messages)
        result_content = result.content
        st.write(result_content)

