from view.eleven_labs import tts_elevenlabs
from controller.find_horario import find_horario
from controller.definir_alarme import definir_alarme
from view.speech_to_text import speech_to_text
from view.interface import atualizar_lista
from controller.variavelglobal import listaHorarios

def horario_alarme():
  
  while True:
    sent = 0
    while sent != 1:
      print ("Nosso robô chama Beto")
      print ("Fale algo:")
      arrTextBeto = speech_to_text(1)
      arrTextBeto = arrTextBeto.split(' ')
      if "beto" in arrTextBeto:
        sent = 1
      elif "Beto" in arrTextBeto:
        sent = 1
    
    sent = 0
    tts_elevenlabs("Qual o horário do alarme?")
    print ("Fale o horário:")

    while sent != 1:
      arrTextHoras = speech_to_text(0)
      arrTextHoras = arrTextHoras.split(' ')
      horario = find_horario(arrTextHoras)
      if horario:
        print("Horário identificado:", horario)
        sent = 1

    tts_elevenlabs("Grave seu lembrete")
    print ("Fale o lembrete:")
    lembrete = speech_to_text(0)
    
    print("Lembrete gravado:", lembrete)
    horarioAux = horario + " - " + lembrete

    definir_alarme(horario, lembrete,horarioAux)
    listaHorarios.append(horarioAux)
    atualizar_lista()
    

  


