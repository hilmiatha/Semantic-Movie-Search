from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

class moviesdb:
    def __init__(self, embeddings='hf', db_path='E:\Education\Personal Projects\RAG Semantic Movie Search\chroma_movies_db'):
        self.db_path = db_path
        if embeddings == 'hf':
            self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                            model_kwargs={'device': 'cpu'})
    def load_db(self):
        db = Chroma(persist_directory=self.db_path, embedding_function=self.embeddings)
        return db
    def get_movies(self, db, query):
        return db.similarity_search(query, k=1)