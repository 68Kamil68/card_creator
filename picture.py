from PIL import Image, ImageDraw
import base64
from io import BytesIO


def create_picture():
    profile_pic = Image.open('profile.jpg', 'r')
    resized = profile_pic.resize((200, 350), Image.ANTIALIAS)
    resized.save('profile_resized.jpg', optimize=True)
    img = Image.new('RGB', (1016, 648), color='white')
    writer = ImageDraw.Draw(img)
    writer.text((300, 200), "Jan", fill=(0, 0, 0))
    writer.text((300, 300), "Kowalski", fill=(0, 0, 0))
    writer.text((300, 400), "01 Grudnia 1997", fill=(0, 0, 0))
    writer.text((300, 500),  "ul. Akacjowa, 19-411 Swietajno", fill=(0, 0, 0))
    writer.text((300, 600), "Jan Kowalski", fill=(0, 0, 0))
    writer.text((600, 600), "01 Grudnia 2018", fill=(0, 0, 0))
    writer.text((100, 600), "5761", fill=(0, 0, 0))
    writer.multiline_text((800, 250),
                          "Szkola podstawowa nr 4 \n we Wroclawiu \n ul. Akacjowa 6 \n 52-200 Wroclaw",
                          fill=(0, 0, 0))
    img.paste(resized, (50, 200))
    img.save('test_img.bmp', "BMP")
    buffered = BytesIO()
    img.save(buffered, format="BMP")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    string_file = open("base64.txt", 'w+')
    string_file.write(img_str)


if __name__ == "__main__":
    create_picture()
