import qrcode

img = qrcode.make(
    ''
)
img.save('myQRcode.png')
img.show()
