from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import  StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from openai import BadRequestError

load_dotenv()

llm = ChatOpenAI()

web_prompt = PromptTemplate(
    template="Answer the following question - \n {question} from the following {text}.",
    input_variables = ["question", "text"]
)

str_parser = StrOutputParser()

chain = web_prompt | llm | str_parser

def summarize_webpage(page_url):
    web_loader = WebBaseLoader(page_url)
    web_docs = web_loader.load()

    try:
        summary_result = chain.invoke({"question": "Summarize the page content within 500 words.", "text": web_docs[0].page_content})

        return summary_result
    except BadRequestError:
        return ""