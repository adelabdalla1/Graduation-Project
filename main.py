# ============================================================================= library =============================================================================
import os
from tkinter import *
from tkinter import filedialog as fd
from tkinter import filedialog


import cv2
import datetime


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)



#========================== Optical microphone
import cv2 as cv
import matplotlib.pyplot as plt
from os import path
from scipy.io import wavfile






import cv2 as cv
import math
import numpy as np
import pyrtools as pt
from scipy import signal


import cv2 as cv
import matplotlib.pyplot as plt
from os import path
from scipy.io import wavfile


import numpy as np
from scipy import signal

from playsound import playsound


import tkinter 
from PIL import Image, ImageTk






# ============================================================================= function =============================================================================





#========================== btn_clicked ====================================


def btn_clicked():
    print("Button Clicked")
    
    






#========================== select , disp  ====================================
    #filetypes=[("video files", ["*.mp4","*.avi"])]
def selectFile():
    global filePath
    filePath = filedialog.askopenfilename(title = "Select A Video",filetypes = (("mp4", "*.mp4"), ("avi", "*.avi")))
    print(filePath)
    
    
    file_name = os.path.basename(filePath)
    global video_name
    global video_extention
    video_name , video_extention  =os.path.splitext(file_name)
    
    
    disp_file_dir() 
    disp_file_name_extention()
    disp_video_time_reslution()
    plot_selected_video()
    
    
    entry0.delete(0, END)
    entry0.insert(0, "")
    
    
    entry1.delete(0, END)
    entry1.insert(0, "")
    
    
    entry2.delete(0, END)
    entry2.insert(0, "")
    
    
    entry3.delete(0, END)
    entry3.insert(0, "")
    
    label_Spectogram_Sound_Enhaced.after(1000, label_Spectogram_Sound_Enhaced.destroy())    
    label_Spectogram_Sound.after(1000, label_Spectogram_Sound.destroy())

    
    
    
    
def disp_file_dir():
    file_dir_disp = Label(window, height=1, width=68, fg="green",background ='#dcdcdc',text=filePath)
    file_dir_disp.place(x = 345 , y = 44)
    


def disp_file_name_extention():   
    video_name_disp = Label(window, height=1, width=30, fg="green",background ='#dcdcdc',text=video_name)
    video_name_disp.place(x = 180 , y = 463)
    
    video_extention_disp = Label(window, height=1, width=30, fg="green",background ='#dcdcdc',text=video_extention)
    video_extention_disp.place(x = 180 , y = 526)



def disp_video_time_reslution(): 
    global video
    video = cv2.VideoCapture(filePath)
    
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    
    seconds = int(frames / fps)
    video_time = str(datetime.timedelta(seconds=seconds))
    
    
    video_time_disp = Label(window, height=1, width=30, fg="green",background ='#dcdcdc',text=video_time)
    video_time_disp.place(x = 180 , y = 582)
    
    
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    
    reseluotion_disp = Label(window, height=1, width=30, fg="green",background ='#dcdcdc',text=(int(height) , 'x' ,int(width)))
    reseluotion_disp.place(x = 180 , y = 645)
    
    
    
    
    
    
def Disp_precentage_of_sound():
    progress_disp = Label(window, height=1, width=30, fg="green",background ='#dcdcdc',text='Percentage Of Processing :  '+ format(progress*100, ".2f")+' %' )
    progress_disp.place(x = 640 , y = 676)



    
    
    
    
#========================== plot Spectogarme  ====================================



def plot_specgram_Sound(sound, sampling_rate):
  plt.figure()
  plt.specgram(sound, Fs=sampling_rate, cmap=plt.get_cmap('jet'))
  plt.xlabel('Time (sec)')
  plt.ylabel('Frequency (Hz)')
  plt.colorbar().set_label('PSD (dB)')
  plt.savefig('Results/plot_specgram_sound.png')
  Plot_Spectogram_Sound()




def plot_specgram_Sound_Enhaced(sound, sampling_rate):
  plt.figure()
  plt.specgram(new_sound, Fs=sampling_rate, cmap=plt.get_cmap('jet'))
  plt.xlabel('Time (sec)')
  plt.ylabel('Frequency (Hz)')
  plt.colorbar().set_label('PSD (dB)')
  plt.savefig('Results/plot_specgram_sound_Enhaced.png')
  Plot_Spectogram_Sound_Enhaced()





#========================== plot images  ====================================


def plot_selected_video():
    #i1 = cv2.imread(filePath3)
    ret, frame = video.read()
    scaled_frame = frame
    img1 = cv2.cvtColor(scaled_frame, cv2.COLOR_BGR2RGB)
    # i2 = cv2.imread(filePath2)
    # img2 = cv2.cvtColor(i2, cv2.COLOR_BGR2RGB)


    #plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    #plt.axis('off')
    #plt.show()


    labelDraw = Canvas(window)
    labelDraw.place(
        x = 45 , y = 186,
        width=365.0,
        height=205,
    )
    # win = Tk()

    # # setting the title
    # win.title('Plotting in Tkinter')

    # # dimensions of the main window
    # win.geometry("1000x1000")

    # the figure that will contain the plot
    fig = Figure(figsize=(10, 10),
                 dpi=100)

    # list of squares
    # 	y = [i**2 for i in range(101)]

    # adding the subplot
    plot1 = fig.add_subplot()
    plot1.axis('off')
    # plot2 = fig.add_subplot(122)
    # plot2.axis('off')


    # plotting the graph
    plot1.imshow(img1)
    # plot2.imshow(img2)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=labelDraw)

    # canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()


    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   labelDraw)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()













def Plot_Spectogram_Sound():

    # Create an object of tkinter ImageTk
   # img = ImageTk.PhotoImage(Image.open("Results/plot_specgram_sound_Enhaced.png"))
    img= (Image.open('Results/plot_specgram_sound.png'))
    
    #Resize the Image using resize method
    resized_image= img.resize((270,180), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    # Create a Label Widget to display the text or Image
    global label_Spectogram_Sound
    label_Spectogram_Sound = Label(window, image = new_image, bg='#FFFFFF')
    label_Spectogram_Sound.pack()
    label_Spectogram_Sound.place(
        x = 528 , y = 207,
        width=320.0,
        height=180,
    )
    window.mainloop()





def Plot_Spectogram_Sound_Enhaced():
    # Create an object of tkinter ImageTk
   # img = ImageTk.PhotoImage(Image.open("Results/plot_specgram_sound_Enhaced.png"))
    img= (Image.open("Results/plot_specgram_sound_Enhaced.png"))
    
    #Resize the Image using resize method
    resized_image= img.resize((270,180), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    # Create a Label Widget to display the text or Image
    global label_Spectogram_Sound_Enhaced
    label_Spectogram_Sound_Enhaced = Label(window, image = new_image, bg='#FFFFFF')
    label_Spectogram_Sound_Enhaced.pack()
    label_Spectogram_Sound_Enhaced.place(
        x = 922 , y = 207,
        width=320.0,
        height=180
    )
    window.mainloop()






#========================== Gnerate Sound  (Optical microphone) ====================================



from Optical_Microphone.sound_from_video import sound_from_video
from Optical_Microphone.sound_spectral_subtraction import get_soud_spec_sub
from Optical_Microphone.sound_spectral_subtraction import get_scaled_sound





def Genearte_Sound():
    global Sampling_Rate
    Sampling_Rate = int(entry3.get())
    global Resize_factor
    Resize_factor = float(entry2.get())
    video1 = cv.VideoCapture(filePath)
    
    global sound
    sound = sound_from_video(video1, 1, 2, downsample_factor=Resize_factor)

    wavfile.write('Results/recovered_sound.wav', Sampling_Rate, sound.astype(np.float32))
    
    disp_Sound_Gnerated = Label(window, height=1, width=30, fg="green",background ='#dcdcdc',text='Sound Is Generated' )
    disp_Sound_Gnerated.place(x = 640 , y = 676)



    plot_specgram_Sound(sound, Sampling_Rate)
    

    
    





#========================== Denoise  ====================================


from Optical_Microphone.sound_spectral_subtraction_denoise import get_soud_spec_sub
from Denoise.Spectral_Subtraction_Algo import spectral_subtraction
from Denoise.Manual_Threshold_Algo import manual_threshold
from Denoise.Stationary_Noise_Algo import stationary_noise

import soundfile as sf




 
def Denoise():
    global select_algo
    select_algo = int(entry1.get())
     
    if select_algo == 1:
        #spectral_subtraction(float(entry0.get()))
        
        Url  = 'Results/recovered_sound.wav'
        data, rate  = sf.read(Url)
        data = data
        get_soud_spec_sub(data,rate,float(entry0.get()))
        Plot_Spectogram_Sound_Enhaced()
        

    elif select_algo == 2:
         stationary_noise()
         Plot_Spectogram_Sound_Enhaced()


    elif select_algo == 3:
         manual_threshold(float(entry0.get()))
         Plot_Spectogram_Sound_Enhaced()

         
    else:
        print('Your Select Is Wrong')
        Wrong_Select = Label(window, height=1, width=30, fg="green",background ='#dcdcdc',text='Your Select Is Wrong' )
        Wrong_Select.place(x = 640 , y = 676)
        
        
#========================== Save  ====================================



def Save():
    url1 = 'Results/recovered_sound.wav'
    Fs1, sound1 = wavfile.read(url1)
    
    url2 = "Results/recovered_sound_Enhaced.wav"
    Fs2, sound2 = wavfile.read(url2)
    
    url3 = "Results/recovered_sound_Enhaced+.wav"
    Fs3, sound3 = wavfile.read(url3)
    
    
    specgram1 = cv2.imread('Results/plot_specgram_sound.png')
    
    specgram2 = cv2.imread('Results/plot_specgram_sound_Enhaced.png')
    
    
    
    
    
    
    folder_selected = filedialog.askdirectory(title = "Select Save File")
    print(folder_selected)
    
    
    
    wavfile.write(path.join(folder_selected ,'recovered_sound.wav'), Fs1, sound1)
    
    wavfile.write(path.join(folder_selected ,'recovered_sound_Enhaced.wav'), Fs2, sound2)
    
    wavfile.write(path.join(folder_selected ,'recovered_sound_Enhaced+.wav'), Fs3, sound3)
    
    
    
    cv2.imwrite(path.join(folder_selected ,'plot_specgram_sound.png'),specgram1)
    cv2.imwrite(path.join(folder_selected ,'plot_specgram_sound_Enhaced.png'),specgram2)


    disp_Play_sound = Label(window, height=1, width=30, fg="green",background ='#dcdcdc',text='Files Is Saved' )
    disp_Play_sound.place(x = 640 , y = 676)
    
    
    
    
    
    
    
    
    





#========================== play sounds ====================================



def Play_sound():
    print ('Sound Is Playing')    
    playsound('Results/recovered_sound.wav')
    print ('Sound Is Complete')
    disp_Play_sound = Label(window, height=1, width=30, fg="green",background ='#dcdcdc',text='Sound Is Played' )
    disp_Play_sound.place(x = 640 , y = 676)


def Play_sound_Enhaced():
    print ('Sound Is Playing')    
    playsound('Results/recovered_sound_Enhaced+.wav')
    print ('Enhaced Sound Is Complete')
    disp_Play_sound = Label(window, height=1, width=30, fg="green",background ='#dcdcdc',text='Enhaced Sound Is Played' )
    disp_Play_sound.place(x = 640 , y = 676)
    
    


#========================== information window ====================================



def Open_Popup():
    top= Toplevel(window)
    top.geometry("1000x500")
    top.title('Optical Microphone _ Information Message')

    
    frame = Frame(top, width=1280, height=720)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    
    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("GUI/background_small_window.png"))
    
    # Create a Label Widget to display the text or Image
    label = Label(frame, image = img)
    label.pack()
    window.mainloop()







#============================================================================= GUI =============================================================================
    
window = Tk()

window.geometry("1280x720")
window.configure(bg = "#f3f3f3")
window.title('Optical Microphone')


p1 = PhotoImage(file = 'GUI/logo.png')
window.iconphoto(False, p1)


canvas = Canvas(
    window,
    bg = "#f3f3f3",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"GUI/background.png")
background = canvas.create_image(
    -51.5 +691 , 30.0+331+2,
    image=background_img)

entry0_img = PhotoImage(file = f"GUI/img_textBox0.png")
entry0_bg = canvas.create_image(
    505.0+691, 247.0+331+2,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#dcdcdc",
    highlightthickness = 0)

entry0.place(
    x = 485.0+691, y = 234+331+2,
    width = 40.0,
    height = 24)

entry1_img = PhotoImage(file = f"GUI/img_textBox1.png")
entry1_bg = canvas.create_image(
    430.0+691, 247.0+331+2,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#dcdcdc",
    highlightthickness = 0)

entry1.place(
    x = 409.0+691, y = 234+331+2,
    width = 42.0,
    height = 24)

entry2_img = PhotoImage(file = f"GUI/img_textBox2.png")
entry2_bg = canvas.create_image(
    99.5+691, 235.5+331,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#dcdcdc",
    highlightthickness = 0)

entry2.place(
    x = 25.0+691, y = 216+331+2,
    width = 149.0,
    height = 37)

entry3_img = PhotoImage(file = f"GUI/img_textBox3.png")
entry3_bg = canvas.create_image(
    99.5+691, 179.5+331,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#dcdcdc",
    highlightthickness = 0)

entry3.place(
    x = 25.0+691, y = 160+331+2,
    width = 149.0,
    height = 37)

img0 = PhotoImage(file = f"GUI/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = Save,
    cursor = "hand2",
    relief = "flat")

b0.place(
    x = 420+691, y = 336+331,
    width = 142+8,
    height = 48+8)

img1 = PhotoImage(file = f"GUI/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = Denoise,
    cursor = "hand2",
    relief = "flat")

b1.place(
    x = 249+691, y = 283+331,
    width = 101+8,
    height = 27+8)

img2 = PhotoImage(file = f"GUI/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = Genearte_Sound,
    cursor = "hand2",
    relief = "flat")

b2.place(
    x = -155+691, y = 283+331,
    width = 101+10,
    height = 27+10)

# =============================================================================
# img3 = PhotoImage(file = f"GUI/img3.png")
# b3 = Button(
#     image = img3,
#     borderwidth = 0,
#     highlightthickness = 0,
#     command = btn_clicked,
#     cursor = "hand2",
#     relief = "flat")
# 
# b3.place(
#     x = 447+691, y = 74+331,
#     width = 68+8,
#     height = 29+8)
# =============================================================================

img4 = PhotoImage(file = f"GUI/img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = Play_sound_Enhaced,
    cursor = "hand2",
    relief = "flat")

b4.place(
    x = 922+160-38, y = 74+331,
    width = 68+8,
    height = 29+8)

# =============================================================================
# img5 = PhotoImage(file = f"GUI/img5.png")
# b5 = Button(
#     image = img5,
#     borderwidth = 0,
#     highlightthickness = 0,
#     command = btn_clicked,
#     cursor = "hand2",
#     relief = "flat")
# 
# b5.place(
#     x = 46+691, y = 74+331,
#     width = 68+8,
#     height = 29+8)
# =============================================================================

img6 = PhotoImage(file = f"GUI/img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = Play_sound,
    cursor = "hand2",
    relief = "flat")

b6.place(
    x = 528+160-38, y = 74+331,
    width = 68+8,
    height = 29+8)

img7 = PhotoImage(file = f"GUI/img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = selectFile,
    cursor = "hand2",
    relief = "flat")

b7.place(
    x = -671+691, y = -316+331,
    width = 247+8,
    height = 90+8)

img8 = PhotoImage(file = f"GUI/img8.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = Open_Popup,
    cursor = "hand1",
    relief = "flat")

b8.place(
    x = 511+691, y = -293+331,
    width = 39+8,
    height = 39+8)

window.resizable(False, False)
window.mainloop()
