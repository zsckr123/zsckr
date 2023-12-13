import qrcode
img = qrcode.make('To jest qr code')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")