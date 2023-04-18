from tkinter import *
from tkinter import filedialog
from PIL import Image
import pylibjpeg
# import pyzlib

image_path = ''
watermark_image = ''

window = Tk()
window.title('Image Watermarker')
window.config(padx=20, pady=20)


def file_select_button():
    global image_path
    image_path = filedialog.askopenfilename()
    file_text.config(text=image_path)


def watermark_select():
    global watermark_image
    watermark_image = filedialog.askopenfilename()


def watermark():
    global image_path
    global watermark_image
    image_to_watermark = Image.open(image_path)
    with Image.open(watermark_image) as wm:
        (width, height) = (wm.width // 6, wm.height // 6)
        watermark_to_apply = wm.resize((width, height))

    image_to_watermark.paste(watermark_to_apply, (0,0))
    image_to_watermark.save('C:/Users/bnkrd/Pictures/Watermarked images')


canvas = Canvas(width=400, height=400)
logo = PhotoImage(file='header-image.png')
canvas.create_image(200, 200, image=logo)
canvas.grid(column=1, row=0)

title = Label(text='Welcome to the Image Watermarker.')
title.grid(column=1, row=1, sticky='ew')

image_path_title = Label(text='Please select the image you would like to watermark.')
image_path_title.grid(column=1, row=2, sticky='ew')

select_button = Button(text='Select File', command=file_select_button)
select_button.grid(column=0, row=3)

file_text = Label(text='')
file_text.grid(column=1, columnspan=2, row=3)

watermark_image_button = Button(text='Select watermark', command=watermark_select)
watermark_image_button.grid(column=2, row=3)

watermark_button = Button(text='Watermark!', command=watermark)
watermark_button.grid(column=1, row=4)

window.mainloop()
