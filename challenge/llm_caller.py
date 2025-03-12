import yaml
from langchain.chains.llm import LLMChain

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM


class LLMCaller:

    def call_llm(
        self,
        prompt: str,
        data: dict,
        temperature: float = 0.0,
    ) -> str:

        model = OllamaLLM(model="llama3.2", temperature=temperature)
        chain = prompt | model
        results_raw = chain.invoke(data)

        return results_raw
