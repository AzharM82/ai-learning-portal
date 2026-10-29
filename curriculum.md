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

## AI engineering — round 2
- [ ] Model Context Protocol (MCP): servers, tools, resources, and transports
- [ ] Coding agents in practice: Copilot agent mode, task decomposition, repo-scale changes
- [ ] Spec-driven development: specs as the source of truth for AI-built features
- [ ] Agent frameworks compared: LangGraph, Semantic Kernel, and the Microsoft Agent Framework
- [ ] Browser and computer-use agents: perception, grounding, and safe action
- [ ] Multimodal models: vision, audio, and document understanding in products
- [ ] Long-context engineering: million-token windows, lost-in-the-middle, and compaction
- [ ] LoRA and PEFT in practice: fine-tuning a small model hands-on
- [ ] Preference tuning: RLHF, DPO, and teaching models what "good" means
- [ ] Voice and realtime agents: streaming speech, turn-taking, and latency budgets
- [ ] Document intelligence pipelines: OCR, layout, and extraction at scale
- [ ] AI feedback loops: production signals, drift, and continuous improvement

## The trio's adjacents — round 2 (loop / graph / harness)
- [ ] MCP gateways and tool registries: governing hundreds of tools
- [ ] Graph-based agent control: LangGraph-style state graphs in production
- [ ] Regression harnesses for prompts: golden sets wired into CI

## Software engineering — round 2
- [ ] Kubernetes from zero: pods, services, and why orchestration exists
- [ ] Reliability engineering: SLOs, error budgets, and incident response
- [ ] Event-driven architecture: event sourcing and CQRS without the hype
- [ ] Distributed systems failure modes: partitions, clocks, and consensus basics
- [ ] Database scaling: replication, sharding, and consistency trade-offs
- [ ] Auth in practice: OAuth 2.0, OIDC, and session design for builders
- [ ] Performance profiling and load testing: finding the real bottleneck
- [ ] Feature flags and progressive delivery: shipping without the big bang
