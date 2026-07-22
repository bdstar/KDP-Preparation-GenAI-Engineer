from crewai import Agent, Task, Crew, Process
from crewai_tools import TavilySearchTool          # AI-native web search (Section 21.9)
from crewai_tools import MCPServerAdapter           # tools exposed via MCP (Section 21.7)
 
tavily = TavilySearchTool()                          # returns distilled, agent-ready results
mcp_tools = MCPServerAdapter({"url": "http://localhost:8000/mcp"}).tools  # MCP server tools
 
researcher = Agent(
    role="Research Analyst",
    goal="Research {topic} thoroughly using web search and available tools",
    backstory="A meticulous investigator who grounds every claim in a source.",
    tools=[tavily, *mcp_tools])                       # web + MCP tools together
