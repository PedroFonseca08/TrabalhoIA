import threading
from view.interface import criar_interface
from view.sense import horario_alarme
from controller.loop_alarme import loop_alarme

def runRobot():

  interface_thread = threading.Thread(target=criar_interface)
  interface_thread.daemon = True
  interface_thread.start()

  alarme_thread = threading.Thread(target=horario_alarme)
  alarme_thread.daemon = True  
  alarme_thread.start()

  loop_alarme()

