############------------ IMPORTS ------------############
from datetime import datetime, timedelta
import time
import random
import pytz


############------------ FUNCTION(S) ------------############
def print_newyorkcity_time(seconds):
    print("Starting print_newyorkcity_time task")

    for second in range(seconds):
            tz_nyc = pytz.timezone('America/New_York') 
            datetime_nyc = datetime.now(tz_nyc)
            print("NY time:", datetime_nyc.strftime("%H:%M:%S"))

            time.sleep(1)

    print("Task print_newyorkcity_time completed")


def print_london_time(seconds):
    print("Starting print_london_time task")

    for second in range(seconds):
        tz_London = pytz.timezone('Europe/London')
        datetime_London = datetime.now(tz_London)
        print("London time:", datetime_London.strftime("%H:%M:%S"))

    print("Task to print_london_time completed")


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    print_newyorkcity_time()

    print_london_time()