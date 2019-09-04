import json, markovify, random, textwrap
from PIL import Image, ImageFont, ImageDraw


#Load pre-trained Markov data from JSON.
with open("markov.json") as f:
    markov = markovify.Text.from_json(json.load(f))
    f.close()

#Load image files.
img = Image.open("template.png")
bubble = Image.open("bubble.png")

#Pick which of the four panels will contain text.
panelx = [220, 560, 910, 1250]
random.shuffle(panelx)
text_panelx = panelx[0:random.randint(1,2)]
text_panelx.sort()

#For each panel with text...
font = ImageFont.truetype("font.otf", 19)
for x in text_panelx:

    #Paste a speech bubble on each panel with text.
    img.paste(bubble, (x, 35), bubble)

    #Generate text from Markov model and wrap it within bounds of bubble.
    text = markov.make_short_sentence(60)
    lines = textwrap.wrap(text, 15)

    #Superimpose text on image.
    draw = ImageDraw.Draw(img)
    for i, ln in enumerate(lines):
        draw.text((x + 18, 70 + (18 * i)), ln, (0, 0, 0), font = font)

#Save image file.
img.save("comic.png")
