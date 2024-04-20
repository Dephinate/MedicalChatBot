import pypdf
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from medicalChatBot.entity  import DataLoaderConfig
from medicalChatBot.config.configurations import ConfigurationManager


class DataLoader:
    def __init__(self,
                 config : DataLoaderConfig)->None :
        self.config = config

    # Extract data from the pdf
    def load_pdf(self):
        loader = DirectoryLoader(   # To load all pdfs from a directory
            path=self.config.data_path,
            glob=self.config.file_types,
            loader_cls=PyPDFLoader,
            show_progress=True
        )
        documents = loader.load()
        return documents