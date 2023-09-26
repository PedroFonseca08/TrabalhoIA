import tkinter as tk
import threading
import datetime
import schedule
from playsound import playsound
from view.eleven_labs import tts_elevenlabs
from controller.find_horario import find_horario
from view.speech_to_text import speech_to_text
from controller.loop_alarme import loop_alarme


listaHorarios = []

def disparar_alarme(lembrete, horarioAux):
    playsound(r'C:\Users\pedro\OneDrive\Área de Trabalho\TrabalhoIA\model\batAlarme.mp3')
    tts_elevenlabs(lembrete)
    print(horarioAux)
    if horarioAux in listaHorarios:
       listaHorarios.remove(horarioAux)
       atualizar_lista()

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

def atualizar_lista():
    lista_box.delete(0, tk.END)  # Limpa a lista atual
    for horario in listaHorarios:
        lista_box.insert(tk.END, horario)

def criar_interface():
  global horario_entry 
  global lista_box

  root = tk.Tk()
  root.title("Horários")
  root.geometry("400x500")  # Aumenta a altura da janela
  root.iconbitmap(r'C:\Users\pedro\OneDrive\Área de Trabalho\TrabalhoIA\model\icone.ico')

  # Criação da lista de horários
  lista_frame = tk.Frame(root)
  lista_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)  # Preenche o espaço disponível

  scrollbar = tk.Scrollbar(lista_frame, orient=tk.VERTICAL)
  lista_box = tk.Listbox(lista_frame, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set, font=("Arial", 12))
  scrollbar.config(command=lista_box.yview)
  scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
  lista_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

  # Botão para fechar a janela
  fechar_button = tk.Button(root, text="Fechar", command=root.quit)
  fechar_button.pack(padx=10, pady=10)

  # Cria e inicia a thread para adicionar horários
  alarme_thread = threading.Thread(target=horario_alarme)
  alarme_thread.daemon = True  # A thread será encerrada quando a janela for fechada
  alarme_thread.start()

  loopAlarme_thread = threading.Thread(target=loop_alarme)
  loopAlarme_thread.daemon = True
  loopAlarme_thread.start()

  root.mainloop()

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
    

  


