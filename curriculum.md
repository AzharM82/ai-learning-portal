# Curriculum backlog

The daily publisher takes Azharuddin's queued topics first (`queue.json`). When the
queue is empty, it works through this list top-down, skipping anything already in
`published.json`. Focus: AI engineering, software engineering, and everything around
the loop / graph / harness trio.

## AI engineering
- [ ] Prompt engineering: instructions, few-shot, and output contracts
- [ ] Context engineering: what actually goes into the window
- [ ] RAG architectures: naive, advanced, and when to skip RAG
- [ ] Chunking and embeddings: the unglamorous 80%
- [ ] Vector databases: indexes, ANN search, and trade-offs
- [ ] Re-ranking and query rewriting for retrieval quality
- [ ] Knowledge graphs for RAG (GraphRAG patterns)
- [ ] Tool calling / function calling done right
- [ ] Structured outputs: JSON mode, grammars, and validation
- [ ] Agent memory systems: short-term, long-term, episodic
- [ ] Planning and reasoning: CoT, ReAct, tree-of-thought
- [ ] Multi-agent orchestration and handoffs
- [ ] LLM evals and LLM-as-judge: building trust in outputs
- [ ] Eval-driven development for AI features
- [ ] Fine-tuning vs RAG vs prompting: how to choose
- [ ] Guardrails, safety, and prompt-injection defense
- [ ] Inference optimization: quantization, vLLM, batching
- [ ] Streaming UX for AI products
- [ ] Semantic caching to cut cost and latency
- [ ] Model routing, fallbacks, and cost control
- [ ] Distillation: small models from big ones
- [ ] Synthetic data generation for training and evals
- [ ] Observability for LLM apps: traces, token accounting

## The trio's adjacents (loop / graph / harness)
- [ ] State machines for agents: explicit states beat vibes
- [ ] Workflow orchestration engines (Temporal-style durable execution)
- [ ] Human-in-the-loop patterns: approvals, edits, takeovers
- [ ] Sandboxing and least-privilege tool permissions
- [ ] Agent eval harnesses: tasks, graders, scoring loops
- [ ] Error recovery patterns: retries, compensation, sagas
- [ ] Checkpointing and resumable agent runs

## Software engineering
- [ ] System design fundamentals: thinking in trade-offs
- [ ] API design: contracts that survive contact with clients
- [ ] Testing strategies: the pyramid in practice
- [ ] CI/CD pipelines that developers trust
- [ ] Observability: metrics, logs, traces
- [ ] Database indexing: how queries get fast
- [ ] Caching strategies: layers and invalidation
- [ ] Message queues and async architectures
- [ ] Containerization and reproducible environments
- [ ] Git workflows for teams
- [ ] Code review craft: reviewing like a senior
- [ ] Refactoring without fear
- [ ] Design patterns worth knowing (and ones to skip)
- [ ] Concurrency basics: threads, async, races
- [ ] Security basics: OWASP top 10 for builders
- [ ] Infrastructure as code from zero
