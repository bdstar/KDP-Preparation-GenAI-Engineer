# CrewAI models a team as agents with roles, tasks, and a process.
from crewai import Agent, Task, Crew, Process
 
researcher = Agent(role="Research Analyst",
                   goal="Find and synthesize current information on the topic",
                   backstory="A meticulous investigator who checks sources.",
                   tools=[web_search])
writer = Agent(role="Technical Writer",
               goal="Turn research into a clear, well-structured brief",
               backstory="An experienced writer who values clarity.")
 
research = Task(description="Research the topic: {topic}", agent=researcher,
                expected_output="A bulleted list of key findings with sources.")
write = Task(description="Write a one-page brief from the findings.", agent=writer,
             expected_output="A polished one-page brief.")
 
crew = Crew(agents=[researcher, writer], tasks=[research, write],
            process=Process.sequential)         # or Process.hierarchical with a manager
result = crew.kickoff(inputs={"topic": "retrieval-augmented generation in 2026"})
