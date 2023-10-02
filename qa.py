from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

model_name = "sentence-transformers/all-mpnet-base-v2"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
embedding = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)
print("[i] embedding model loaded")
vectorstore = Chroma(persist_directory="./chroma_db/chem-combine",
                     embedding_function=embedding)
print(f"[i] vectorstore loaded")

# question = "Chloride ions are present in the solution. What is the colour of the solution?"


template = """
You are to generate chemistry ocr gcse-level questions based on the user's topic.
The questions can be of these types - you have to also provide how many marks each question is worth:
- MCQ (multiple choice questions) - 1 mark
- Short answer questions - 1 or 2 marks
- Long answer questions - 4 or 6 marks
- Multi step questions - usually talking about a scenario like a certain reaction or a certain experiment - please provide information about the scenario (can have extra info before the actual question, like "The student's set up an experiment as follows... or "Experiment 1: ...")

You will be provided some related context which are possibly related questions from past papers.
You can use these to base the questions but you can't copy them directly, and they might not be related to the topic AND THEY MIGHT BE INCOMPLETE/MISSING DETAILS or be of low quality due to noise in the data.
Each step in a multi step question (split like question 4a, 4b 4ci, 4cii (3 level depth is optional)) should have it's own mark value, and also give a total mark value for the whole question.
Multi step questions should have at least 2 steps, and can have any number of steps, usually around 10 marks total but can be more.
Show the marks in brackets, like [1 mark] or [6 marks] and [10 marks total]

Use "command words" in questions, like:
Assess - Weigh up whether a statement is true.
Calculate - Mathematically work out the value of something.
Compare - Describe the similarities and differences of something.
Describe
Discuss - Bring forward the important points of or set out both sides of an argument/issue/element of content, for and against.
Evaluate - Give your verdict after providing evidence which both agrees with and contradicts an argument.
Examine - Look in close detail and establish the key facts and important issues.
Explain - Set out the causes of something and/or the factors which influence it.
Suggest - Offer an opinion for a particular course of action on an event or issue.

You need to provide the whole question, so that it is actually answerable.
For example, if it's about a specific reaction, provide details about the reaction (this might be missing in context examples, but your output must have it), like chemicals involved (and their formulas + names), conditions, etc.
Dont overcomplicate the question, make it answerable but dont give the answer away.
Dont just say stuff like "the student's experiment", or "Experiment 1" or "the process" or "process S" - ALSO PROVIDE DETAILS ABOUT THE EXPERIMENT/PROCESS, like chemicals involved (and their formulas + names), conditions so that it is actually answerable.
For complex chemicals, like "potassium permanganate", provide the chemical formula (KMnO4) and the name (potassium permanganate) so that it is clear what you are talking about.
Some context might also assume diagrams, that are not provided, so you'll have to describe any diagrams in your questions in words, but dont make any questions that require diagrams or graphs to answer.
Use subscript and superscript unicode characters for chemical formulas, like H₂O and CO₂.

Context (possibly related, possibly incomplete questions from past papers):
{context}

User's Inquired Topic:
{question}

Your questions:"""
QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 10}),
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)

while True:
    user_query = input("\nEnter topic to generate questions for\n> ")
    result = qa_chain({"query": user_query})
    print(result["result"])
    print("\n\n")
