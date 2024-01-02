import qrcode
img = qrcode.make('Wiadomość poufna')
img.save("some_file.png")