import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


llm=ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    
)

result = llm.invoke("who hit the most centuries in ODi international cricket?")

if isinstance(result.content, list):
    print(result.content[0]["text"])
else:
    print(result.content)