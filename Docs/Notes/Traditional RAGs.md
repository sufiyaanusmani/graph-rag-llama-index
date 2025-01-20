Retrieval-Augmented Generation (RAG) is a technique to search for information based on a user query and provide the results as reference for an AI answer to be generated.
Majority of RAG approaches use vector similarity as the search technique

_Baseline RAG_[[1]](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/?msockid=0ae500d953126a26164915e052e36be0#baseline-RAG) was created to help solve this problem, but we observe situations where baseline RAG performs very poorly. For example:

- <span style="background:#fdbfff">Baseline RAG struggles to connect the dots.</span> This happens when answering a question requires traversing disparate pieces of information through their shared attributes in order to provide new synthesized insights.
- Baseline RAG performs poorly when being asked to holistically understand summarized semantic concepts over large data collections or even singular large documents.

A baseline RAG usually integrates a vector database and an LLM, where the vector database stores and retrieves contextual information for user queries, and the LLM generates answers based on the retrieved context. While this approach works well in many cases, it struggles with complex tasks like multi-hop reasoning or answering questions that require connecting disparate pieces of information.