import execute
import threading, time
import datetime
from time import sleep


WAIT_TIME_SECONDS = 86400

ticker =threading.Event()

while not ticker.wait(WAIT_TIME_SECONDS):
    execute.run()
    now = datetime.datetime.now()
    time = f'{now.hour}:{now.minute}:{now._second} '
    print(f'Task executed at {time}')

    sleep(43200)

    execute.run()
    now = datetime.datetime.now()
    time = f'{now.hour}:{now.minute}:{now._second} '
    print(f'Task executed at {time}')

    