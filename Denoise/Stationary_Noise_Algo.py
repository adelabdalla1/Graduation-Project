#--------------------------------------------libraries--------------------------------------------
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



def stationary_noise():
    
    
    Url  = 'Results/recovered_sound.wav'
    data, rate  = sf.read(Url)
    data = data


    #--------------------------------------------reduce noise-------------------------------------
    reduced_noise = nr.reduce_noise(y = data, sr=rate,time_mask_smooth_ms=120)
    
    
    #--------------------------------------------plot after reduce------------------------------------
    
    
    plot_specgram_Sound(reduced_noise,rate)
    
    
    
    
    wavfile.write("Results/recovered_sound_Enhaced.wav", rate , reduced_noise.astype(np.float32))
      
      
    wavfile.write("Results/recovered_sound_Enhaced+.wav", rate, (reduced_noise.astype(np.float32))*4)
    
    print('done2')