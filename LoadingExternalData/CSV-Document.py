from langchain_community.document_loaders import CSVLoader

# Step 1: Give your CSV file path
file_path = "titanic.csv"   # make sure file is in same folder

# Step 2: Create loader
loader = CSVLoader(file_path=file_path)

# Step 3: Load data
documents = loader.load()

# Step 4: Print basic info
print("Total rows loaded:", len(documents))

# Step 5: Show first 2 rows
for i in range(2):
    print(f"\n--- Row {i+1} ---")
    print("Content:")
    print(documents[i].page_content)

    print("\nMetadata:")
    print(documents[i].metadata)