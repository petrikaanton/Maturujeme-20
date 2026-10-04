from PIL import Image, ImageDraw
bez_pismena = ""
height = 0
width = 0
longest = 0
fr = open("text.txt","r").read().lower()
for i in range(97,122):
    if fr.count(chr(i)) > 0:
        print(chr(i-32),"-", fr.count(chr(i)))
    else:
        bez_pismena += chr(i-32)
print("Tieto písmená sav texte nenachádzajú:",bez_pismena)
for line in open("text.txt","r").read().splitlines():
    height += 14
    if len(line) > longest:
        longest = len(line)*25
    width = longest
image = Image.new("RGBA", (width, height), "white")
draw = ImageDraw.Draw(image)
draw.text((2,0), open("text.txt","r").read(), fill="black")
image.show()
