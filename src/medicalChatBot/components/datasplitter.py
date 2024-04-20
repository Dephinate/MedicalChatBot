# Data Splitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from medicalChatBot.entity  import SplitterConfig

class Splitter:
    def __init__(self,
                 config:SplitterConfig) -> None:
        self.config = config

    # function to impement recursive text splitting 
    def split_recursive(self,extracted_data:None,chunk_size:int=None, chunk_overlap:int=None, separators:list=None):
        chunk_size = chunk_size or self.chunk_size
        chunk_overlap = chunk_overlap or self.chunk_overlap
        separators = separators or self.separators
        
        splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size  , chunk_overlap = chunk_overlap, separators=['\n\n', '\n', '.', ','])
        chunks = splitter.split_documents(extracted_data)
        return chunks