import os
import faiss
from sentence_transformers import SentenceTransformer

class SemanticIndexer:
    """
    Indexes the local repository into a persistent knowledge graph.
    Drastically reduces token usage by only returning strictly relevant files to the LLM.
    """
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.IndexFlatL2(384) # 384-dimensional embeddings
        self.file_map = {}

    def ingest_codebase(self):
        print(f"Indexing repository at {self.repo_path}...")
        for root, _, files in os.walk(self.repo_path):
            for i, file in enumerate(files):
                if file.endswith(('.rs', '.go', '.ts', '.py')):
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    embedding = self.model.encode([content])
                    self.index.add(embedding)
                    self.file_map[i] = filepath
                    
        print(f"Index complete. {len(self.file_map)} files vectorized.")

if __name__ == "__main__":
    indexer = SemanticIndexer("/workspace")
    indexer.ingest_codebase()
  
