# Template String
template1="""
[INST] <<SYS>>
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
<</SYS>>
Use the Context to answer the Question.
Context: {context}
Question: {question}[/INST]

"""

template2="""
Answer the question based on the context below.
If you don't know the answer, only return I don't know, Do not make an answer.

Context: {context}
Question: {question}

Answer:
"""


template3 = """
<<USER>> {question}

<<SYS>>
Answer the question based on the context below..
{context}
system_prompt: "You are a helpful assistant, below is ... llama-2-7b-chat.Q4_K_M.gguf"
"""

# Most effective Template String

default_template="""
[INST] <<SYS>>
Answer the query based on the information. If you don't know the answer, return 'I do not know', Do not make an answer.
<</SYS>>
query:{question}
information:{context}[/INST]

"""

template4 = """
<s>[INST] <<SYS>>
Answer the following. If you don't know the answer, return 'I do not know', Do not make an answer.
<</SYS>>
Based on the given information,
query:{question}

information:{context}[/INST]

"""
