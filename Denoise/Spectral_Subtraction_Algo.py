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
  
  
  
  

def spectral_subtraction(noise_cliped):
    
    Url  = 'Results/recovered_sound.wav'
    data, Fs  = sf.read(Url)
    data = data
        #--------------------------------------------select end second for clip of noise--------------------------------------------
    end_sec   = noise_cliped
        #----------------------------------know time of wav audio-----------------------------------------------
    n = data.size
    t = n / Fs
        #--------------------------------------------select clip of noise only-------------------------------------
    presentag_crop = end_sec*100/t
    Fs_crop = Fs*presentag_crop/100
    Fs_crop = int(Fs_crop)
    size_data_crop = data.size*presentag_crop/100
    size_data_crop = int(size_data_crop)
    data_crop = []
    data_crop = data[0:size_data_crop]
       
        
        #--------------------------------------------reduce noise-------------------------------------
    reduced_noise = nr.reduce_noise(y = data,sr=Fs,y_noise=data_crop,time_mask_smooth_ms=120)
        
        #--------------------------------------------plot after reduce------------------------------------
    plot_specgram_Sound(reduced_noise,Fs)
    
        #--------------------------------------------create wav file after reduce------------------------------------
    wavfile.write("Results/recovered_sound_Enhaced.wav", Fs, reduced_noise.astype(np.float32))
      
      
    wavfile.write("Results/recovered_sound_Enhaced+.wav", Fs, (reduced_noise.astype(np.float32))*4)
    
    print('done1')