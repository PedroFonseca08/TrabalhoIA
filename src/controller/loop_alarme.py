import schedule
import time

def loop_alarme():
  while True:
      schedule.run_pending()
      time.sleep(1)