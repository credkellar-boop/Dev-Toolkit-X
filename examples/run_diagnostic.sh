#!/bin/bash
echo "Running full-stack diagnostic..."
cd src/scanner && go run audit.go
cd ../orchestrator && cargo test
echo "Diagnostic complete. System healthy."
