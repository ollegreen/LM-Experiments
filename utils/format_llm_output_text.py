from IPython.display import display, Markdown

def format_llm_answer(llm_output):
    formatted_string = llm_output.replace("\\n", "\n")
    formatted_output = display(Markdown(formatted_string))

    return formatted_output