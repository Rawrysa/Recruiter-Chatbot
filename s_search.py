import faiss
from sentence_transformers import SentenceTransformer

class SearchEngine:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.embeddings = None

    def chunk_text(self, text: str, chunk_size: int = 1000):
        paragraphs = text.split("\n\n")
        chunks = []
        current_chunk = ""
        for para in paragraphs:
            if len(current_chunk) + len(para) < chunk_size:
                current_chunk += para + "\n\n"
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = para + "\n\n"
        if current_chunk:
            chunks.append(current_chunk.strip())
        return chunks

    def build_index(self, texts):
        self.embeddings = self.model.encode(texts)
        D = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(D)
        self.index.add(self.embeddings)

    def search(self, query: str, k: int = 4):
        query_embedding = self.model.encode([query])
        d, i = self.index.search(query_embedding, k=k)
        return i
