# Core Concepts

This document is the **index** for concept guides. Each exercise has its own concept file under [docs/concepts/](concepts/) with key concepts, visuals, code examples, and teach-back prompts.

---

## Beginner (Exercises 1–4)

| # | Concept | Summary | Guide |
|---|---------|---------|--------|
| 1 | **Model Basics** | Models as APIs; invoke, stream, batch; temperature and parameters | [01_model_basics.md](concepts/01_model_basics.md) |
| 2 | **Messages** | SystemMessage, HumanMessage, AIMessage, ToolMessage; conversation as message lists | [02_messages.md](concepts/02_messages.md) |
| 3 | **Tool Definition** | Defining tools with docstrings and type hints; schemas for agents | [03_tool_definition.md](concepts/03_tool_definition.md) |
| 4 | **Basic Agents** | ReAct pattern: Reason + Act; agent loop and tool use | [04_basic_agents.md](concepts/04_basic_agents.md) |

---

## Intermediate (Exercises 5–8)

| # | Concept | Summary | Guide |
|---|---------|---------|--------|
| 5 | **Tool Execution** | Running tools safely; error handling and retries | [05_tool_execution.md](concepts/05_tool_execution.md) |
| 6 | **Advanced Tools** | Composed tools; structured I/O; async tools | [06_advanced_tools.md](concepts/06_advanced_tools.md) |
| 7 | **Structured Output** | Pydantic schemas; guaranteed format and validation | [07_structured_output.md](concepts/07_structured_output.md) |
| 8 | **System Prompts** | System prompts, chain of thought, dynamic prompts | [08_system_prompts.md](concepts/08_system_prompts.md) |

---

## Advanced (Exercises 9–12)

| # | Concept | Summary | Guide |
|---|---------|---------|--------|
| 9 | **Streaming** | Token and event streaming; real-time UX | [09_streaming.md](concepts/09_streaming.md) |
| 10 | **Memory & State** | Short-term (history), long-term (storage), checkpoints | [10_memory_state.md](concepts/10_memory_state.md) |
| 11 | **Middleware** | Before/after hooks; logging, validation, caching | [11_middleware.md](concepts/11_middleware.md) |
| 12 | **Advanced Workflows** | Multi-agent; supervisor pattern; message passing | [12_advanced_workflows.md](concepts/12_advanced_workflows.md) |

---

## RAG Deep Dive (Exercises 13–18)

| # | Concept | Summary | Guide |
|---|---------|---------|--------|
| 13 | **Document Loading** | Loaders for PDF, web, CSV; metadata; clean text | [13_document_loading.md](concepts/13_document_loading.md) |
| 14 | **Text Chunking** | Chunk size, overlap, token-aware and semantic chunking | [14_text_chunking.md](concepts/14_text_chunking.md) |
| 15 | **Embeddings & Vector Stores** | Embeddings, similarity search, metadata filtering | [15_embeddings.md](concepts/15_embeddings.md) |
| 16 | **Retrieval Chains** | RAG flow; retrieve, augment, generate; citations | [16_retrieval_chains.md](concepts/16_retrieval_chains.md) |
| 17 | **Advanced RAG** | Reranking, hybrid search, HyDE, query decomposition | [17_advanced_rag.md](concepts/17_advanced_rag.md) |
| 18 | **RAG Evaluation** | Retrieval and generation metrics; test data; monitoring | [18_evaluation.md](concepts/18_evaluation.md) |

---

## Summary Table

| Concept | Purpose | Key insight |
|---------|---------|-------------|
| Models | Generate text | Different invocation modes and parameters |
| Messages | Communicate | Conversations are message lists |
| Tools | External actions | Agents use tools; models can't compute |
| Agents | Autonomous solving | ReAct: Think → Act → Observe |
| Tool Execution | Run tools safely | Handle errors and retries |
| Advanced Tools | Richer tools | Composition, structured I/O, async |
| Structured Output | Reliable parsing | Guarantee format with Pydantic |
| Prompts | Guide behavior | System prompts and chain of thought |
| Streaming | Real-time feedback | Tokens and events as they arrive |
| Memory | Context | Short-term history, long-term storage |
| Middleware | Customize execution | Before/after hooks |
| Multi-Agent | Complex tasks | Supervisor + workers, message passing |
| Document Loading | RAG foundation | Loaders, metadata, clean text |
| Chunking | Retrieval quality | Size, overlap, token/semantic strategies |
| Embeddings | Semantic search | Similar text → similar vectors |
| Retrieval Chains | RAG pipeline | Retrieve → augment → generate |
| Advanced RAG | Better retrieval | Rerank, hybrid, HyDE, decomposition |
| Evaluation | Measure quality | Retrieval + generation metrics |

---

## Resources

- **LangChain Docs**: https://docs.langchain.com
- **ReAct Paper**: https://arxiv.org/abs/2210.03629
- **Prompt Engineering**: https://platform.openai.com/docs/guides/prompt-engineering
- **Pydantic**: https://docs.pydantic.dev
