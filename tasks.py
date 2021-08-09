############------------ IMPORTS ------------############
from datetime import datetime, timedelta
import time
import random


############------------ FUNCTION(S) ------------############
def print_task(seconds):
    print("Starting task")

    # random_num = random.randrange(1, 3, 1)
    # random_num = 2
    
    # if random_num == 2:
    #     raise RuntimeError('Sorry, I failed! Let me try again.')
    # else:
    #     for second in range(seconds):
    #         print(second + 1, ". Hello World!")
    #         time.sleep(1)

    for second in range(seconds):
            now = datetime.now()

            current_time = now.strftime("%H:%M:%S")
            print("Current Time is", current_time)
            time.sleep(1)

    print("Task completed")


def print_numbers(seconds):
    print("Starting num task")

    for second in range(seconds):
        print(second + 1)
        time.sleep(1)

    print("Task to print_numbers completed")


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    print_task()