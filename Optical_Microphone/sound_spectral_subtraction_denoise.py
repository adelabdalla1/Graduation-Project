import numpy as np
from scipy import signal

from scipy.io import wavfile
import noisereduce as nr
import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np

 
  
  


def plot_specgram_Sound(new_sound, sampling_rate):
  plt.figure()
  plt.specgram(new_sound, Fs=sampling_rate, cmap=plt.get_cmap('jet'))
  plt.xlabel('Time (sec)')
  plt.ylabel('Frequency (Hz)')
  plt.colorbar().set_label('PSD (dB)')
  plt.savefig('Results/plot_specgram_sound_Enhaced.png')
  


  
  
# This function scale and center sound to the range [-1, 1]
def get_scaled_sound(sound: np.array):
  maxv = np.max(sound)
  minv = np.min(sound)

  if maxv != 1.0 or minv != -1.0:
    rangev = maxv - minv
    sound = 2 * sound / rangev
    newmax = np.max(sound)
    offset = newmax - 1.0
    sound -= offset

  return sound


# Function to improve sound using spectral subtraction. Adapted
# from the original work of Myers Abraham Davis (Abe Davis), MIT
def get_soud_spec_sub(sound: np.array, Fs,qtl=0.5):
  _, _, st = signal.stft(sound)

  st_mags = np.multiply(np.abs(st), np.abs(st))
  st_angles = np.angle(st)

  noise_floor = np.quantile(st_mags, qtl, axis=-1)

  for t in range(st_mags.shape[-1]):
    st_mags[:, t] -= noise_floor
    st_mags[:, t] = np.maximum(st_mags[:, t], 0.0)

  st_mags = np.sqrt(st_mags)
  newst = np.multiply(st_mags, 1j * st_angles)

  _, new_sound = signal.istft(newst)

  new_sound = get_scaled_sound(new_sound)
  
  plot_specgram_Sound(new_sound,Fs)
  

  wavfile.write("Results/recovered_sound_Enhaced.wav", Fs, new_sound.astype(np.float32))
  
  
  wavfile.write("Results/recovered_sound_Enhaced+.wav", Fs, (new_sound.astype(np.float32))*4)
  
  

  return new_sound