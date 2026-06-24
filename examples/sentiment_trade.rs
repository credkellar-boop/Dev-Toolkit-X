use dev_toolkit_orchestrator::{ParallelAgent, GatewayClient, TraceLogger};

#[tokio::main]
async fn main() {
    // 1. Initialize specialized agents
    let sentiment_agent = ParallelAgent::new("Sentiment-Analyst");
    let execution_agent = ParallelAgent::new("Execution-Bot");
    let gateway = GatewayClient::new();

    // 2. Fetch context and route via AI Gateway
    let market_data = "BTC price volatility spike detected";
    let analysis = gateway.route(market_data, "sentiment").await;

    // 3. Execution logic
    if analysis.contains("bullish") {
        let trace = execution_agent.execute_trade("BUY", 1.0).await;
        
        // 4. Log the immutable trace
        TraceLogger::log(trace);
    }
}
