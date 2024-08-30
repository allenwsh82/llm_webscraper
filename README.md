# llm_webscraper


Basically what is web scraper?


Web scraping is the process of using bots to extract content and data from a website. Unlike screen scraping, which only copies pixels displayed onscreen, web scraping extracts underlying HTML code and, with it, data stored in a database. The scraper can then replicate entire website content elsewhere.



End to End Web Scraping with RAG Pipeline Block Diagram

<img width="950" alt="End_2_End_Web_Scraping_RAG" src="https://github.com/user-attachments/assets/b0e0dfa2-3088-41cc-a05c-3dbca3cc514f">



RAG Framework: LlamaIndex (https://www.llamaindex.ai/) 
[Production ready LLM application]

Model Serving Framework / Libraries : Ollama (https://ollama.com/)
User Interface : Streamlit (https://streamlit.io/) 
URL Reader API: SimpleWebPageReader 
LLM Model: meta-llama/Meta-Llama-3.1-8B-Instruct [The latest and greatest model from Meta !]
Embedding Model: BAAI/bge-large-en-v1.5 (https://lnkd.in/eKNWQMVV)
Vector Store: In Memory from LlamaIndex (https://lnkd.in/gZWqXRvv)
 
Inference Hardware Configuration: 

CPU : Intel 4th Gen Xeon 8480+
RAM usage: 12GB (During RAG Prompt), 5GB (During document indexing)
OS: Ubuntu 22.04

Key Components / Features:

1. reader = SimpleWebPageReader
Reader API used to simplify data ingestion from multiple sources which include webpages for processing and data extraction.
Follow this URL: https://lnkd.in/e-_yEFZk

3. query_engine = index.as_query_engine
query engine API takes in natural language query and generates a rich response to the user. It has built in one or many indexes capacities as retrievers which simplify the process of building a AI ChatBot with RAG capabilities.
Follow this URL: https://lnkd.in/ezpK-RF9

5. index = VectorStoreIndex.from_documents
Vector Stores are key component in RAG and you can easily call out this function from LlamaIndex to load a set of documents and build an index from them using from_documents.
Follow this URL: https://lnkd.in/evJQsj-M

7. Settings.llm=Ollama(model="llama3.1")
Ollama allows user to setup and run a local ollama instance with your desired model. In this demo, llama3.1-8B is being used and setting up ollama with LlamaIndex framework is so much easier.
Follow this URL: https://lnkd.in/eWsN9Uxb


Summary:

1) Building a NLP workload with RAG is pretty easy and straightforward by using open source frameworks such as LlamaIndex 

2) There is so many ready APIs with different functionality and usages to use which you can refer to think link: https://lnkd.in/eCBWja99

3) By following the guidelines and examples from LlamaIndex official documentation, developers and enterprises can integrate LlamaIndex framework into their projects to enhance the capabilities and performances running it either on CPU, GPU or AI Accelerator.


How to run llm with web scraping with RAG Demo:

1) Clone the project: git clone https://github.com/allenwsh82/llm_webscraper
   
3) Create a new environment for this project: python -m venv webscaper_env
   
5) Activate the environment: source webscraper_env/bin/activate
   
7) Setup the environment with all the dependencies: pip install -r requirements.txt
   
9) Run the demo script by this command: streamlit run web_scraper.py



User Interface Demo 

<img width="950" alt="Web_Scraper_RAG_1" src="https://github.com/user-attachments/assets/ea80d361-3303-4990-97f1-7c518ccd17ac">

