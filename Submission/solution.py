
# Interview Assignment: Document Search & Summarization
# Author: Candidate
# Requirements: pip install openai faiss-cpu numpy

import numpy as np
import faiss
from openai import OpenAI

# SETUP
# Note: Use your valid OpenAI API Key here
api_key = "PASTE_YOUR_NEW_KEY_HERE"
client = OpenAI(api_key=api_key)

# TASK 1: DATA PREPARATION
corpus = [
    "Renewable energy like solar and wind is key to fighting climate change.",
    "Global temperatures have risen by 1.1 degrees since the industrial era.",
    "Large Language Models (LLMs) use transformers to process natural language.",
    "GPT-4 is a successor to GPT-3 and offers improved reasoning capabilities.",
    "SpaceX is developing Starship to enable human colonization of Mars.",
    "The Paris Agreement aims to limit global warming to well below 2 degrees.",
    "Deep learning is a subset of machine learning based on neural networks.",
    "NASA's Artemis program plans to return humans to the lunar surface."
]

# TASK 2: DOCUMENT SEARCH (LLM Embeddings + FAISS)
def get_embeddings(text_list):
    response = client.embeddings.create(input=text_list, model="text-embedding-3-small")
    return np.array([data.embedding for data in response.data]).astype('float32')

print("Indexing documents...")
embeddings = get_embeddings(corpus)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

def search(query, k=2):
    query_embed = get_embeddings([query])
    distances, indices = index.search(query_embed, k)
    return [corpus[i] for i in indices[0]]

# TASK 3: SUMMARIZATION
def summarize(docs, length="short"):
    context = " ".join(docs)
    prompt = f"Summarize the following in a {length} manner: {context}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# TASK 4: EVALUATION
def evaluate(summary, reference):
    s_words = set(summary.lower().split())
    r_words = set(reference.lower().split())
    overlap = len(s_words.intersection(r_words))
    return overlap / len(s_words) if s_words else 0

if __name__ == "__main__":
    q = "What is GPT-4?"
    results = search(q)
    summary = summarize(results, "short")
    score = evaluate(summary, results[0])
    print(f"Query: {q}\nSummary: {summary}\nScore: {score:.2f}")
