from playsound import playsound
from view.eleven_labs import tts_elevenlabs
from controller.variavelglobal import listaHorarios
from view.interface import atualizar_lista

def disparar_alarme(lembrete, horarioAux):
    playsound(r'C:\Users\pedro\OneDrive\Área de Trabalho\TrabalhoIA\model\batAlarme.mp3')
    tts_elevenlabs(lembrete)
    print(horarioAux)
    if horarioAux in listaHorarios:
       listaHorarios.remove(horarioAux)
       atualizar_lista()