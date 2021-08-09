## Intro to Redis

Playing around with Redis (intro level). 

Starting with _How to Run Your First Task with RQ, Redis, and Python_ from [Twilio](https://www.twilio.com/blog/first-task-rq-redis-python).


### Env

- `conda create -n redis`
- `conda activate redis`
- `brew install redis`
- `conda install -c conda-forge rq`
- `conda install -c anaconda pytz`

### RUN

3 tabs are needed: 

1. `redis-server`
2. `rq worker --with-scheduler`
3. `python app.py`