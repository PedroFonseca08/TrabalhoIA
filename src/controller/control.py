import threading
from view.interface import criar_interface
from view.sense import horario_alarme
from controller.loop_alarme import loop_alarme

# Função responsável por criar todas as threads necessárias 
def runRobot():

  # Thread para a interface gráfica
  interface_thread = threading.Thread(target=criar_interface)
  interface_thread.daemon = True
  interface_thread.start()

  # Thread para o loop do beto
  alarme_thread = threading.Thread(target=horario_alarme)
  alarme_thread.daemon = True  
  alarme_thread.start()

  # Thread principal irá verificar se o alarme deve ser ativo ou não
  loop_alarme()

