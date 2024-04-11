from MedicalChatBot.constants import  *
from MedicalChatBot.entity import *
from MedicalChatBot.utils.common import read_yaml, create_directory, create_file

class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 param_filepath=PARAMS_FILE_PATH) -> None:
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(param_filepath)

        create_directory([self.config.artifacts_root])
        

    def get_vectorization_config(self)->VectorizationConfig:
        config = self.config.vectorization

        vectorizationConfig = VectorizationConfig(
            model_name = config.model_name,
            index_name = config.index_name,
            namespace = config.namespace,
            encoder_name = config.encoder_name,
            encoder_platform = config.encoder_platform,
            num_of_documnets = config.num_of_documnets
        )
        return vectorizationConfig
    
    def get_model_config(self)->ModelConfig:
        config = self.config.llm_model
        params_model = self.params.model_params

        modelConfig = ModelConfig(
            # LlamaCpp
            implementation = config.implementation,
            model_path = params_model.model_path,
            n_gpu_layers = params_model.n_gpu_layers,
            n_batch = params_model.n_batch,
            n_ctx = params_model.n_ctx,
            f16_kv = params_model.f16_kv, 
            temperature = params_model.temperature,
            # CTransformers
            model = params_model.model,
            model_type = params_model.model_type,
            max_new_tokens = params_model.max_new_tokens
        )
        return modelConfig
    
    def get_dataloader_config(self)->DataLoaderConfig:
        config = self.config.data_loader
        dataLoaderConfig =  DataLoaderConfig(
            data_path = config.data_path,
            file_types = config.file_types
        )
        return dataLoaderConfig

    def get_datasplitter_config(self)->SplitterConfig:
        config = self.config.data_splitter
        splitterConfig =  SplitterConfig(
            data_path = config.chunk_size,
            file_types = config.chunk_overlap
        )
        return splitterConfig