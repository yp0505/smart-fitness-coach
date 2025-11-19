# app.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

import os
import plotly.graph_objects as go
import plotly
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")

EXAMPLE_PROMPTS = [
    "Design a 4-day strength program focused on compound lifts",
    "What should I eat before and after HIIT cardio?",
    "Give me a recovery checklist for the day after leg day",
    "Suggest supplements that boost energy without jitters",
    "Visualize a balanced weekly workout schedule"
]


def _base_context(request: Request, **kwargs):
    """Helper to keep shared template context tidy."""
    base = {
        "request": request,
        "response": "",
        "chart_json": None,
        "examples": EXAMPLE_PROMPTS
    }
    base.update(kwargs)
    return base

llm = OllamaLLM(model="llama3")
embeddings = OllamaEmbeddings(model="llama3")

file_topic_map = {
    "fitness_knowledge/workouts.md": "workout",
    "fitness_knowledge/nutrition.md": "nutrition",
    "fitness_knowledge/recovery.md": "recovery",
    "fitness_knowledge/supplements_motivation.md": "supplements"
}

retrievers = {}
for path, topic in file_topic_map.items():
    docs = TextLoader(path).load()
    chunks = CharacterTextSplitter(chunk_size=500, chunk_overlap=50).split_documents(docs)
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(f"fitness_vectorstore_{topic}")
    retriever = FAISS.load_local(
        f"fitness_vectorstore_{topic}",
        embeddings,
        allow_dangerous_deserialization=True
    ).as_retriever(search_kwargs={"k": 4})
    retrievers[topic] = retriever


def build_prompt(context: str, question: str) -> str:
    instructions = (
        "You are Smart Fitness Coach, a certified trainer and nutritionist. "
        "Use the provided knowledge snippets to deliver structured, actionable guidance. "
        "Format the answer with short sections, bullet points, and bold labels when helpful."
    )
    return (
        f"{instructions}\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}\n\n"
        "Answer:"
    )

def route_query(query):
    q = query.lower()
    if any(w in q for w in ["workout", "training", "exercise"]): return "workout"
    if any(w in q for w in ["eat", "calorie", "diet", "food", "protein"]): return "nutrition"
    if any(w in q for w in ["sleep", "recovery", "stress", "rest"]): return "recovery"
    if any(w in q for w in ["supplement", "motivation", "creatine", "whey"]): return "supplements"
    return "workout"

def generate_workout_chart():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    plan = ["Pushups", "Cardio", "Squats", "Rest", "HIIT", "Stretch", "Rest"]
    fig = go.Figure(data=[go.Table(
        header=dict(values=["Day", "Workout"], fill_color="lightblue", align="left"),
        cells=dict(values=[days, plan], fill_color="lavender", align="left")
    )])
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", _base_context(request))

@app.post("/", response_class=HTMLResponse)
async def handle_query(request: Request, query: str = Form(...)):
    print("Query received:", query)
    if "visualize" in query.lower():
        chart_json = generate_workout_chart()
        return templates.TemplateResponse(
            "index.html",
            _base_context(request, chart_json=chart_json)
        )
    try:
        topic = route_query(query)
        retriever = retrievers[topic]
        docs = retriever.get_relevant_documents(query)
        context = "\n\n".join(doc.page_content for doc in docs)
        prompt = build_prompt(context, query)
        result = llm.invoke(prompt)
        print("🧠 Response:", result)
    except Exception as e:
        result = f"Error: {str(e)}"
        print("Exception occurred:", result)

    return templates.TemplateResponse(
        "index.html",
        _base_context(request, response=result)
    )
