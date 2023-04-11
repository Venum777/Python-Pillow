from PIL import (
    Image,
    ImageDraw,
    ImageFont
)


# img = Image.open('1.png')

# print(img.size)
# print(img.format)
# print(img.mode)

# scale_format: int = 0.2

# size =(
#     int(img.size[0] * scale_format),
#     int(img.size[1] * scale_format)
# )
# img_resize = img.resize(size=size)
# img_resize.show()
# img_resize.save('2.png')

# img_resize = img.resize(size=(3, 3))
# img_resize.show()


# size = int(input('Введите число градуса: '))

# img_rotate = img.rotate(
#     angle=size, 
#     expand=True, 
#     fillcolor=(0, 230, 200)
# )
# img_rotate.show()

# new_img = img.crop((0, 0, 800, 300))
# new_img.show()

# new_img = img.crop((0, 0, 0, 0))
# new_img.show()

# new_img = ImageDraw.Draw(img)
# my_font = ImageFont.truetype('times.ttf', size=40)
# my_text: str = 'Hello world!'

# new_img.text(
#     xy=(300, 400),
#     text=my_text,
#     font=my_font,
#     fill=(255, 255, 255, 255)
# )

# img.show()

img = Image.new(
    mode="1", 
    size=(400, 600),
    color=1
)
d1 = ImageDraw.Draw(img)
my_font = ImageFont.truetype('arial.ttf', 50)
my_text = "Магнум"
x, y, w, h = d1.textbbox((0, 0), my_text, my_font)

d1.text(
    ((img.size[0]-w)/2, 50),
    my_text,
    0,
    my_font
)

my_text = "fggfdfgl\ndjndfgdfgg\nldfgdfgs\nddfgdfgfj\ngljdfgdfgk\nfdsfdgdfglgjd\ndfgdfsgsfdfgdgdfg\nasddfgdASD\nasdsad\nasdasdsa\ngfdgdgdfgfdg"
max_height = img.size[1] - (50 + h + 30)
font_size = 50

while True:
    my_font = ImageFont.truetype('arial.ttf', font_size)
    x, y, w, h2 = d1.textbbox((0, 0), my_text, my_font)
    if h2 <= max_height or font_size <= 10:
        break
    font_size -= 1

d1.text(
    ((img.size[0]-w)/2, 50 + h + 30),
    my_text,
    0,
    my_font,
    align='center'
)

img.show()