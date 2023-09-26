import speech_recognition as sr

recognizer = sr.Recognizer()

def speech_to_text(flag):

  # Captura o áudio do microfone
  with sr.Microphone() as source:
    text = ""
    print("*")
    recognizer.adjust_for_ambient_noise(source)  # Ajusta o barulho do ambiente
    try:
      if flag == 1:
        audio = recognizer.listen(source, phrase_time_limit = 3)
      else:
         audio = recognizer.listen(source)
    except sr.WaitTimeoutError:
      print("Tempo limite excedido. Não foi possível detectar fala dentro do limite de tempo.")

    try:
      # Recognize the speech using Google Web Speech API
      text = recognizer.recognize_google(audio, language='pt-BR')
      print("Você falou:", text)
    except sr.UnknownValueError:
      print("Desculpe, não foi possível entender o que você disse")
    except sr.RequestError as e:
      print("Desculpe, um erro ocorreu. Não foi possível solicitar resultados.; {0}".format(e))
  return text