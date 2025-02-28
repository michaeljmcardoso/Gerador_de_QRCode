import qrcode

img = qrcode.make('https://play.google.com/store/apps/details?id=com.zumbiverde.barbuddybrasil&hl=pt_BR')
print(type(img))
print(img.size)

img.save('qrcode_budd_app.png')
