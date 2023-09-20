import speech_recognition as sr
import pyttsx3
import time
import re
import tkinter as tk
from tkinter import Listbox, Entry, Button, Scrollbar
import threading
import datetime
import schedule

recognizer = sr.Recognizer()
listaHorarios = []

def disparar_alarme(hora_alarme):
    print(f"Alarme disparado às {hora_alarme.strftime('%H:%M')}")


def definir_alarme(hora_alarme):
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
      schedule.every().day.at(hora_alarme.strftime("%H:%M")).do(disparar_alarme, hora_alarme=hora_alarme)
  
  except ValueError:
      print("Formato de hora inválido. Use o formato '00:00'.")

def atualizar_lista():
    lista_box.delete(0, tk.END)  # Limpa a lista atual
    for horario in listaHorarios:
        lista_box.insert(tk.END, horario)

def adicionar_horario():
    novo_horario = horario_entry.get()
    if novo_horario:
        listaHorarios.append(novo_horario)
        definir_alarme(novo_horario)
        atualizar_lista()

def remover_horario():
    selected_index = lista_box.curselection()
    if selected_index:
        listaHorarios.pop(selected_index[0])
        atualizar_lista()

def find_horario(arrText):
    # Padrão de regex para encontrar horários no formato HH:MM
    padrao_horario1 = r'\d{2}:\d{2}'
    padrao_horario2 = r'\d{1}:\d{2}'

    horario = ""

    # Procura por correspondências em cada elemento da lista usando regex
    for palavra in arrText:
        correspondencias = re.findall(padrao_horario1, palavra)
        if correspondencias:
            horario = correspondencias[0]
            break
        correspondencias = re.findall(padrao_horario2, palavra)
        if correspondencias:
            horario = correspondencias[0]
            break
    
    # Retorna a lista de horários encontrados
    return horario

def loopAlarme():
  while True:
      schedule.run_pending()
      time.sleep(1)

def criar_interface():
    global horario_entry 
    global lista_box

    root = tk.Tk()
    root.title("Horários")

    # Criação da lista de horários
    lista_frame = tk.Frame(root)
    lista_frame.pack(padx=10, pady=10)

    scrollbar = Scrollbar(lista_frame, orient=tk.VERTICAL)
    lista_box = Listbox(lista_frame, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set)
    scrollbar.config(command=lista_box.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lista_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    atualizar_lista()  # Preenche a lista inicialmente

    # Entrada de texto para adicionar horários
    horario_entry = Entry(root)
    horario_entry.pack(padx=10, pady=5)

    # Botão para adicionar horários
    adicionar_button = Button(root, text="Adicionar Horário", command=adicionar_horario)
    adicionar_button.pack(padx=10, pady=5)

    # Botão para remover horários
    remover_button = Button(root, text="Remover Horário", command=remover_horario)
    remover_button.pack(padx=10, pady=5)

    # Botão para fechar a janela
    fechar_button = Button(root, text="Fechar", command=root.quit)
    fechar_button.pack(padx=10, pady=10)

    # Cria e inicia a thread para adicionar horários
    alarme_thread = threading.Thread(target=horario_alarme)
    alarme_thread.daemon = True  # A thread será encerrada quando a janela for fechada
    alarme_thread.start()

    loopAlarme_thread = threading.Thread(target=loopAlarme)
    loopAlarme_thread.daemon = True
    loopAlarme_thread.start()

    root.mainloop()
    
def text_to_speech(text):
    # Inicialize o mecanismo de síntese de voz
    engine = pyttsx3.init()
  
    # Defina a voz que você deseja usar (opcional)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Escolhe a primeira voz disponível

    # Faça o sistema falar a frase
    engine.say(text)
    engine.runAndWait()

def speech_to_text():

  # Capture audio from the microphone
  with sr.Microphone() as source:
    arrText = ""
    print("Fale algo...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
    try:
      audio = recognizer.listen(source, phrase_time_limit = 3)
    except sr.WaitTimeoutError:
      print("Tempo limite excedido. Não foi possível detectar fala dentro do limite de tempo.")

    try:
      # Recognize the speech using Google Web Speech API
      text = recognizer.recognize_google(audio, language='pt-BR')
      arrText = text.split(' ')
      print("Você falou:", arrText)
    except sr.UnknownValueError:
      print("Sorry, I couldn't understand the audio.")
    except sr.RequestError as e:
      print("Sorry, an error occurred. Could not request results; {0}".format(e))
  return arrText

def horario_alarme():
  sent = 0
  while sent != 1:
    arrTextBeto = speech_to_text()
    print ("*", arrTextBeto)
    if "beto" in arrTextBeto:
      sent = 1
    elif "Beto" in arrTextBeto:
      sent = 1
  
  sent = 0
  text_to_speech("Qual o horário do alarme?")
  while sent != 1:
    arrTextHoras = speech_to_text()
    horario = find_horario(arrTextHoras)
    if horario:
      print("Horário identificado:", horario)
      listaHorarios.append(horario)
      atualizar_lista()
      sent = 1
  definir_alarme(horario)
  text_to_speech("Grave seu lembrete")
  lembrete = speech_to_text()
  print("Lembrete gravado:", lembrete)

  


