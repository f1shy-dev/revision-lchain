from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

model_name = "sentence-transformers/all-mpnet-base-v2"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
embedding = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)
print("model loaded")
vectorstore = Chroma(persist_directory="./chroma_db/chem-combine",
                     embedding_function=embedding)
print("vectorstore loaded")
# question = "Chloride ions are present in the solution. What is the colour of the solution?"

while True:
    print("\033[H\033[J", end="")

    question = input("Enter query for vectorstore\n> ")
    docs = vectorstore.similarity_search(question, k=10)

    for doc in docs:
        print(
            f"\n\nfrom {doc.metadata['source']}, page {doc.metadata['page']}:")
        print(doc.page_content)

    print(f"\n\n{len(docs)} results")
    cont = input("Continue? (y/n)\n> ")
    if cont == "n":
        break
    print("\033[H\033[J", end="")
