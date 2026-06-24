#!/usr/bin/env bash
set -e

echo "⚡ Booting Dev-Toolkit-X Installer..."
echo "Checking dependencies..."

if ! command -v docker &> /dev/null; then
    echo "❌ Docker is required but not installed. Aborting."
    exit 1
fi

echo "📦 Cloning repository and pulling optimized images..."
git clone https://github.com/YOUR_USERNAME/Dev-Toolkit-X.git ~/.dev-toolkit-x
cd ~/.dev-toolkit-x

echo "🔑 Setting up local environment. Edit .env to add your API keys."
cp .env.example .env

echo "🚀 Starting multi-agent orchestrator and MCP server..."
docker-compose up -d

echo "✅ Dev-Toolkit-X is live. Dashboard: http://localhost:8080"
