import qrcode

text=input("enter the text or url to be converted in Qrcode:")
filename=input("Enter filename to save the qrcode image:")

def generate_qr_code(text, filename):
    image_qrcode=qrcode.make(text)
    image_qrcode.save(filename)
generate_qr_code(text, filename)