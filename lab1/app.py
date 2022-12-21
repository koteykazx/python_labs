from PIL import Image, ImageFilter

img = Image.open("apple.jpg")

img_blurred = img.filter(filter=ImageFilter.BLUR)
im1 = img.convert('1')
imL = img.convert('L')
imLA = img.convert('LA')

img_blurred.show()
im1.show()
imL.show()
imLA.show()

img_blurred.save("apple_blured.jpg")
im1.save("im1.png")
imL.save("imL.png")
imLA.save("imLA.png")

