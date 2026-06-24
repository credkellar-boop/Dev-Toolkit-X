import { GeminiClient, ClaudeClient } from './providers';

interface QueryPayload {
    task: string;
    context: string[];
    priority: 'speed' | 'reasoning';
}

/**
 * Dynamically routes requests to the optimal model based on the workload.
 * Eliminates API lock-in and handles fallback logic natively.
 */
export class UnifiedRouter {
    private gemini: GeminiClient;
    private claude: ClaudeClient;

    constructor() {
        this.gemini = new GeminiClient(process.env.GEMINI_API_KEY);
        this.claude = new ClaudeClient(process.env.CLAUDE_API_KEY);
    }

    async routeQuery(payload: QueryPayload) {
        if (payload.priority === 'speed') {
            // High-throughput requests default to Gemini for rapid context processing
            return await this.gemini.generate(payload.task, payload.context);
        } else {
            // Fallback or complex architectural reasoning
            return await this.claude.generate(payload.task, payload.context);
        }
    }
}
