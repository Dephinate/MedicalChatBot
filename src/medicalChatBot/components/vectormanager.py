import os
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain.embeddings import HuggingFaceEmbeddings
from medicalChatBot.entity import VectorizationConfig
from medicalChatBot.utils.common import load_env



class Vectorizer:
    def __init__(self,
                 config : VectorizationConfig = None) -> None:
        self.config = config

    def download_embeddings_from_huggingface(self,model_name:str = None):
        model_name = model_name or self.config.encoder_name
        embeddings = HuggingFaceEmbeddings(model_name=model_name)
        return embeddings
    
    def create_pinecone_instance(self,env_file_path:str = None):
        load_env(env_file_path=env_file_path)
        print("Key:",os.getenv('PINECONE_API_KEY'))
        pc = Pinecone(
            api_key = f"{os.getenv('PINECONE_API_KEY')}"
        )
        return pc
    
    def check_pinecone_index_status(self,db_instance, index_name = None):
        index_name = index_name or self.config.index_name
        index = db_instance.Index(index_name)
        return index.describe_index_stats()

    def create_pinecone_vectorstore_instance(self,db_instance=None,namespace=None,index_name=None,embeddings=None):
        index_name = index_name or self.config.index_name
        namespace = namespace or self.config.namespace
        
        vectorstore = PineconeVectorStore(
        index=db_instance.Index(index_name),
        embedding=embeddings,
        namespace=namespace,
        index_name=index_name
        )
        return vectorstore
    
    def clean_pinecone_db(self, db_instance,index_name:str=None,namespace:str=None):
        index_name = index_name or self.config.index_name
        namespace = namespace or self.config.namespace
        db_instance.Index(index_name).delete(delete_all=True,namespace=namespace)

    def add_records_pinecone_db(self,vectorstore_instance, chunks):
        vectorstore_instance.add_texts(texts=[t.page_content for t in chunks])

