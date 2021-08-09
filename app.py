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
    loops = 0
    
    while loops < 3:
        queue.enqueue(tasks.print_newyorkcity_time, 5, retry=Retry(max=2))
        queue.enqueue_in(timedelta(seconds=5), tasks.print_london_time, 5)

        loops += 1
    


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    queue_tasks()