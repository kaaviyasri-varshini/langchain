# pip install langchain langchain-community jq

from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    file_path="people.json",
    jq_schema=".[].name",
    text_content=False
)

docs = loader.load()

for d in docs:
    print(d.page_content)
    print(d.metadata)