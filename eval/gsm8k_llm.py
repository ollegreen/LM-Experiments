from datasets import load_dataset
from langchain.llms import Ollama


# set up GSM8K
GSM8K = load_dataset("gsm8k", 'main')

def get_GSM8K_QA(question_or_answer, question_number) -> str:

    if question_or_answer == "Q":
        output = GSM8K['train']['question'][question_number-1]
    elif question_or_answer == "A":
        output = GSM8K['train']['answer'][question_number-1]
    else:
        output = "either put 'Q' for question or 'A' for answer"

    return output


def check_answer_using_llm(llm_answer: str, benchmark_answer: str, ollama_model_name: str = "starling-lm:latest"):

        # set up LLM
    llm = Ollama(model=ollama_model_name)

    def query_llm(input_query) -> str:
        invoke = llm.invoke(input_query)
        return invoke

    def GSM8K_QA(question_number) -> str: # TODO: fix

        question = GSM8K['train']['question'][question_number-1]
        answer = GSM8K['train']['answer'][question_number-1]

        return question, answer


    extract_llm_number = query_llm(f"What is the final numerical answer of this text: {llm_answer}")
    extract_benchmark_number = query_llm(f"What is the final numerical answer of this text: {benchmark_answer}")

    compare = query_llm(f"Are these two answers the same: 1; [{extract_llm_number}] and 2; [{extract_benchmark_number}]")
    compare_binary = query_llm(f"You are a binary analyser returning a single digit. If the upcoming text is said to have the same answers, you return [1]. If they are not the same you return [0]. Here is the text: {compare}")

    print(f"extract_llm_number output: {extract_llm_number}")
    print(f"extract_gsm8k_number output: {extract_benchmark_number}")
    print(f"compare output: {compare}")
    print(f'compare binary output: {compare_binary}')