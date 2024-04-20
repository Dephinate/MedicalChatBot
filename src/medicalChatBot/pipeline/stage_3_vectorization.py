from medicalChatBot.config.configurations import ConfigurationManager
from medicalChatBot.components.vectormanager import Vectorizer

class VectorizerPipeline:
    def __init__(self,vectorstore_instance,chunks) -> None:
        self.chunks=chunks
        self.vectorstore_instance=vectorstore_instance

    def main(self):
        config = ConfigurationManager()
        vectorizer_config = config.get_vectorization_config()
        vectorizer = Vectorizer(config=vectorizer_config)
        vectorizer.add_records_pinecone_db(vectorstore_instance=self.vectorstore_instance,chunks=self.chunks)