from medicalChatBot.config.configurations import ConfigurationManager
from medicalChatBot.components.dataloader import DataLoader

class DataLoaderPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_loader_config = config.get_dataloader_config()
        data_loader = DataLoader(config=data_loader_config)
        extracted_documents = data_loader.load_pdf()
        return extracted_documents