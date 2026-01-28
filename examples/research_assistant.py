"""
Research Assistant Example

This example demonstrates a complex multi-step agent that:
- Conducts research on topics
- Maintains conversation history
- Uses structured output for reports
- Handles long-running operations with streaming
- Manages token limits with summarization

Combines exercises:
- 01: Model initialization
- 02: Messages and conversation management
- 03: Tool definition
- 04: Agent creation
- 05: Tool execution
- 07: Structured output
- 08: System prompts and chain-of-thought
- 09: Streaming responses
- 10: Memory and state management
- 11: Middleware (logging, caching)
"""

from typing import Optional
from dataclasses import dataclass, field
from datetime import datetime
from langchain_core.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage, BaseMessage
from pydantic import BaseModel, Field


# Define structured outputs
class ResearchFinding(BaseModel):
    """A single research finding"""
    topic: str = Field(description="What this finding is about")
    finding: str = Field(description="The research finding")
    source_type: str = Field(description="Type of source (article, paper, etc)")
    confidence: float = Field(description="Confidence level 0-1", ge=0, le=1)


class ResearchReport(BaseModel):
    """Complete research report"""
    topic: str = Field(description="Main research topic")
    summary: str = Field(description="Executive summary")
    findings: list[ResearchFinding] = Field(description="List of findings")
    next_questions: list[str] = Field(description="Questions for further research")
    timestamp: str = Field(description="When report was generated")


@dataclass
class ResearchMemory:
    """Track research progress and findings"""
    topic: str
    findings: list[ResearchFinding] = field(default_factory=list)
    conversation_history: list[BaseMessage] = field(default_factory=list)
    context_window: int = 100000  # Tokens available
    used_tokens: int = 0
    
    def add_finding(self, finding: ResearchFinding):
        """Add a finding to research"""
        self.findings.append(finding)
    
    def add_message(self, message: BaseMessage):
        """Add message to conversation history"""
        self.conversation_history.append(message)
    
    def get_context(self) -> list[BaseMessage]:
        """Get conversation history for context"""
        return self.conversation_history
    
    def summarize_if_needed(self) -> Optional[str]:
        """Summarize findings if reaching token limit"""
        tokens_remaining = self.context_window - self.used_tokens
        if tokens_remaining < 20000:  # Less than 20% remaining
            # TODO: Implement summarization
            # Should create concise summary of findings
            pass
        return None


# Mock tools for research
@tool
def search_academic_papers(query: str, num_results: int = 5) -> list[dict]:
    """Search for academic papers on a topic.
    
    Args:
        query: Research query
        num_results: Number of results to return
        
    Returns:
        List of paper summaries
    """
    # Mock data
    papers = {
        "machine learning": [
            {"title": "Deep Learning Review", "abstract": "Comprehensive review...", "citations": 1000},
            {"title": "Neural Networks Basics", "abstract": "Introduction to...", "citations": 500},
        ],
        "climate change": [
            {"title": "Carbon Cycle Analysis", "abstract": "Study of...", "citations": 800},
            {"title": "Temperature Trends", "abstract": "Historical data...", "citations": 600},
        ],
    }
    
    query_lower = query.lower()
    results = papers.get(query_lower, [])
    return results[:num_results]


@tool
def search_news(topic: str, days_back: int = 7) -> list[dict]:
    """Search recent news articles.
    
    Args:
        topic: Topic to search
        days_back: How many days of news to search
        
    Returns:
        List of news articles
    """
    # Mock data
    articles = {
        "artificial intelligence": [
            {"title": "AI Breakthrough", "date": "2024-01-15", "source": "Tech News"},
            {"title": "AI Safety Concerns", "date": "2024-01-14", "source": "Science Daily"},
        ],
        "renewable energy": [
            {"title": "Solar Capacity Grows", "date": "2024-01-15", "source": "Energy Weekly"},
            {"title": "Wind Farm Records", "date": "2024-01-13", "source": "Green Tech"},
        ],
    }
    
    topic_lower = topic.lower()
    results = articles.get(topic_lower, [])
    return results


@tool
def synthesize_information(topic: str, findings: list[str]) -> dict:
    """Synthesize multiple findings into insights.
    
    Args:
        topic: Research topic
        findings: List of findings to synthesize
        
    Returns:
        Synthesized insights
    """
    # TODO: Implement synthesis
    # Should:
    # 1. Analyze connections between findings
    # 2. Identify patterns
    # 3. Generate new insights
    pass


def create_research_memory(topic: str) -> ResearchMemory:
    """Initialize research memory for a topic.
    
    Args:
        topic: Research topic
        
    Returns:
        Initialized memory object
    """
    return ResearchMemory(topic=topic)


def conduct_research(
    topic: str,
    depth: str = "comprehensive",
    save_report: bool = True
) -> ResearchReport:
    """Conduct full research on a topic.
    
    Args:
        topic: What to research
        depth: "quick", "standard", or "comprehensive"
        save_report: Whether to save report to file
        
    Returns:
        Complete research report
    """
    # TODO: Implement research process
    # Should:
    # 1. Initialize ResearchMemory
    # 2. Create system prompt for research expert
    # 3. Use tools to gather information
    # 4. Manage conversation history
    # 5. Generate structured ResearchReport
    # 6. Optionally save to file
    pass


def add_follow_up_research(
    memory: ResearchMemory,
    follow_up_questions: list[str]
) -> ResearchReport:
    """Add follow-up research to existing findings.
    
    Args:
        memory: Existing research memory
        follow_up_questions: Additional questions
        
    Returns:
        Updated research report
    """
    # TODO: Implement follow-up research
    # Should:
    # 1. Use existing memory context
    # 2. Add new questions to research
    # 3. Maintain conversation history
    # 4. Update findings
    # 5. Return updated report
    pass


def export_research_report(report: ResearchReport, format: str = "markdown") -> str:
    """Export research report in specified format.
    
    Args:
        report: Research report to export
        format: "markdown", "json", or "pdf"
        
    Returns:
        Formatted report content
    """
    if format == "json":
        return report.model_dump_json(indent=2)
    elif format == "markdown":
        # TODO: Implement markdown formatting
        pass
    elif format == "pdf":
        # TODO: Implement PDF export
        pass
    
    raise ValueError(f"Unsupported format: {format}")


# Example usage
if __name__ == "__main__":
    # Initialize research
    topic = "artificial intelligence"
    memory = create_research_memory(topic)
    
    # Conduct research
    report = conduct_research(
        topic,
        depth="comprehensive",
        save_report=True
    )
    
    # Display results
    print(f"Research Report: {report.topic}")
    print("=" * 60)
    print(f"Summary:\n{report.summary}\n")
    print(f"Findings ({len(report.findings)}):")
    for finding in report.findings:
        print(f"  - {finding.topic}: {finding.finding}")
    
    print(f"\nFurther Questions:")
    for q in report.next_questions:
        print(f"  - {q}")
    
    # Follow up on specific questions
    follow_up = ["What are the safety implications?", "How is it regulated?"]
    updated_report = add_follow_up_research(memory, follow_up)
    
    # Export
    json_export = export_research_report(updated_report, format="json")
    print(f"\nJSON Export:\n{json_export}")
