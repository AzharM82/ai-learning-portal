# Curriculum extension — DRAFT for Azharuddin's approval (prepared 2026-10-29)

Status: NOT live. The first curriculum is exhausted — the final item,
"Infrastructure as code from zero," published 2026-10-29, and queue.json is
empty. If approved, append the topics below to curriculum.md (same section
style); the daily publisher (ai-portal-daily-topic, 9:24 AM PT) then picks
them top-down starting with MCP. If not approved, tomorrow's run has nothing
to publish.

Selection logic: no repeats of the 46 published topics. Round 2 goes one
level deeper on the themes Azharuddin follows daily (AI agents, GitHub
Copilot, agentic loops, knowledge graphs, LLMs for coding) and continues the
software-engineering ladder where it left off (containers → IaC → the topics
below).

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

Total: 23 topics ≈ 3+ weeks of daily lessons at the current cadence.
