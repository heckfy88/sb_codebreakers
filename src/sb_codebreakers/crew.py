from crewai import Agent, Crew, Process, LLM, Task
from crewai.project import CrewBase, agent, crew, task

from src.sb_codebreakers.tools.git_search_tool import my_git_loader_tool


@CrewBase
class SbCodebreakersCrew:
    """Cb crew"""

    @agent
    def retrieval_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['retrieval_agent'],
            tools=[my_git_loader_tool],
            verbose=True,
            llm=LLM(
                model="litellm_proxy/gigachat-custom-model",
                base_url="http://localhost:4000",
                # не нужно, но вдруг придется указывать разные ключи для каждого агента?
                api_key="<API_KEY>"
            ),
            task=self.retrieve_task
        )

    @agent
    def fixing_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['fixing_agent'],
            verbose=True,
            llm=LLM(
                model="litellm_proxy/gigachat-custom-model",
                base_url="http://localhost:4000",
                api_key="<API_KEY>"
            ),
            task=self.fix_task
        )

    @task
    def retrieve_task(self) -> Task:
        return Task(
            config=self.tasks_config['retrieve_task'],
            human_input=True,
        )

    @task
    def fix_task(self) -> Task:
        return Task(
            config=self.tasks_config['fix_task'],
            human_input=True,
            output_file="diff.txt"
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # желательно бы настроить, но у меня он пытается обратиться к OpenAI все равно
            #planning=True,
            #planning_llm
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
