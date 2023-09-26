import speech_recognition as sr

recognizer = sr.Recognizer()

def speech_to_text(flag):

  # Capture audio from the microphone
  with sr.Microphone() as source:
    text = ""
    recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
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
      print("Eu... Eu não entendi o que você falou")
    except sr.RequestError as e:
      print("Sorry, an error occurred. Could not request results; {0}".format(e))
  return text