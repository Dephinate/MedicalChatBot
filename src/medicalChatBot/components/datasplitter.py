# Data Splitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from medicalChatBot.entity  import SplitterConfig

class Splitter:
    def __init__(self,
                 config:SplitterConfig) -> None:
        self.config = config

    # function to impement recursive text splitting 
    def split_recursive(self, extracted_data:None):
        splitter = RecursiveCharacterTextSplitter(chunk_size = self.config.chunk_size  , chunk_overlap = self.config.chunk_overlap, separators=['\n\n', '\n', '.', ','])
        chunks = splitter.split_documents(extracted_data)
        return chunks