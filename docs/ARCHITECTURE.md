# Architectural Overview
Dev-Toolkit-X operates on a "distributed-brain" model. 
1. The **Orchestrator** (Rust) manages the execution loop.
2. The **Gateway** (TS) offloads reasoning to LLMs.
3. The **Indexer** (Python) provides semantic memory.
4. The **Scanner** (Go) ensures integrity at each step.
