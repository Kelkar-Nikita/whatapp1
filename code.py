import qrcode

url=input("enter url")
image=qrcode.make("hlo")
image.save("1.png")