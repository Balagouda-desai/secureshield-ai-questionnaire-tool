import os
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Lazy load model (fix for Render memory issue)
model = None


def get_model():
    global model
    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model


# 1️⃣ Load reference documents
def load_reference_documents(folder_path):

    documents = []

    for filename in os.listdir(folder_path):

        filepath = os.path.join(folder_path, filename)

        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()

            documents.append({
                "filename": filename,
                "text": text
            })

    return documents


# 2️⃣ Split documents into chunks
def chunk_documents(documents, chunk_size=200):

    chunks = []

    for doc in documents:

        text = doc["text"]

        words = text.split()

        for i in range(0, len(words), chunk_size):

            chunk_text = " ".join(words[i:i+chunk_size])

            chunks.append({
                "filename": doc["filename"],
                "text": chunk_text
            })

    return chunks


# 3️⃣ Create embeddings for chunks
def create_embeddings(chunks):

    model = get_model()

    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(texts)

    return embeddings


# 4️⃣ Find best matching chunk for a question
def find_best_match(question, chunks, chunk_embeddings):

    model = get_model()

    question_embedding = model.encode([question])

    similarities = cosine_similarity(question_embedding, chunk_embeddings)[0]

    best_index = np.argmax(similarities)

    best_chunk = chunks[best_index]

    confidence = similarities[best_index]

    return best_chunk, confidence