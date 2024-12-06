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

local_repository_path = os.environ["LOCAL_REPOSITORY_PATH"]
branch = os.environ["BRANCH"]

actual_result_file_path = os.environ["ACTUAL_RESULT_FILE_PATH"]
expected_result_file_path = os.environ["EXPECTED_RESULT_FILE_PATH"]

def run():
    actual_result = open(actual_result_file_path, "r").read()
    expected_result = open(expected_result_file_path, "r").read()

    """
    Run the crew.
    """
    inputs = {
        "repo_path": local_repository_path,
        "branch": branch,

        "actual_result": actual_result,
        "expected_result": expected_result
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
