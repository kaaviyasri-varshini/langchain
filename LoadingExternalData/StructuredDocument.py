from langchain_core.documents import Document
from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import CharacterTextSplitter
import asyncio

# 1. Create a Structured Document

doc = Document(
    page_content="This is my own custom data about AI and Python.",
    metadata={
        "source": "My Notes",
        "author": "Kaaviya"
    }
)

print("\n--- Basic Document ---")
print(doc)
print("\nInternal Structure:")
print(doc.__dict__)

# 2. Load Text as Documents

FILE_PATH = "./country.csv" 

loader = CSVLoader(FILE_PATH)

docs = loader.load()
print("\n--- Loaded Documents ---")
print(f"Total documents loaded: {len(docs)}")
print("\nSample Document:")
print(docs[0].page_content[:200])
print("Metadata:", docs[0].metadata)


# 3. Split Documents

text_splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0
)

split_docs = loader.load_and_split(text_splitter=text_splitter)
print("\n--- Split Documents ---")
print(f"Total chunks: {len(split_docs)}")


# 4. Lazy Loading (Streaming)

print("\n--- Lazy Loading ---")
for i, d in enumerate(loader.lazy_load()):
    print(f"Doc {i+1} metadata:", d.metadata)
    if i == 2:  # limit output
        break


# 5. Async Loading

async def load_async():
    adocs = await loader.aload()
    print("\n--- Async Loaded Documents ---")
    print(f"Total async docs: {len(adocs)}")

asyncio.run(load_async())


# 6. Manual Metadata Enrichment

print("\n--- Metadata Enrichment ---")
for d in docs[:2]:
    d.metadata["processed_by"] = "LangChain Pipeline"
    d.metadata["category"] = "AI Research"
    print(d.metadata)

#END
