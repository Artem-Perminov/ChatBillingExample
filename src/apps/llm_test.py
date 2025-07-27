import asyncio
from src.services.llm import LLMService


async def main():
    llm = LLMService(model_name="llama3.2:3b", ollama_base_url="http://localhost:11434")
    result = await llm.execute(text="Hi, how are you?", history=[])
    print(result)


if __name__ == "__main__":
    asyncio.run(main())