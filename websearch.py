from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()
web_agent = Agent(
    name="Trading Assistant",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=["Always Provide the Links"],
    show_tool_calls=True,
    markdown=True,
)
web_agent.print_response("Please suggest me top 10 Stocks to invest in 2025 in Tech?", stream=True)