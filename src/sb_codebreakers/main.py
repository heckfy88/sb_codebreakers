#!/usr/bin/env python
import os
import sys
from sb_codebreakers.crew import SbCodebreakersCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

os.environ["OPENAI_API_KEY"] = "NA"
os.environ["OTEL_SDK_DISABLED"] = "true"

def run():
    """
    Run the crew.
    """
    inputs = {
        "repo_path": "/Users/ruslanagaev/uni/codebreaker",
        "branch": "develop",

        "actual_result": "Current month is: Current month is: This is January",
        "expected_result": "Current month is: January"
    }
    SbCodebreakersCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "repo_path": "/Users/ruslanagaev/uni/codebreaker",
        "branch": "develop",
    }
    try:
        SbCodebreakersCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SbCodebreakersCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "repo_path": "/Users/ruslanagaev/uni/codebreaker",
        "branch": "develop",
    }
    try:
        SbCodebreakersCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
