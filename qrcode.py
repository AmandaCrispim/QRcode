import qrcode

img = qrcode.make(
    'link'
)
img.save('myQRcode.png')
img.show()
