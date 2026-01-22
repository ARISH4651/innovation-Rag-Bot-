import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

df = pd.read_csv("qa_data (1).csv")

context_text = ""

for _, row in df.iterrows():
   context_text += f"Q: {row['question']}\nA: {row['answer']}\n\n"

def ask_gemini(query):
    prompt = f"""You are an Q&A assistant. Use the following context to answer the question accurately.
     if the answer is not in the context, respond with "I don't know particular answer on this".
     Context:
     {context_text}

     Question:
    {query}
    """

    response = model.generate_content(prompt)
    return response.text.strip()

print("Rag-Bot is started")
print("="*50)

while True:
    user_input = input("You : ")
    if user_input.lower()=="exit":
        print("Exiting....")
        break
    answer = ask_gemini(user_input)
    print(f"Rag-Bot : {answer}\n")