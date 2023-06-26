from langchain.document_loaders import PyPDFLoader
import os
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

loader = PyPDFLoader("clean_code.pdf")
pages = loader.load_and_split()

print(len(pages))
print(pages[0].page_content)


openai_key = os.environ.get("OPENAI_KEY")

faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings(openai_api_key=openai_key))
docs = faiss_index.similarity_search("bad", k=2)
for doc in docs:
    print(doc)
    # print(str(doc.metadata["page"]) + ":", doc.page_content[:300])