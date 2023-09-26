from playsound import playsound
from view.tts import tts_elevenlabs
from controller.variavel_global import listaHorarios
from view.interface import atualizar_lista

def disparar_alarme(lembrete, horarioAux):
    # playsound(r'C:\Users\pedro\OneDrive\Área de Trabalho\TrabalhoIA\model\batAlarme.mp3')
    playsound(r'/home/lucasmalachias/l/CC/IA/TrabalhoIA/backup/src/model/batAlarme.mp3')
    tts_elevenlabs(lembrete)
    print(horarioAux)
    if horarioAux in listaHorarios:
       listaHorarios.remove(horarioAux)
       atualizar_lista()