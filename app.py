############------------ IMPORTS ------------############
from datetime import datetime, timedelta
import time
from redis import Redis
from rq import Queue
from rq.job import Retry
import tasks


############------------ GLOBAL VARIABLE(S) ------------############
queue = Queue(connection=Redis())


############------------ FUNCTION(S) ------------############
def queue_tasks():
    queue.enqueue(tasks.print_task, 1, retry=Retry(max=2))
    # queue.enqueue_in(timedelta(seconds=10), tasks.print_numbers, 5)


def main():
    queue_tasks()


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    main()