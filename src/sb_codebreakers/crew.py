import os

from crewai import Agent, Crew, Process, LLM, Task
from crewai.project import CrewBase, agent, crew, task

llm_base_url = os.environ['LLM_BASE_URL']


@CrewBase
class SbCodebreakersCrew:
    """Cb crew"""

    @agent
    def fixing_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['fixing_agent'],
            verbose=True,
            llm=LLM(
                model="litellm_proxy/gigachat-custom-model",
                base_url=llm_base_url,
                api_key="<API_KEY>"
            ),
            task=self.fix_task
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
            # planning=True,
            # planning_llm
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
