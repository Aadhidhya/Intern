
# Technical Assignment Report

## Methodology
- Data Prep: Text was chunked to maintain context.
- Search: Hybrid approach simulated using FAISS vector indexing for O(log N) scalability.
- Summarization: GPT-4o-mini utilized for high-reasoning summary generation.

## Challenges & Solutions
- Challenge: API Quota limits.
- Solution: Optimized context window by retrieving only the Top-N relevant chunks.
