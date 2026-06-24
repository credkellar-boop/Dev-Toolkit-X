# Contributing to Dev-Toolkit-X

We love contributions! Whether it's adding a new AI provider to the gateway, optimizing the Rust orchestrator, or improving our defensive scanners, your input makes Dev-Toolkit-X better.

## 🚀 How to Contribute
1. **Fork the Repo:** Create your own branch from `main`.
2. **Issue Tracking:** Please check the [Issues](https://github.com/YOUR_USERNAME/Dev-Toolkit-X/issues) to see if your bug or feature request is already being tracked.
3. **Commit Standards:** Keep commit messages descriptive (e.g., `feat: add Anthropic Claude 3.5 support to gateway`).
4. **Pull Requests:** All PRs must pass the CI checks (run `go run audit.go` and `cargo build --release` locally).

## 🛠️ The Architecture Stack
* **Orchestrator (Rust):** Keep core logic memory-safe and low-latency.
* **AI Gateway (TypeScript):** Ensure vendor-neutral abstraction layers.
* **Vector Indexer (Python):** Maintain compatibility with FAISS/SentenceTransformers.
* **Scanner (Go):** Stick to the standard library to maintain zero-dependency security.

## ⚖️ Our Philosophy
* **Performance first:** Every millisecond counts.
* **Security second:** We favor read-only, local-first execution.
* **Transparency:** All agent actions must be traceable via `trace_logger`.
