import os

os.environ["OPENAI_API_KEY"] = "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"

from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import Docx2txtLoader
from langchain.document_loaders import TextLoader

base_dir = 'langchain/learn2/xianhua_pj/doc/'
documents = []

# 加载数据
for file in os.listdir(base_dir):
    file_path = os.path.join(base_dir,file)
    if file_path.endswith('.pdf'):
        loader = PyPDFLoader(file_path)
        documents.extend(loader.load())
    elif file.endswith('.docx') or file_path.endswith('.doc'):
        loader = Docx2txtLoader(file_path)
        documents.extend(loader.load())
    elif file.endswith('.txt'):
        loader = TextLoader(file_path)
        documents.extend(loader.load())

# 文本切分
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200,chunk_overlap=10)
chunk_documents = text_splitter.split_documents(documents)

# 向量数据库存储
