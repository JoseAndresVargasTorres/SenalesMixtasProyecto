
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


def calculate_spectrogram(audio_file):
    # Cargar el archivo de audio utilizando Librosa
    y, sr = librosa.load(audio_file)

    # Calcular el espectrograma utilizando la transformada de Fourier de tiempo corto (STFT)
    spectrogram = librosa.amplitude_to_db(librosa.stft(y), ref=np.max)

    # Visualizar el espectrograma
    plt.figure(figsize=(10, 6))
    librosa.display.specshow(spectrogram, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Espectrograma de la señal de audio')
    plt.show()


# Llamada a la función con un archivo de audio
calculate_spectrogram('AvaMaxSoamI.wav')
