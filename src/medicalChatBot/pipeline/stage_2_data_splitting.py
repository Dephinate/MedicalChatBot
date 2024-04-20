from medicalChatBot.config.configurations import ConfigurationManager
from medicalChatBot.components.datasplitter import Splitter

class DataSplitterPipeline:
    def __init__(self,extracted_data) -> None:
        self.extracted_data=extracted_data

    def main(self):
        config = ConfigurationManager()
        data_splitter_config = config.get_datasplitter_config()
        data_splitter = Splitter(config=data_splitter_config)
        chunks = data_splitter.split_recursive(extracted_data=self.extracted_data)
        return chunks