from fastapi import FastAPI
from llama_hub.tools.arxiv import ArxivToolSpec


tool = ArxivToolSpec()

print(tool.arxiv_query("quantum"))

# agent = OpenAIAgent.from_tools(tool_spec.to_tool_list())

# agent.chat('Whats going on with the superconductor lk-99')
# agent.chat('what are the latest developments in machine learning')

## fastAPI example using llama_hub tool

api = FastAPI()

@api.get("/arxiv/{query}")
def arxiv_query(query: str):
    return tool.arxiv_query(query)


