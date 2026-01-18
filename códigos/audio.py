import sounddevice as sd
import numpy as np
# biblioteca numpy - versão 2.4.1
# biblioteca sounddevice - versão 0.5.3

_volume = 0.0

def _callback(indata, frames, time, status):
    global _volume
    _volume = np.linalg.norm(indata)

def iniciar_microfone():
    stream = sd.InputStream(callback=_callback)
    stream.start()
    return stream

def pegar_volume():
    return min(_volume * 5, 1)