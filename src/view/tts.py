from elevenlabs import clone, generate, play, set_api_key
from elevenlabs.api import History

set_api_key("9d6d699e10bbf481fdbfb7792811d91b")

from elevenlabs import generate, play

def tts_elevenlabs(audioText):
    audio = generate(
    text=audioText,
    voice="Charlie",
    model="eleven_multilingual_v2"
    )

    play(audio)