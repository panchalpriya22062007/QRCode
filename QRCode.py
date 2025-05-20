import qrcode

img = qrcode.make("https://www.openai.com")

img.save("openai_qr.png")


