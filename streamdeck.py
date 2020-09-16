
import os
import threading

from PIL import Image, ImageDraw, ImageFont
from StreamDeck.DeviceManager import DeviceManager
from StreamDeck.ImageHelpers import PILHelper


ICON_PATH = os.path.join(os.path.dirname(__file__), "icons")



# borrowed from https://github.com/abcminiuser/python-elgato-streamdeck/

def create_image(deck, background='black'):
    from PIL import Image

    image_format = deck.key_image_format()

    return Image.new("RGB", image_format['size'], background)



def create_scaled_image(deck, image, margins=[0, 0, 0, 0], background='black'):
    from PIL import Image

    if len(margins) != 4:
        raise ValueError("Margins should be given as an array of four integers.")

    final_image = create_image(deck, background=background)

    thumbnail_max_width = final_image.width - (margins[1] + margins[3])
    thumbnail_max_height = final_image.height - (margins[0] + margins[2])

    thumbnail = image.convert("RGBA")
    thumbnail.thumbnail((thumbnail_max_width, thumbnail_max_height), Image.LANCZOS)

    thumbnail_x = (margins[3] + (thumbnail_max_width - thumbnail.width) // 2)
    thumbnail_y = (margins[0] + (thumbnail_max_height - thumbnail.height) // 2)

    final_image.paste(thumbnail, (thumbnail_x, thumbnail_y), thumbnail)

    return final_image


def render_key_image(deck, icon_filename, font_filename, label_text):
    try:
        icon = Image.open(icon_filename)
    except:
        icon = Image.open(os.path.join(ICON_PATH, "notfound.png"))
        
    image = create_scaled_image(deck, icon, margins=[0, 0, 20, 0])

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_filename, 14)
    label_w, label_h = draw.textsize(label_text, font=font)
    label_pos = ((image.width - label_w) // 2, image.height - 20)
    draw.text(label_pos, text=label_text, font=font, fill="white")

    return PILHelper.to_native_format(deck, image)
