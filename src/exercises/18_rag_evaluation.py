"""
Exercise 18: RAG Evaluation and Optimization
=============================================

LEVEL: Advanced (RAG-focused)

GOAL: Measure RAG quality and systematically improve your system.
      "What gets measured gets improved."

TODO:
1. Implement evaluate_retrieval() for retrieval quality metrics
2. Implement evaluate_generation() for answer quality metrics
3. Implement evaluate_rag_pipeline() for end-to-end evaluation
4. Implement create_evaluation_dataset() for benchmark creation
5. Implement run_ab_test() for comparing configurations
6. Implement analyze_failures() for systematic debugging

CONCEPTS TO LEARN:
- Retrieval metrics (MRR, NDCG, Recall@k, Precision@k)
- Generation metrics (faithfulness, relevance, answer correctness)
- End-to-end RAG evaluation with RAGAS
- Building evaluation datasets
- A/B testing for RAG configurations
- Failure analysis and debugging

RESOURCES:
- RAGAS docs: https://docs.ragas.io/
- LangSmith evaluation: https://docs.smith.langchain.com/
- Related exercises: 16_retrieval_chains, 17_advanced_rag

HINTS:
- Good evaluation requires good test data
- Separate retrieval and generation evaluation
- Automated metrics are a starting point, not the end
- Real user feedback is the ultimate metric
"""

from typing import Any, Callable, Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum


@dataclass
class Document:
    """Document with content and metadata."""
    page_content: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class EvaluationSample:
    """A single evaluation example."""
    question: str
    ground_truth_answer: Optional[str] = None
    ground_truth_contexts: Optional[List[str]] = None
    retrieved_contexts: Optional[List[str]] = None
    generated_answer: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class EvaluationResult:
    """Results from an evaluation run."""
    metrics: Dict[str, float]
    sample_results: List[Dict[str, Any]]
    summary: str
    recommendations: List[str] = field(default_factory=list)


class RetrievalMetric(Enum):
    """Available retrieval metrics."""
    PRECISION_AT_K = "precision@k"
    RECALL_AT_K = "recall@k"
    MRR = "mrr"  # Mean Reciprocal Rank
    NDCG = "ndcg"  # Normalized Discounted Cumulative Gain
    HIT_RATE = "hit_rate"


class GenerationMetric(Enum):
    """Available generation metrics."""
    FAITHFULNESS = "faithfulness"
    ANSWER_RELEVANCE = "answer_relevance"
    CONTEXT_RELEVANCE = "context_relevance"
    ANSWER_CORRECTNESS = "answer_correctness"


def evaluate_retrieval(
    samples: List[EvaluationSample],
    metrics: List[RetrievalMetric],
    k: int = 5
) -> Dict[str, float]:
    """
    TODO: Evaluate retrieval quality.
    
    Requirements:
    - Calculate each requested metric
    - Handle missing ground truth gracefully
    - Return aggregate scores
    
    Args:
        samples: Evaluation samples with retrieved contexts
        metrics: Which metrics to calculate
        k: k value for @k metrics
        
    Returns:
        Dictionary of metric name to score
        
    Example:
        >>> results = evaluate_retrieval(samples, [RetrievalMetric.RECALL_AT_K], k=5)
        >>> print(results)
        {"recall@5": 0.78}
    """
    pass


def precision_at_k(
    retrieved: List[str],
    relevant: List[str],
    k: int
) -> float:
    """
    TODO: Calculate precision at k.
    
    Precision@k = (relevant docs in top k) / k
    
    Args:
        retrieved: List of retrieved document IDs/contents
        relevant: List of relevant document IDs/contents
        k: Number of top results to consider
        
    Returns:
        Precision score (0-1)
    """
    pass


def recall_at_k(
    retrieved: List[str],
    relevant: List[str],
    k: int
) -> float:
    """
    TODO: Calculate recall at k.
    
    Recall@k = (relevant docs in top k) / (total relevant docs)
    
    Args:
        retrieved: List of retrieved document IDs/contents
        relevant: List of relevant document IDs/contents
        k: Number of top results to consider
        
    Returns:
        Recall score (0-1)
    """
    pass


def mean_reciprocal_rank(
    samples: List[EvaluationSample]
) -> float:
    """
    TODO: Calculate Mean Reciprocal Rank.
    
    MRR = (1/|Q|) * sum(1/rank_i) where rank_i is position of first relevant doc
    
    Args:
        samples: Evaluation samples
        
    Returns:
        MRR score (0-1)
    """
    pass


def ndcg_at_k(
    retrieved: List[str],
    relevance_scores: List[float],
    k: int
) -> float:
    """
    TODO: Calculate Normalized Discounted Cumulative Gain at k.
    
    NDCG rewards relevant documents appearing earlier in results.
    
    Args:
        retrieved: Retrieved document IDs
        relevance_scores: Relevance score for each retrieved doc
        k: Number of results to consider
        
    Returns:
        NDCG score (0-1)
    """
    pass


def evaluate_generation(
    samples: List[EvaluationSample],
    metrics: List[GenerationMetric],
    llm: Any = None
) -> Dict[str, float]:
    """
    TODO: Evaluate generation quality.
    
    Requirements:
    - Calculate each requested metric
    - Use LLM for subjective metrics if provided
    - Handle missing ground truth
    
    Args:
        samples: Evaluation samples with generated answers
        metrics: Which metrics to calculate
        llm: Language model for LLM-as-judge metrics
        
    Returns:
        Dictionary of metric name to score
    """
    pass


def evaluate_faithfulness(
    answer: str,
    contexts: List[str],
    llm: Any
) -> float:
    """
    TODO: Check if answer is faithful to the provided contexts.
    
    Faithfulness = Can all claims in answer be verified by context?
    
    Requirements:
    - Extract claims from answer
    - Check each claim against contexts
    - Return ratio of supported claims
    
    Args:
        answer: Generated answer
        contexts: Retrieved contexts used
        llm: Language model for evaluation
        
    Returns:
        Faithfulness score (0-1)
    """
    pass


def evaluate_answer_relevance(
    question: str,
    answer: str,
    llm: Any
) -> float:
    """
    TODO: Check if answer is relevant to the question.
    
    Requirements:
    - Use LLM to assess if answer addresses the question
    - Consider completeness and focus
    
    Args:
        question: Original question
        answer: Generated answer
        llm: Language model for evaluation
        
    Returns:
        Relevance score (0-1)
    """
    pass


def evaluate_context_relevance(
    question: str,
    contexts: List[str],
    llm: Any
) -> float:
    """
    TODO: Check if retrieved contexts are relevant to question.
    
    Requirements:
    - Assess each context for relevance
    - Return average relevance score
    
    Args:
        question: User question
        contexts: Retrieved contexts
        llm: Language model for evaluation
        
    Returns:
        Context relevance score (0-1)
    """
    pass


def evaluate_rag_pipeline(
    pipeline: Any,
    test_dataset: List[EvaluationSample],
    retrieval_metrics: List[RetrievalMetric] = None,
    generation_metrics: List[GenerationMetric] = None,
    llm: Any = None
) -> EvaluationResult:
    """
    TODO: Run end-to-end RAG evaluation.
    
    Requirements:
    - Run each sample through the pipeline
    - Collect retrieval and generation results
    - Calculate all metrics
    - Generate summary and recommendations
    
    Args:
        pipeline: RAG pipeline to evaluate
        test_dataset: Evaluation samples
        retrieval_metrics: Retrieval metrics to calculate
        generation_metrics: Generation metrics to calculate
        llm: LLM for generation metrics
        
    Returns:
        Complete evaluation results
    """
    pass


def create_evaluation_dataset(
    documents: List[Document],
    llm: Any,
    num_samples: int = 50,
    difficulty_distribution: Dict[str, float] = None
) -> List[EvaluationSample]:
    """
    TODO: Generate evaluation dataset from documents.
    
    Requirements:
    - Generate diverse questions from documents
    - Include ground truth answers
    - Mark relevant contexts
    - Balance difficulty levels
    
    Args:
        documents: Source documents
        llm: LLM for question generation
        num_samples: Number of samples to generate
        difficulty_distribution: {"easy": 0.3, "medium": 0.5, "hard": 0.2}
        
    Returns:
        List of evaluation samples
    """
    pass


def generate_question_answer_pairs(
    document: Document,
    llm: Any,
    num_pairs: int = 3
) -> List[Dict[str, str]]:
    """
    TODO: Generate question-answer pairs from a document.
    
    Requirements:
    - Generate factoid questions
    - Generate reasoning questions
    - Include ground truth answers
    
    Args:
        document: Source document
        llm: Language model
        num_pairs: Number of pairs to generate
        
    Returns:
        List of {question, answer, context} dicts
    """
    pass


def run_ab_test(
    pipeline_a: Any,
    pipeline_b: Any,
    test_dataset: List[EvaluationSample],
    metrics: List[str],
    confidence_level: float = 0.95
) -> Dict[str, Any]:
    """
    TODO: Run A/B test between two RAG configurations.
    
    Requirements:
    - Run both pipelines on same dataset
    - Calculate metrics for each
    - Perform statistical significance test
    - Determine winner
    
    Args:
        pipeline_a: First pipeline configuration
        pipeline_b: Second pipeline configuration
        test_dataset: Evaluation dataset
        metrics: Metrics to compare
        confidence_level: Required confidence for winner
        
    Returns:
        A/B test results with winner and statistics
        
    Example:
        >>> results = run_ab_test(pipeline_v1, pipeline_v2, dataset, ["recall@5"])
        >>> print(results)
        {
            "winner": "pipeline_b",
            "metrics": {"pipeline_a": {...}, "pipeline_b": {...}},
            "p_value": 0.03,
            "significant": True
        }
    """
    pass


def analyze_failures(
    samples: List[EvaluationSample],
    results: EvaluationResult,
    failure_threshold: float = 0.5
) -> Dict[str, Any]:
    """
    TODO: Analyze failure cases to identify patterns.
    
    Requirements:
    - Identify low-scoring samples
    - Categorize failure modes
    - Suggest improvements
    
    Args:
        samples: Evaluation samples
        results: Evaluation results
        failure_threshold: Score below which is considered failure
        
    Returns:
        Failure analysis with categories and suggestions
        
    Example:
        >>> analysis = analyze_failures(samples, results)
        >>> print(analysis)
        {
            "failure_count": 15,
            "categories": {
                "retrieval_miss": 8,
                "unfaithful_generation": 4,
                "incomplete_answer": 3
            },
            "suggestions": [
                "Consider adding hybrid search for 'retrieval_miss' cases",
                "Add faithfulness check middleware"
            ]
        }
    """
    pass


def calculate_latency_metrics(
    pipeline: Any,
    samples: List[EvaluationSample],
    warmup_runs: int = 3
) -> Dict[str, float]:
    """
    TODO: Measure pipeline latency statistics.
    
    Requirements:
    - Measure retrieval latency
    - Measure generation latency
    - Calculate percentiles (p50, p95, p99)
    
    Args:
        pipeline: RAG pipeline to measure
        samples: Test samples
        warmup_runs: Number of warmup runs before measuring
        
    Returns:
        Latency statistics in milliseconds
    """
    pass


def create_evaluation_report(
    results: EvaluationResult,
    include_samples: bool = True,
    format: str = "markdown"
) -> str:
    """
    TODO: Generate human-readable evaluation report.
    
    Requirements:
    - Summary of all metrics
    - Comparison to baselines
    - Sample of good and bad cases
    - Recommendations
    
    Args:
        results: Evaluation results
        include_samples: Whether to include sample outputs
        format: Output format (markdown, html, json)
        
    Returns:
        Formatted evaluation report
    """
    pass


def continuous_evaluation_monitor(
    pipeline: Any,
    sample_rate: float = 0.1,
    alert_thresholds: Dict[str, float] = None
) -> Callable:
    """
    TODO: Create a monitor for production RAG systems.
    
    Requirements:
    - Sample percentage of production queries
    - Calculate ongoing metrics
    - Alert when metrics drop below threshold
    
    Args:
        pipeline: RAG pipeline to monitor
        sample_rate: Fraction of queries to evaluate
        alert_thresholds: Metric thresholds for alerts
        
    Returns:
        Monitoring function to wrap pipeline
    """
    pass
