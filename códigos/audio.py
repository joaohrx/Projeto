import sounddevice as sd
import numpy as np
# biblioteca numpy - versão 2.4.1
# biblioteca sounddevice - versão 0.5.3

_volume = 0.0

def _callback(indata, frames, time, status):
    global _volume
    _volume = np.linalg.norm(indata)

def iniciar_microfone():
    try:
        stream = sd.InputStream(
            channels=1,
            callback=_callback,
            samplerate=44100
        )
        stream.start()
        return stream
    except Exception as e:
        print("Erro ao iniciar microfone:", e)
        return None

def pegar_volume():
    return min(_volume * 5, 1)