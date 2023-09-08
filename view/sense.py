import speech_recognition as sr
import pyttsx3
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

def criar_interface():
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

    # Botão para fechar a janela
    fechar_button = Button(root, text="Fechar", command=root.quit)
    fechar_button.pack(padx=10, pady=10)

    # Cria e inicia a thread para adicionar horários
    ouvinte_thread = threading.Thread(target=speech_to_text)
    ouvinte_thread.daemon = True  # A thread será encerrada quando a janela for fechada
    ouvinte_thread.start()

    root.mainloop()

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
  # Initialize the recognizer
  sent = 0

  # Capture audio from the microphone
  with sr.Microphone() as source:
    print("Fale algo...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
    while sent == 0:
      audio = recognizer.listen(source,2)

      try:
        # Recognize the speech using Google Web Speech API
        text = recognizer.recognize_google(audio, language='pt-BR')
        arrText = text.split(' ')
        if "qualquer" in arrText:
          sent = 1
        print("Você falou:", arrText)
      except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
      except sr.RequestError as e:
        print("Sorry, an error occurred. Could not request results; {0}".format(e))
    horario_alarme()


def horario_alarme():
  text_to_speech("Qual o horário do alarme?")

  with sr.Microphone() as source:
    print("Fale algo...")
    recognizer.adjust_for_ambient_noise(source)  # Ajusta para o ruído

    audio = recognizer.listen(source, 2)
    try:
      # Reconhece o discurso usando o Google Web Speech API
      text = recognizer.recognize_google(audio, language='pt-BR')
      arrText = text.split(' ')
      print("Você falou:", arrText)

      # Procura por um horário no texto usando regex
      horario = find_horario(arrText)
      if horario:
          print("Horário identificado:", horario)
          listaHorarios.append(horario)
          atualizar_lista()
      else:
          print("Nenhum horário identificado.")
    except sr.UnknownValueError:
        print("Desculpe, não consegui entender o áudio.")
    except sr.RequestError as e:
        print("Desculpe, ocorreu um erro. Não foi possível obter resultados; {0}".format(e))

