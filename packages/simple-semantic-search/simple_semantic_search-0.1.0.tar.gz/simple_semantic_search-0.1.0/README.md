# Simple Semantic Search
A lightning fast, no-dependency semantic search library.

A Python package combining keyword efficiency with semantic understanding for improved search relevance.

## Introduction

Keyword search offers speed and precision but lacks context. Semantic search understands intent but can be complex and resource-intensive. Simple Semantic Search bridges this gap, providing a lightweight solution that enhances search relevance without the complexity of full natural language processing.

## Installation

```bash
pip install simple-semantic-search
```

# Quickstart
```python
from simple_semantic_search import SimpleSemanticSearch

products = [
    "Wireless noise-cancelling headphones with Bluetooth",
    "Ergonomic office chair with lumbar support",
    "Stainless steel water bottle, vacuum insulated",
    "Smart LED bulb, color changing, WiFi enabled",
]

searcher = SimpleSemanticSearch(products)
results = searcher.search("cordless headset for work", top_k=3)

for product, score in results:
    print(f"Score: {score:.2f} - {product}")
```

# Benchmark

We compared Simple Semantic Search against several other search methods using a dataset of 100,000 product descriptions. The benchmark measured both accuracy (measured by relevance to human-rated results) and speed (in milliseconds per query).

| Method                      | Accuracy | Speed (ms) |
|-----------------------------|----------|------------|
| Keyword Search              | 70%      | 50         |
| Sentence Transformers       | 92%      | 500        |
| Simple Search (Small Vocab) | 65%      | 3         |
| Simple Search (Large Vocab) | 85%      | 2         |

*Note: Benchmarks were performed on a standard desktop computer (Intel i7, 16GB RAM). Results may vary based on hardware and dataset characteristics.*