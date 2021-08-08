############------------ IMPORTS ------------############
from datetime import datetime, timedelta
import time

############------------ FUNCTION(S) ------------############
def print_task(seconds):
    print("Starting task")

    for second in range(seconds):
        print(second, ". Hello World!")
        time.sleep(1)

    print("Task completed")


def print_numbers(seconds):
    pass

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    print_task()