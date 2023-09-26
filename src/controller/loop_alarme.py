import schedule
import time

# Função responsável por verificar se o alarme deve ser ativado ou não
def loop_alarme():
  while True:
      schedule.run_pending()
      time.sleep(1)