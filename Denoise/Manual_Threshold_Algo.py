#--------------------------------------------libraries--------------------------------------------
import noisereduce as nr
from matplotlib import pyplot as plt
from scipy.ndimage import maximum_filter1d
from scipy.io import wavfile
import soundfile as sf
import numpy as np




def plot_specgram_Sound(new_sound, sampling_rate):
    plt.figure()
    plt.specgram(new_sound, Fs=sampling_rate, cmap=plt.get_cmap('jet'))
    plt.xlabel('Time (sec)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar().set_label('PSD (dB)')
    plt.savefig('Results/plot_specgram_sound_Enhaced.png')




def manual_threshold(thr):
    
        #--------------------------------------------upload wav file--------------------------------------------
    bird_url  = 'Results/recovered_sound.wav'
    data, rate  = sf.read(bird_url)
    data = data
    
        #--------------------------------------------function for select low frequency--------------------------------------------
    def envelope(y, rate, threshold):
        mask = []
        y_mean = maximum_filter1d(np.abs(y), mode="constant", size=rate//20)
        for mean in y_mean:
            if mean > threshold:
                mask.append(True)
            else:
                    mask.append(False)
        return mask, y_mean
        #--------------------------------------------call function------------------------------------
    mask, env = envelope(data, rate, thr)
        #--------------------------------------------reduce noise--------------------------------------------
    reduced_noise = nr.reduce_noise(y=data,sr=rate, y_noise=data[np.logical_not(mask)],time_mask_smooth_ms=120)
    #--------------------------------------------plot before reduce------------------------------------
    plot_specgram_Sound(reduced_noise,rate)

    #--------------------------------------------create wav file ater reduce--------------------------------------------

    wavfile.write("Results/recovered_sound_Enhaced.wav", rate , reduced_noise.astype(np.float32))
      
      
    wavfile.write("Results/recovered_sound_Enhaced+.wav", rate, (reduced_noise.astype(np.float32))*4)
    
    print('done3')
    
    