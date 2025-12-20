import re
from datetime import datetime

MAX_RETRIES = 2

# ---------------- PLANNER ----------------
def planner(question: str) -> str:
    return "parse question -> extract values -> compute -> verify -> format answer"


# ---------------- EXECUTOR ----------------
def executor(question: str):
    # Handle time-based questions
    time_pattern = r"(\d{1,2}:\d{2})"
    times = re.findall(time_pattern, question)

    if len(times) == 2:
        start = datetime.strptime(times[0], "%H:%M")
        end = datetime.strptime(times[1], "%H:%M")
        diff = end - start
        minutes = diff.seconds // 60
        return {
            "type": "time",
            "minutes": minutes
        }

    # Handle simple arithmetic questions
    numbers = list(map(int, re.findall(r"\d+", question)))
    if numbers:
        return {
            "type": "math",
            "result": sum(numbers)
        }

    return None


# ---------------- VERIFIER ----------------
def verifier(result):
    checks = []

    if result["type"] == "time":
        passed = result["minutes"] >= 0
        checks.append({
            "check_name": "non_negative_time",
            "passed": passed,
            "details": "Time duration must be positive"
        })
        return passed, checks

    if result["type"] == "math":
        passed = result["result"] >= 0
        checks.append({
            "check_name": "non_negative_result",
            "passed": passed,
            "details": "Result must be non-negative"
        })
        return passed, checks

    return False, []


# ---------------- SOLVER ----------------
def solve(question: str) -> dict:
    retries = 0
    plan = planner(question)

    while retries <= MAX_RETRIES:
        result = executor(question)
        if result is None:
            break

        passed, checks = verifier(result)

        if passed:
            if result["type"] == "time":
                hours = result["minutes"] // 60
                mins = result["minutes"] % 60
                answer = f"{hours} hours {mins} minutes"
            else:
                answer = str(result["result"])

            return {
                "answer": answer,
                "status": "success",
                "reasoning_visible_to_user": "Solved step by step and verified.",
                "metadata": {
                    "plan": plan,
                    "checks": checks,
                    "retries": retries
                }
            }

        retries += 1

    return {
        "answer": "\n",
        "status": "failed \n",
        "reasoning_visible_to_user": "Unable to verify a correct solution. \n",
        "metadata": {
            "plan": plan,
            "checks": [],
            "retries": retries
        }
    }


# ---------------- TEST RUN ----------------
if __name__ == "__main__":
    questions = [
        "If a train leaves at 14:30 and arrives at 18:05,\n how long is the journey?",
        "\n Alice has 3 red apples and 6 green apples.\n How many apples total?",
        "\n Meeting from 09:00 to 10:00"
    ]

    for q in questions:
        print("Question:", q)
        print(solve(q))
        print("-" * 50)
