from langchain.llms import CTransformers
from langchain_community.llms import LlamaCpp
from medicalChatBot.entity import ModelConfig

class LoadModel:
    def __init__(self,
                 config:ModelConfig = None) -> None:
        self.config = config

    def load_model_from_ctransformers(self, model_path = None, model_type=None,max_new_tokens=None,n_ctx:int=None,temperature=None):
        model_path = model_path or self.config.model_path
        model_type = model_type or self.config.model_type
        max_new_tokens = max_new_tokens or self.config.max_new_tokens
        context_length = n_ctx or self.config.n_ctx

        temperature = temperature or self.config.temperature

        print(model_path)
        print(model_type)
        print(max_new_tokens)
        print(temperature)
        print(context_length)

        llm=CTransformers(model=model_path,
                        model_type=model_type,
                        config={'max_new_tokens':max_new_tokens,
                                'temperature':temperature,
                                'context_length': context_length})
        
        return llm
    
    def load_model_from_llamacpp(self,model_path:str=None, n_gpu_layers:int=None, n_batch:int=None, n_ctx:int=None, f16_kv:bool=None, temperature:int=None):
        model_path = model_path or self.config.model_path 
        n_gpu_layers = n_gpu_layers or self.config.n_gpu_layers 
        n_batch = n_batch or self.config.n_batch
        n_ctx = n_ctx or self.config.n_ctx
        f16_kv = f16_kv or self.config.f16_kv
        temperature = temperature or self.config.temperature
        
        print(model_path)
        print(n_gpu_layers)
        print(n_batch)
        print(n_ctx)
        print(f16_kv)
        print(temperature)
        
        lcpp_llm = None
        lcpp_llm = LlamaCpp(
            model_path=model_path,
            n_gpu_layers=n_gpu_layers,
            n_batch=n_batch,
            n_ctx=n_ctx,
            f16_kv=f16_kv, 
            temperature = temperature
            )
        return lcpp_llm
    
    def load_model(self):
        implementation_lower = self.config.implementation.lower()
        print(implementation_lower)
        if 'ctransformers' in implementation_lower:
            llm = self.load_model_from_ctransformers()
        elif 'llama' in implementation_lower or 'llamacpp' in implementation_lower:
            llm = self.load_model_from_llamacpp()
        return llm  