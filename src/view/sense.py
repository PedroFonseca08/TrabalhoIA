from view.tts import tts_elevenlabs
from controller.find_horario import find_horario
from controller.definir_alarme import definir_alarme
from view.stt import speech_to_text
from view.interface import atualizar_lista
from controller.variavel_global import listaHorarios

# Função responsável por manter o Beto sempre funcionando
def horario_alarme():
  
  tts_elevenlabs("Olá. Eu sou o Beto. Para configurar um alarme é só me chamar.")

  # O Beto funcionará enquanto o programa estiver em execução
  while True:
    sent = 0
    print ("Nosso robô chama Beto")

    # Enquanto não for ouvida a palavra "Beto", o loop continuará
    while sent != 1:
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

    # Enquanto não for ouvido um horário válido, o loop continuará
    while sent != 1:
      arrTextHoras = speech_to_text(0)
      arrTextHoras = arrTextHoras.split(' ')
      horario = find_horario(arrTextHoras)
      if horario:
        print("Horário identificado:", horario)
        sent = 1

    # Gravação do bilhete 
    tts_elevenlabs("Grave seu lembrete")
    print ("Fale o lembrete:")
    lembrete = speech_to_text(0)
    
    print("Lembrete gravado:", lembrete)
    horarioAux = horario + " - " + lembrete

    # Definição do alarme
    definir_alarme(horario, lembrete, horarioAux)
    listaHorarios.append(horarioAux)
    atualizar_lista()
    tts_elevenlabs("Alarme definido!")

  


