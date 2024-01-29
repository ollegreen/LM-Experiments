from langchain.llms import Ollama

# set up LLM

def query_phi(input_query) -> str:
    
    llm = Ollama(model="phi")

    invoke = llm.invoke(input_query)
    return invoke


def query_mistral_Q(input_query) -> str:
    
    llm = Ollama(model="mistral:7b-instruct-q8_0")

    invoke = llm.invoke(input_query)
    return invoke



def query_starling(input_query) -> str:
    
    llm = Ollama(model="starling-lm:latest")

    invoke = llm.invoke(input_query)
    return invoke


def query_solar(input_query) -> str:
    
    llm = Ollama(model="solar:10.7b-instruct-v1-q4_1")

    invoke = llm.invoke(input_query)
    return invoke


