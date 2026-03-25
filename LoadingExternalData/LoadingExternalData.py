#from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader


#document = Document("Hello, this is LangChain's document.")


FILE_PATH = "/home/sanjju/kact/langchain/LoadingExternalData/country.csv"
loader = PyPDFLoader(FILE_PATH)

docs = loader.load()
print(len(docs))
print(docs[1])