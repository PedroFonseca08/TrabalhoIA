import speech_recognition as sr
import pyttsx3
import time
import re
import tkinter as tk
from tkinter import Listbox, Entry, Button, Scrollbar
import threading

recognizer = sr.Recognizer()
listaHorarios = []

def atualizar_lista():
    lista_box.delete(0, tk.END)  # Limpa a lista atual
    for horario in listaHorarios:
        lista_box.insert(tk.END, horario)

def adicionar_horario():
    novo_horario = horario_entry.get()
    if novo_horario:
        listaHorarios.append(novo_horario)
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
    arrText = speech_to_text()
    print ("*", arrText)
    if "beto" in arrText:
      sent = 1
    elif "Beto" in arrText:
      sent = 1
  
  sent = 0
  text_to_speech("Qual o horário do alarme?")
  while sent != 1:
    arrText = speech_to_text()
    horario = find_horario(arrText)
    if horario:
      print("Horário identificado:", horario)
      listaHorarios.append(horario)
      atualizar_lista()
      sent = 1
  


