# Language Models Experiments

Tinkering and test of new models and agent frameworks.

### To-dos
* Loop the LLM over GSM8K Qs and output the aggregated % correct answers. Make the loop output two things in a nice datastructure: (1) the actual table or number of % correct, and (2) the actual text LLM output/logic for each answer and question.

### Quick usage notes on Ollama models
* **Phi-2**: pretty damn good reasoning for such a small model. However using it: fair amount of verbose responses where it generates more user responses instead of simply answering the question, so often it becomes a bit problematic to use. Maybe can work with a bit of prompt engineering or more specific instructions or adding few-shot.
* **Mistral 7B 4-bit quantized**: seems pretty damn good for this size. Will keep in testing and write any cons that comes up.
* **starling-lm**: Highlighted on Reddit to be a solid model in use. but TBD for my own testing using GPT-4 labeled ranking dataset (Nectar), and new reward training and policy tuning pipeline.
* **Solar 10.7b-instruct-v1-q4_1**: Highlighted on Reddit to be maybe even better than starling.