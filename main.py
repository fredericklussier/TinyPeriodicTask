#import asyncio
import time
from TinyPeriodicTask import TinyPeriodicTask

#The function to periodically run
def task(message='this'):
  print("I'm working on {0}".format(message))

task1 = TinyPeriodicTask(3, task)
task1.start()

task2 = TinyPeriodicTask(6, task, message='that')
task2.start()

try:
  print('Execution en cours')

  while True:
    time.sleep(0.5)

except KeyboardInterrupt:
  task1.stop()
  task2.stop()
  print('Loop stopped')
