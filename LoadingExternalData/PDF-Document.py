# pip install langchain langchain-community pypdf pymupdf

from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader

# Step 1: Give your PDF file path
file_path = "sample.pdf"   # keep PDF in same folder

# -------------------------------
# 1. PyPDFLoader (Simple & Easy)
# -------------------------------
print("\n--- Using PyPDFLoader ---")

loader = PyPDFLoader(file_path)
documents = loader.load()

print("Total pages:", len(documents))

# Show first page
print("\nFirst Page Content:\n")
print(documents[0].page_content[:300])

print("\nMetadata:\n")
print(documents[0].metadata)


# -------------------------------
# 2. PyMuPDFLoader (Better Output)
# -------------------------------
print("\n--- Using PyMuPDFLoader ---")

loader = PyMuPDFLoader(file_path)
documents = loader.load()

print("Total pages:", len(documents))

# Show first page
print("\nFirst Page Content:\n")
print(documents[0].page_content[:300])

print("\nMetadata:\n")
print(documents[0].metadata)