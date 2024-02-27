# import qrcode as qr
# img = qr.make("http://youtube.com")
# img.save("kiran.png")

    # or

import  qrcode

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data("https://www.youtube.com/")
qr.make(fit=True)
img = qr.make_image(fill_color = "black",back_color = "red")
img.save("youtube.png")