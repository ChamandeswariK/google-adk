# Google ADK Course

Example agents built with Google's [Agent Development Kit (ADK)](https://google.github.io/adk-docs/). Each folder is a standalone agent, starting with a single built-in tool and building up to a multi-tool agent backed by a database.

All agents use the `gemini-3.5-flash` model.

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
