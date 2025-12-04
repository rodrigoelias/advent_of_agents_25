# advent_of_agents_25
https://adventofagents.com/

issues:
Skyscanner's artifactory - couldn't login on it so I forced the pip index to ignore it with the --index command

## Day 3 

Steps
uv init
uv add google-adk --index https://pypi.org/simple
uv add google-genai --index https://pypi.org/simple
export GOOGLE_API_KEY="YOUR_API_KEY" (from https://aistudio.google.com/api-keys)
source .venv/bin/activate
adk create my_agent

Google Search Tool:
https://google.github.io/adk-docs/tools/built-in-tools/#google-search
https://google.github.io/adk-docs/tools/built-in-tools/#python

Final Source: 
https://raw.githubusercontent.com/GoogleCloudPlatform/devrel-demos/refs/heads/main/ai-ml/agent-labs/gemini-3-pro-agent-demo/my_agent/agent.py

adk web --port 8000
