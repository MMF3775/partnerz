import json
import re
import os
from langchain.schema import Document


class DocumentLoader:
    def __init__(self,):
        self.doc = []

    def load_json(self, path: str):
        """ Load json file"""
        with open(path, 'r') as f:
            docs = json.load(f)

        self.doc.extend([Document(
            page_content=f"Question:{doc.get('content')}\nAnswer: {doc.get('content')}\nSource: {doc.get('url')}",
            metadata={"source": path,
                      "page": idx+1,
                      "format": "json",
                      "file_name": os.path.basename(path)}
        )for idx,doc in enumerate(docs)])

    def load_pdf(self,path: str):
        """ Load pdf file"""
        pass

    def load_txt(self,path:str):
        """ Load txt file"""
        pass


    @property
    def content(self):
        """Get content from the loaded document."""
        return [item.page_content for item in self.doc]

    @property
    def metadata(self):
        """Get metadata from the loaded document."""
        return [item.metadata for item in self.doc]

    @property
    def document(self):
        """Get metadata from the loaded document."""
        return self.doc

