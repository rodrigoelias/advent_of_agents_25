# advent_of_agents_25
https://adventofagents.com/



## Day 4

 It isn’t clear in the instructions that you must pre-configure a GCP account.

More issues with my local machine (reinstalled gcloud-cli)

Had to:
brew install --cask gcloud-cli
gcloud init
received an error that something was wrong with my user
gcloud auth login
gcloud init (again!)
Another issue with my project quota (??) when enabling Vertex AI
gcloud auth application-default login instead of gcloud auth login(ty Stackoverflow)
gcloud auth application-default set-quota-project PROJECT_ID (from https://aistudio.google.com/api-keys)

Deployment failed because I had to setup a “billing account”. This is odd/bad. 
There wasn’t an option to set my billing country to China tho, this may be an issue for my peers (needs to confirm)

make deploy failed a few times. Tried to recreate the agent from scratch (had initially chosen GitHub Action instead of Google Cloud Build) - failed again with GC Build.

make install && make playground will run it locally for now  

After checking the gcp log: looks like I have to enable “Cloud Resource Manager API” at https://console.cloud.google.com/apis/library/cloudresourcemanager.googleapis.com?project=PROJECT_ID.

 It’s alive!  

Note (limitation?): the same ADK agent can’t call 2 tools at once, when one of them is “search”.



## Day 3 
issues:
company's artifactory - couldn't login on it so I forced the pip index to ignore it with the --index command


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


