import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


llm=ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite", temperature=1.5,
    
)

result = llm.invoke("write a simple function in python to add two numbers")

if isinstance(result.content, list):
    print(result.content[0]["text"])
    
    
else:
    print(result.content)