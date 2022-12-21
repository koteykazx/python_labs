from PIL import Image

img = Image.open("apple.jpg")
img = img.convert("1")

(width, height) = img.size
data = list(img.getdata())

f = open("ph2.txt", "w")
count = 0

print(type(data))
print((width, height))
for i in data:
    if i == 255:
        f.write('1')
    if i == 0:
        f.write('0')
    count += 1
    if count == width:
        count = 0
        f.write('\n') 
        
f.close()
