The indexing process includes four key steps:

1. Text Unit Segmentation: The entire input corpus is divided into multiple text units (text chunks). These chunks are the smallest analyzable units and can be paragraphs, sentences, or other logical units. By segmenting long documents into smaller chunks, we can extract and preserve more detailed information about this input data.
2. Entity, Relationship, and Claims Extraction: GraphRAG uses LLMs to identify and extract all entities (names of people, places, organizations, etc.), relationships between them, and key claims expressed in the text from each text unit. We will use this extracted information to construct an initial knowledge graph.
3. Hierarchical Clustering: GraphRAG uses the [Leiden](https://arxiv.org/pdf/1810.08473) technique to perform hierarchical clustering on the initial knowledge graphs. Leiden is a community detection algorithm that can effectively discover community structures within the graph. Entities in each cluster are assigned to different communities for more in-depth analysis.

_Note:_ _A community is a group of nodes within the graph that are densely connected to each other but sparsely connected to other dense groups in the network._

1. Community Summary Generation: ==GraphRAG generates summaries for each community and its members using a bottom-up approach.== These summaries include the main entities within the community, their relationships, and key claims. This step gives an overview of the entire dataset and provides useful contextual information for subsequent queries.

![](https://miro.medium.com/v2/resize:fit:700/1*ONBAXxbYTd20FmfC7fPM6w.png)

_Figure 1: An LLM-generated knowledge graph built using GPT-4 Turbo._

_(Image Source:_ [_Microsoft Research_](https://microsoft.github.io/graphrag/)_)_