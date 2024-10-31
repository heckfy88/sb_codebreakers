from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task


from src.sb_codebreakers.tools.git_search_tool import my_git_loader_tool

# Uncomment the following line to use an example of a custom tool
# from cb.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

repo_path = "/Users/ruslanagaev/uni/codebreaker"


@CrewBase
class SbCodebreakersCrew:
	"""Cb crew"""

	@agent
	def retrieval_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['retrieval_agent'],
			tools = [my_git_loader_tool],
			verbose=True,
			llm=LLM(model="ollama/llama3.1", base_url="http://localhost:11434"),
			task=self.retrieve_task
		)

	@task
	def retrieve_task(self) -> Task:
		return Task(
			config=self.tasks_config['retrieve_task'],
			human_input=True,
		)

	@agent
	def counting_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['counting_agent'],
			verbose=True,
			llm=LLM(model="ollama/llama3.1", base_url="http://localhost:11434"),
			task=self.counting_task
		)

	@task
	def counting_task(self) -> Task:
		return Task(
			config=self.tasks_config['counting_task'],
			human_input=True,
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Cb crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)