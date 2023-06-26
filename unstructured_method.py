from langchain.document_loaders import UnstructuredPDFLoader
from langchain.document_loaders import OnlinePDFLoader

loader = UnstructuredPDFLoader("DS do mang sang My.pdf", mode="elements")
# loader = OnlinePDFLoader("https://documentcloud.adobe.com/gsuiteintegration/index.html?state=%7B%22ids%22%3A%5B%221TD443W9POmVv22kCpVz01RFaBaIzqLCO%22%5D%2C%22action%22%3A%22open%22%2C%22userId%22%3A%22108822917465039894923%22%2C%22resourceKeys%22%3A%7B%7D%7D")

data = loader.load()

print(len(data))
for datum in data[:20]:
    print(datum.page_content)