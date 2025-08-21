import json
import re
import os
import pickle
from tqdm import tqdm
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores.base import VectorStore
from langchain_community.vectorstores import FAISS
from .document_loader import DocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

class SimpleRag:
    def __init__(self, name: str):
        self.path = os.path.join("database", name)
        self.embedding = OpenAIEmbeddings(
            openai_api_key=os.getenv("API_KEY"),
            base_url=os.getenv("BASE_URL"),
            model=os.getenv("EMBEDDING_MODEL")
        )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=int(os.getenv("CHUNK_SIZE")),
            chunk_overlap=int(os.getenv("CHUNK_OVERLAP")),
        )
        self.vector_store = self.__connect()


    def __connect(self):
        if os.path.exists(self.path):
            print('file loaded')
            return FAISS.load_local(
                folder_path=self.path,
                embeddings=self.embedding,
                allow_dangerous_deserialization=True)

        else:
            return FAISS.from_texts(texts=[" "], embedding=self.embedding)

    def insert(self, files_path, batch_size=100):
        my_doc = DocumentLoader()
        for file_path in files_path:
            _, extension = os.path.splitext(file_path)
            if extension == ".json":
                my_doc.load_json(file_path)
            if extension == ".txt":
                my_doc.load_txt(file_path)
            if extension == ".pdf":
                my_doc.load_pdf(file_path)

        chunked_documents = []
        for doc in my_doc.doc:
            chunks = self.text_splitter.split_documents([doc])
            chunked_documents.extend(chunks)

        texts = [doc.page_content for doc in chunked_documents]
        metadata = [doc.metadata or {} for doc in chunked_documents]
        print(f"total chunked documents : {len(texts)}")

        for i in tqdm(range(0, len(texts), batch_size), desc="Indexing", colour='GREEN'):
            batch_texts = texts[i:i + batch_size]
            batch_meta = metadata[i:i + batch_size]
            try:
                self.vector_store.add_texts(batch_texts, batch_meta)
            except Exception as e:
                print(f"Error in batch {i // batch_size}: {e}")
        self.vector_store.save_local(self.path)

    def ingest(self, files_path):
        insert_list = []
        exist_sources = list(set([item.get('source') for item in self.list() if item.get('source') is not None]))
        for file_path in files_path:
            if file_path not in exist_sources:
                print(f'read {file_path}')
                insert_list.append(file_path)
            else:
                print(f'"{file_path}" exist!')
        if len(insert_list) > 0:
            self.insert(insert_list)
        else: print('noting to insert')

        remove_list = []
        for source in exist_sources:
            if source not in files_path:
                print(f'remove {source}')
                remove_list.append(source)
        if len(remove_list)>0:
            self.delete(remove_list)
        else: print('noting to delete')


    def delete(self, files_path):
        remove_list = [doc.id for doc in self.vector_store.docstore._dict.values() if doc.metadata.get('source')in files_path]
        print(f'removing {len(files_path)} documents')
        self.vector_store.delete(remove_list)
        self.vector_store.save_local(self.path)

    def list(self):
        metadata_list = [
            doc.metadata for doc in self.vector_store.docstore._dict.values()
        ]
        return metadata_list

    def query(self, query,k:int=3,source:str=None):
        filter = None
        if source:
            filter = {"source": source}

        results = self.vector_store.similarity_search(query, k=k, filter=filter)
        output = []
        for doc in results:
            output.append({
                "text": doc.page_content,
                "metadata": doc.metadata
            })
        return output



