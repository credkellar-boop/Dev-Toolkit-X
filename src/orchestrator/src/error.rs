#[derive(Debug)]
pub enum OrchestrationError {
    GatewayTimeout,
    AgentPanic,
    SecurityViolation,
    SerializationError,
}

impl std::fmt::Display for OrchestrationError {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "Orchestration Error: {:?}", self)
    }
}
