writer = Agent(
    role="Technical Writer",
    goal="Turn research findings into a clear, well-structured brief",
    backstory="A writer prized for turning complexity into clarity.")
 
research_task = Task(
    description="Research {topic}. Use web search for current facts and MCP tools "
                "for internal data. Cite every finding.",
    agent=researcher,
    expected_output="A bulleted list of findings, each with a source.")
 
writing_task = Task(
    description="Using the findings, write a one-page brief on {topic}.",
    agent=writer,
    expected_output="A polished one-page brief a busy executive could read.")
