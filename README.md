# Google ADK Course

Example agents built with Google's [Agent Development Kit (ADK)](https://google.github.io/adk-docs/). Each folder is a standalone agent, starting with a single built-in tool and building up to a multi-tool agent backed by a database.

All agents use the `gemini-3.5-flash` model.

## Agents

| Folder | What it shows |
| --- | --- |
| `google_adk_tool` | Web search with ADK's built-in `google_search` tool |
| `code_execution_agent` | Writing and running Python with `BuiltInCodeExecutor` |
| `google_adk_chatbot` | Same setup as `code_execution_agent` |
| `world_clock_agent` | A custom function tool (`get_current_time`) for time in any time zone |
| `tavily_search_agent` | Using a LangChain tool (Tavily search) in ADK through `LangchainTool` |
| `combined_tool_agents` | One agent with a function tool, Google Search, code execution and Tavily together |
| `course_enroll_refund_agent` | A course refund assistant that reads and writes a SQLite database and keeps state between turns |

## Setup

Requires Python 3.11+.

```bash
git clone https://github.com/ChamandeswariK/google-adk.git
cd google-adk

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

### API keys

Each agent folder reads its own `.env` file. These files are not committed, so create one in each agent folder you want to run:

```env
GOOGLE_GENAI_USE_ENTERPRISE=FALSE
GOOGLE_API_KEY=your-gemini-api-key
```

Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey).
