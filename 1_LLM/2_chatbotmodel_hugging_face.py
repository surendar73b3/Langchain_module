
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="laion/open-thoughts-4-code-qwen3-32b-annotated-32k_qwen3-8B_32k",
    task="text-generation",
    max_new_tokens=100
)

model = ChatHuggingFace(llm=llm)

result = model.invoke(
    "Who hit the most centuries in ODI international cricket?"
)

print(result.content)