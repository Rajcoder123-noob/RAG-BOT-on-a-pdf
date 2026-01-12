from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()
openai_client=OpenAI()

embedding_model=OpenAIEmbeddings(
    model="text-embedding-3-small"
    )

vector_db=QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

user_query=input("Ask somthing :")

search_results=vector_db.similarity_search(query=user_query)

contex="\n\n\n".join(
    [f"Page content:{result.page_content}\nPage no.:{result.metadata['page']}\nFile loc.:{result.metadata['source']}"
    for result in search_results]
)

PROMPT=f"""
You are a helpfull AI assistent who answers the user query based on the available context
retrieved from the PDF file along with page content,page no. and file location.

you should only answer the user query based on the following context provided and nevigate the user to open
the righ page in the PDF file to know more and not answer beyound the context.

context:
{contex}
"""
response=openai_client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role":"system","content":PROMPT},
        {"role":"user","content":user_query}
    ]
)
print(f"RAG BOT:{response.choices[0].message.content}")