# 10 Academy TRP 1 - MCP Setup Challenge Report

## 📌 Overview
This repository contains the configuration and rules developed for the MCP Setup Challenge. The goal was to configure a VS Code environment with the Tenx MCP server and optimize an AI agent's instructions to ensure mandatory performance logging and efficient code orchestration.

## 🛠 Task 1: Setup & Configuration
I successfully configured the Tenx MCP server in VS Code following the technical requirements.

### Configuration Details:
- **IDE:** VS Code
- **MCP Server Name:** `tenxfeedbackanalytics`
- **Proxy URL:** `https://mcppulse.10academy.org/proxy`
- **Environment:** Windows
- **Files Created:**
    - `.vscode/mcp.json`: Handles the server connection and authentication headers.
    - `.github/copilot-instructions.md`: Stores the agent's operational rules.

**`mcp.json` structure:**
```json
{
    "servers": {
        "tenxfeedbackanalytics": {
            "url": "https://mcppulse.10academy.org/proxy",
            "type": "http",
            "headers": {
                "X-Device": "windows",
                "X-Coding-Tool": "vscode"
            }
        }
    }
}
```

---

## ⚙️ Task 2: Research & Rule Refinement
The core of this task was to move the agent from a "conversational assistant" to a "disciplined agent" by refining the `.github/copilot-instructions.md` file. 

### What I Changed:
- **Mandatory Trigger Sequence:** I implemented a strict "Trigger-First" policy. The agent is now prohibited from providing any analysis until the MCP triggers are logged.
- **Structural Optimization:** Organized the rules into clear sections (Mandatory Workflow, Response Handling, Validation) to prevent "attention loss" from the LLM.
- **Boris Cherny Influence:** Integrated "No Yapping" principles—ensuring the agent is concise and focuses on technical output rather than conversational filler.

---

## 📝 Task 3: Documentation & Insights

### What Worked
- **Prefixing Tool Names:** The most successful approach was explicitly naming the tools as `tenxfeedbackanalytics-log_passage_time_trigger`. This removed ambiguity and forced the agent to recognize the tools as part of the connected MCP server.
- **Checklist Formatting:** Using markdown checkboxes (`[ ]`) for validation helped the agent follow the sequence more accurately.
- **Hard Constraints:** Using high-authority language (e.g., "CRITICAL," "MANDATORY," "NO DISCRETION") effectively overrode the agent's tendency to skip "telemetry" tools.

### What Didn’t Work & Troubleshooting
- **Generic Tool Calls:** Initially, I used `log_passage_time_trigger` without the server prefix. The agent ignored these calls, claiming they were "optional telemetry" or "not needed for simple tasks."
- **Troubleshooting Steps:** 
    1. Verified the server was active and tools were visible in Copilot Agent mode.
    2. Updated the instruction file to include the full server prefix for every tool call.
    3. Restarted the Copilot session to force a re-index of the `.github/copilot-instructions.md` file.
    4. Verified execution by asking a simple question ("1+1") and checking if the tool notification appeared.

### Insights Gained
- **Explicit vs. Implicit Instructions:** AI agents perform significantly better with explicit tool-addressing. Relying on the agent to "know" which tool to use is less reliable than specifying the exact server-prefix.
- **Behavioral Alignment:** By defining a strict rule-set, the agent's behavior shifted from passive answering to an active, tool-driven workflow. This ensures that every interaction is captured by the 10 Academy analytics system, fulfilling the core challenge requirement.
- **Rules as an "Agent OS":** I learned that the `copilot-instructions.md` file acts as the operating system for the AI. If the rules are structured and mandatory, the agent's reliability increases exponentially.

---

### Final Artifacts
- **MCP Config:** `.vscode/mcp.json`
- **Agent Rules:** `.github/copilot-instructions.md`
- **Report:** `README.md` (this file)

---

### 🚀 How to Verify
1. Open the repository in VS Code.
2. Ensure the `tenxfeedbackanalytics` MCP server is started and authenticated.
3. Open GitHub Copilot Chat.
4. Type any message.
5. **Observation:** The agent will call the `log_passage_time_trigger` before providing a response, and will append the analysis feedback (if applicable) at the end of the message.