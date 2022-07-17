from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#f3f3f3")
window.title('Optical Microphone')


p1 = PhotoImage(file = 'logo.png')
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

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    -51.5 +691 , 30.0+331,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    505.0+691, 247.0+331,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry0.place(
    x = 485.0+691, y = 234+331,
    width = 40.0,
    height = 24)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    430.0+691, 247.0+331,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry1.place(
    x = 409.0+691, y = 234+331,
    width = 42.0,
    height = 24)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    99.5+691, 235.5+331,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry2.place(
    x = 25.0+691, y = 216+331,
    width = 149.0,
    height = 37)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    99.5+691, 179.5+331,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry3.place(
    x = 25.0+691, y = 160+331,
    width = 149.0,
    height = 37)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    cursor = "hand2",
    relief = "flat")

b0.place(
    x = 420+691, y = 336+331,
    width = 142+8,
    height = 48+8)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    cursor = "hand2",
    relief = "flat")

b1.place(
    x = 249+691, y = 283+331,
    width = 101+8,
    height = 27+8)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    cursor = "hand2",
    relief = "flat")

b2.place(
    x = -155+691, y = 283+331,
    width = 101+10,
    height = 27+10)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    cursor = "hand2",
    relief = "flat")

b3.place(
    x = 447+691, y = 74+331,
    width = 68+8,
    height = 29+8)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    cursor = "hand2",
    relief = "flat")

b4.place(
    x = 274+691, y = 74+331,
    width = 68+8,
    height = 29+8)

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    cursor = "hand2",
    relief = "flat")

b5.place(
    x = 46+691, y = 74+331,
    width = 68+8,
    height = 29+8)

img6 = PhotoImage(file = f"img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    cursor = "hand2",
    relief = "flat")

b6.place(
    x = -115+691, y = 74+331,
    width = 68+8,
    height = 29+8)

img7 = PhotoImage(file = f"img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    cursor = "hand2",
    relief = "flat")

b7.place(
    x = -671+691, y = -316+331,
    width = 247+8,
    height = 90+8)

img8 = PhotoImage(file = f"img8.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    cursor = "hand1",
    relief = "flat")

b8.place(
    x = 511+691, y = -293+331,
    width = 39+8,
    height = 39+8)

window.resizable(False, False)
window.mainloop()
