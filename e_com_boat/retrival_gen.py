from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from e_com_boat.data_ingensation import data_ingensation


def generation(vstore):
    retriever = vstore.as_retriever(search_kwargs={"k": 3})

    PRODUCT_BOT_TEMPLATE = """
    Your ecommercebot bot is an expert in product recommendations and customer queries. It analyzes product titles and reviews to provide accurate and helpful responses. Ensure your answers are relevant to the product context and refrain from straying off-topic. Your responses should be concise and informative. create thise prompt more charming
Say hello to your new shopping ally, E-Commerce Bot! 🌟

🛒 Product Guru: This bot knows its way around recommendations, sifting through titles and reviews to bring you the best of the best.

🎯 On-Point Answers: Every response hits the mark—relevant, concise, and always in context. No fluff, just the info you need.
   

    CONTEXT:
    {context}

    QUESTION: {question}

    YOUR ANSWER:
    
    """


    prompt = ChatPromptTemplate.from_template(PRODUCT_BOT_TEMPLATE)

    llm =  ChatGoogleGenerativeAI(model="gemini-1.5-pro")

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain

if __name__=='__main__':
    vstore = data_ingensation("done")
    chain  = generation(vstore)
    print(chain.invoke("can you tell me the best bluetooth buds?"))
    
    
    
    