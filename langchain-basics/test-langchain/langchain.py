from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(

    model="gemini-2.5-flash",
    temperature=0.7,
)

response = llm.invoke("What is the capital of Canada?")
print(response)


 