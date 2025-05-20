import qrcode

img = qrcode.make("https://www.openai.com")

img.save("openai_qr.png")
# to customize qrcode

import qrcode as qr
from PIL import Image
qr=qr.QRCode(
version=1, 
error_correction=qr.constants.ERROR_CORRECT_H,
box_size=10,
border=5)
qr.add_data("https://www.openai.com")
qr.make(fit=True)
img=qr.make_image(fill_color="purple",back_color="white")
img.show()
image.save("openai_qr.png")

