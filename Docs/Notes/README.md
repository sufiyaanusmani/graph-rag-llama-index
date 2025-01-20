[Baseline RAGs](Traditional%20RAGs.md)

GraphRAG uses LLM-generated knowledge graphs to provide substantial improvements in question-and-answer performance when conducting document analysis of complex information.

This concept is created by Microsoft Research

This builds upon our recent [research](https://www.microsoft.com/en-us/research/publication/can-generalist-foundation-models-outcompete-special-purpose-tuning-case-study-in-medicine/), which points to the power of prompt augmentation when performing discovery on [[Private Datasets]].

GraphRAG, uses the LLM to create a [[Knowledge Graph]] based on the private dataset. This graph is then used alongside graph machine learning to perform prompt augmentation at query time. GraphRAG shows substantial improvement in answering the two classes of questions described above, demonstrating intelligence or mastery that outperforms other approaches previously applied to private datasets.


![](https://miro.medium.com/v2/resize:fit:700/0*CFrSdpijjpq7HD3h.png)
_The GraphRAG Pipeline (Image Source:_ [_GraphRAG Paper_](https://arxiv.org/pdf/2404.16130)_)_

# Pipeline
1. [Indexing](Indexing)
2. [Querying](Querying)