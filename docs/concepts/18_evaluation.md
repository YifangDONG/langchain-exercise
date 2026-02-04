# Concept Guide: RAG Evaluation

## Key Concepts

1. **Measure before optimizing** - Data beats intuition
2. **Evaluate retrieval and generation separately** - Different failure modes
3. **Good test data is essential** - Evaluation quality depends on test quality
4. **Continuous monitoring catches regressions** - Production needs ongoing checks

## Visual: RAG Metrics

```
┌─────────────────────────────────────────────────────────────┐
│                     RAG METRICS OVERVIEW                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   RETRIEVAL METRICS (Did we find the right docs?)           │
│   ┌────────────────────────────────────────────────────┐    │
│   │ Recall@k:     Found relevant / Total relevant      │    │
│   │               "Did we find what exists?"           │    │
│   │                                                    │    │
│   │ Precision@k:  Relevant in top k / k               │    │
│   │               "How much noise in results?"         │    │
│   │                                                    │    │
│   │ MRR:          1/rank of first relevant             │    │
│   │               "How high is the best result?"       │    │
│   │                                                    │    │
│   │ NDCG:         Ranking quality score                │    │
│   │               "Are relevant docs ranked right?"    │    │
│   └────────────────────────────────────────────────────┘    │
│                                                              │
│   GENERATION METRICS (Is the answer good?)                   │
│   ┌────────────────────────────────────────────────────┐    │
│   │ Faithfulness: Answer grounded in context?          │    │
│   │               "Is this a hallucination?"           │    │
│   │                                                    │    │
│   │ Relevance:    Answer addresses the question?       │    │
│   │               "Did we answer what was asked?"      │    │
│   │                                                    │    │
│   │ Correctness:  Answer is factually correct?         │    │
│   │               "Is this actually right?"            │    │
│   └────────────────────────────────────────────────────┘    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Visual: The Evaluation Cycle

```
┌─────────────────────────────────────────────────────────────┐
│                  THE IMPROVEMENT CYCLE                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│         ┌──────────────┐                                    │
│         │   MEASURE    │ ◄─── Run eval on test set         │
│         └──────┬───────┘                                    │
│                │                                             │
│                ▼                                             │
│         ┌──────────────┐                                    │
│         │   ANALYZE    │ ◄─── Find failure patterns        │
│         └──────┬───────┘                                    │
│                │          "80% failures are retrieval"      │
│                ▼                                             │
│         ┌──────────────┐                                    │
│         │   IMPROVE    │ ◄─── Apply fixes                   │
│         └──────┬───────┘      "Add hybrid search"          │
│                │                                             │
│                ▼                                             │
│         ┌──────────────┐                                    │
│         │   VALIDATE   │ ◄─── A/B test changes             │
│         └──────┬───────┘      "Is new config better?"      │
│                │                                             │
│                └────────────────────▶ (Repeat)              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Code Example

```python
# Retrieval metrics
def recall_at_k(retrieved, relevant, k):
    retrieved_set = set(retrieved[:k])
    relevant_set = set(relevant)
    if not relevant_set:
        return 0.0
    return len(retrieved_set & relevant_set) / len(relevant_set)

def precision_at_k(retrieved, relevant, k):
    retrieved_set = set(retrieved[:k])
    relevant_set = set(relevant)
    return len(retrieved_set & relevant_set) / k

def mrr(samples):
    """Mean Reciprocal Rank"""
    rr_sum = 0
    for sample in samples:
        for rank, doc in enumerate(sample.retrieved, 1):
            if doc in sample.relevant:
                rr_sum += 1 / rank
                break
    return rr_sum / len(samples)

# LLM-as-Judge for generation
def evaluate_faithfulness(answer, contexts, llm):
    prompt = f"""Rate if the answer is supported by the context (0-1).
    
Context: {contexts}
Answer: {answer}

Score (just the number):"""
    return float(llm.invoke(prompt).content)

# A/B Testing
from scipy import stats

def ab_test(scores_a, scores_b, alpha=0.05):
    t_stat, p_value = stats.ttest_ind(scores_a, scores_b)
    return {
        "significant": p_value < alpha,
        "p_value": p_value,
        "winner": "A" if np.mean(scores_a) > np.mean(scores_b) else "B"
    }
```

## Metric Selection Guide

```
SYMPTOM                         CHECK THESE METRICS
────────────────────────────────────────────────────
"Answers are wrong"         →   Recall@k, Faithfulness
"Too much irrelevant info"  →   Precision@k, Context Relevance
"Right doc but bad answer"  →   Faithfulness, Answer Relevance
"System is slow"            →   Latency p50, p95, p99
"Users unhappy"             →   User satisfaction surveys
```

## Teach-Back

Explain in your own words:
1. What's the difference between Recall@k and Precision@k?
2. How does LLM-as-Judge work for evaluating faithfulness?
3. When would you need human evaluation vs automated metrics?
