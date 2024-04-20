from importlib import import_module
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from medicalChatBot.prompts import *


class PromptQueryHandler:

    def __init__(self) -> None:
        pass

    def load_prompt(self, template_name: str = None):
        # Dynamically import the module containing the prompt templates
        prompt_module = import_module("medicalChatBot.prompts")
        default_template_name = "default_template"

        # Check if template_name is None or if the template is not found
        if not template_name:
            template = getattr(prompt_module, default_template_name)
            print(f"No template name provided. Using default template: '{default_template_name}'.")
        else:
            try:
                # Get the template from the module based on the template name
                template = getattr(prompt_module, template_name)
            except AttributeError:
                # If template not found, use a default template``
                template = getattr(prompt_module, default_template_name)
                print(f"Template '{template_name}' not found. Using default template: '{default_template_name}'.")

        # Create a PromptTemplate object from the retrieved template
        prompt = PromptTemplate.from_template(template)
        return prompt
    
    def initialize_chain_with_retrievalqa(self,llm,vector_store,return_source_documents:bool,prompt=None,k:int=3):
        prompt = prompt or self.load_prompt()
        print("prompt: ",prompt)
        qa=RetrievalQA.from_chain_type(
            llm=llm, 
            chain_type="stuff", 
            retriever=vector_store.as_retriever(search_kwargs={'k': k}),
            return_source_documents=return_source_documents, 
            chain_type_kwargs={"prompt": prompt})
        return qa
