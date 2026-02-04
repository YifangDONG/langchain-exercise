# Exercise 18: RAG Evaluation - CONNECTIONS

## Before You Start (5 minutes)

### What Do You Already Know?

Take a moment to reflect on these questions:

1. **Have you ever measured the quality of a system?**
   - Like checking test scores or user satisfaction.

2. **Do you know about A/B testing?**
   - Comparing two versions to see which is better.

3. **Have you debugged by analyzing patterns in failures?**
   - Finding what's common among things that went wrong.

### Real-World Analogy

Think of RAG Evaluation like **Quality Control in Manufacturing**:

```
┌─────────────────────────────────────────────────────────────┐
│            THE QUALITY CONTROL ANALOGY                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Without QC (Flying Blind):                                  │
│  "Our RAG system seems okay... I think?"                    │
│  → No data on actual performance                             │
│  → Problems discovered by angry users                        │
│                                                              │
│  With QC (RAG Evaluation):                                   │
│                                                              │
│  📏 MEASUREMENT (Metrics):                                   │
│     "Retrieval finds correct doc 78% of the time"           │
│     "Answers are faithful to context 92% of time"           │
│                                                              │
│  🔬 TESTING (Evaluation Dataset):                            │
│     Run 500 test questions before each release              │
│     Compare against known correct answers                    │
│                                                              │
│  📊 COMPARISON (A/B Testing):                                │
│     "Config A has 72% accuracy, Config B has 78%"           │
│     "Config B is statistically better (p<0.05)"             │
│                                                              │
│  🔍 FAILURE ANALYSIS:                                        │
│     "80% of failures are retrieval misses"                  │
│     "Recommendation: Add hybrid search"                      │
│                                                              │
│  Result: Data-driven improvements, not guessing!            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### What Gets Measured

```
RAG EVALUATION COMPONENTS:

┌─────────────────────────────────────────────────────────────┐
│  RETRIEVAL EVALUATION                                        │
│  "Did we find the right documents?"                          │
│                                                              │
│  • Recall@k: Did we find the relevant docs in top k?        │
│  • Precision@k: Of top k, how many are relevant?            │
│  • MRR: How high is the first relevant doc ranked?          │
│  • NDCG: Are relevant docs ranked properly?                 │
├─────────────────────────────────────────────────────────────┤
│  GENERATION EVALUATION                                       │
│  "Did we produce a good answer?"                             │
│                                                              │
│  • Faithfulness: Is answer grounded in context?             │
│  • Answer Relevance: Does it address the question?          │
│  • Context Relevance: Was retrieved context useful?         │
│  • Correctness: Is the answer actually correct?             │
├─────────────────────────────────────────────────────────────┤
│  END-TO-END EVALUATION                                       │
│  "How good is the whole system?"                             │
│                                                              │
│  • Accuracy: Correct answers / Total questions              │
│  • Latency: How fast is the response?                       │
│  • User Satisfaction: Do users like the answers?            │
└─────────────────────────────────────────────────────────────┘
```

### Prerequisite Checklist

Before starting this exercise, make sure you:

- [ ] Completed Exercises 13-17 (Full RAG stack)
- [ ] Built at least one RAG pipeline
- [ ] Understand basic statistics (mean, p-values)
- [ ] Have seen evaluation concepts in ML

### Connect to Your Goal

**Building the Best RAG System**: You can't improve what you don't measure.

```
The Improvement Cycle:

    ┌──────────────┐
    │   MEASURE    │ ◄─── RAG Evaluation
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │   ANALYZE    │ ◄─── Failure Analysis
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │   IMPROVE    │ ◄─── Apply techniques from Ex 17
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │   VALIDATE   │ ◄─── A/B Testing
    └──────┬───────┘
           │
           └───────────► Repeat!

This is how you build "the best" RAG system!
```

### Warm-Up Activity

Before coding, think about evaluation:

1. **What questions would you use to test a customer support RAG?**
   - _____________________
   - _____________________
   - _____________________

2. **How would you know if an answer is "faithful" to the context?**
   - _____________________

3. **What would you do if retrieval recall is low?**
   - _____________________

---

**Ready?** Now proceed to `18_rag_evaluation.py` and implement the functions!
