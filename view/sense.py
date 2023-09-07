import speech_recognition as sr

def speech_to_text():
  # Initialize the recognizer
  recognizer = sr.Recognizer()

  # Capture audio from the microphone
  with sr.Microphone() as source:
    print(sr.Microphone.list_microphone_names())
    print("Fale algo...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
    audio = recognizer.listen(source,5)

  try:
    # Recognize the speech using Google Web Speech API
    text = recognizer.recognize_google(audio, language='pt-BR')
    arrText = text.split(' ')
    print("Você falou:", arrText)
  except sr.UnknownValueError:
    print("Sorry, I couldn't understand the audio.")
  except sr.RequestError as e:
    print("Sorry, an error occurred. Could not request results; {0}".format(e))
