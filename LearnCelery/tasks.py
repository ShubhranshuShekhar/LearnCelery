from celery import Celery
# import celeryconfig

app = Celery('tasks', broker='amqp://localhost', backend='amqp://',)

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    app.start()
    app.worker_main()


@app.task(name="tasks.add")
def add(x, y):
    print("X =\t%d" % x)
    print("Y =\t%d" % y)
    print(x + y)
    return x + y

# @app.task
# def mul(x, y):
#     return x * y
#
# @app.task
# def xsum(numbers):
#     return sum(numbers)
