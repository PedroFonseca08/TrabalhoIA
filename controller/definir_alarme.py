import datetime
import schedule
from view.disparar_alarme import disparar_alarme

def definir_alarme(hora_alarme, lembrete, horarioAux):
  try:
      # Divida a hora e os minutos da string fornecida
      hora, minutos = map(int, hora_alarme.split(':'))
      
      # Obtenha a data e hora atual
      agora = datetime.datetime.now()
      
      # Crie um objeto datetime com a data atual e a hora fornecida
      hora_alarme = agora.replace(hour=hora, minute=minutos, second=0, microsecond=0)
      
      # Calcule a diferença entre o alarme e a hora atual
      diferenca = hora_alarme - agora
      
      # Garanta que a diferença seja positiva
      if diferenca.total_seconds() < 0:
          # Se o alarme estiver definido para o próximo dia
          hora_alarme += datetime.timedelta(days=1)
      
      # Agende o alarme com o schedule
      schedule.every().day.at(hora_alarme.strftime("%H:%M")).do(disparar_alarme, lembrete=lembrete, horarioAux=horarioAux)
  except ValueError:
      print("Formato de hora inválido. Use o formato '00:00'.")