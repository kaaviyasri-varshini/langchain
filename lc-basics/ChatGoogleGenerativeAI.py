import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

examples = [
    {
        "question": "Who lived longer, Steve Jobs or Albert Einstein?",
        "answer": """Do we need additional questions? Yes.
    Steve Jobs died at the age of 56.
    Albert Einstein died at the age of 76.
    Final Answer: Albert Einstein lived longer than Steve Jobs."""
    },
    {
        "question": "When was Google's founder born?",
        "answer": """Do we need additional questions? Yes.
    Google's founders are Larry Page and Sergey Brin.
    Larry Page was born on March 26, 1973.
    Sergey Brin was born on August 21, 1973.
    Final Answer: Larry Page was born on March 26, 1973 and Sergey"""
    }
]

example_prompt = PromptTemplate.from_template(
    "Question:\n{question}\nAnswer:\n{answer}"
)

fewshot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    input_variables=["question"],
    suffix="Question:\n{question}\nAnswer:"
)

chain = fewshot_prompt | llm | StrOutputParser()

response = chain.invoke(
    {
        "question": "What are the main responsibilities of a prime minister?"
    }
)

print(response)
