from playsound import playsound
from view.tts import tts_elevenlabs
from controller.variavel_global import listaHorarios
from view.interface import atualizar_lista

# Função responsável por emitir um bat-alarme e o lembrete
def disparar_alarme(lembrete, horarioAux):
    try:
        playsound(r'C:\Users\pedro\OneDrive\Área de Trabalho\TrabalhoIA\model\batAlarme.mp3')
        # playsound(r'/home/lucasmalachias/l/CC/IA/TrabalhoIA/backup/src/model/batAlarme.mp3')
    except:
        print("Não foi possível ativar o Bat-Alarme")
    tts_elevenlabs(lembrete)
    print(horarioAux)
    # Remoção do lembrete na interface gráfica
    if horarioAux in listaHorarios:
       listaHorarios.remove(horarioAux)
       atualizar_lista()