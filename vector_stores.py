from langchain_chroma import Chroma
import config_data as config

class VectorStoreService(object):
    def __init__(self,embedding):
        self.embedding = embedding

        self.vector_store = Chroma(
            collection_name=config.collection_name,
            embedding_function=self.embedding,
            persist_directory=config.persist_directory,
        )

    def get_retriever(self):
        #向量检索
        return self.vector_store.as_retriever(search_kwargs={"k":config.similarity_threshold})



if __name__ == '__main__':
    from langchain_community.embeddings import DashScopeEmbeddings
    import dotenv
    import os

    dotenv.load_dotenv()

    retriever = VectorStoreService(DashScopeEmbeddings(model="text-embedding-v4",dashscope_api_key=os.getenv("OPENAI_API_KEY"))).get_retriever()
    res=retriever.invoke("城市场景图像分割属于什么方向")
    print(res)

