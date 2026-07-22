crew = Crew(agents=[researcher, writer],
            tasks=[research_task, writing_task],
            process=Process.sequential)              # researcher (with tools) -> writer
brief = crew.kickoff(inputs={"topic": "the state of agentic AI in 2026"})
print(brief)
