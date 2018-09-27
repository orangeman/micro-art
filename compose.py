import os
from PIL import Image

def breite(streifen):
    breite = 0
    for s in streifen:
        breite += s.size[0]
    return breite

def cropped(streifen):
    cropped = []
    for s in streifen:
        cropped.append(s.crop(
            (50, 0, 2098-100, 15000)))
    return cropped

def compose(streifen):
    offset = 0
    comp = Image.new('I;16',
        (breite(streifen), 15000))
    for s in streifen:
        print("stitching ", s.size)
        comp.paste(s, (offset, 0))
        offset += s.size[0]
    return comp


streifen = []
for f in sorted(os.listdir("./try2")):
    # if f.startswith("ju") and not f.startswith("juf"):
    if f.startswith("juf"):
        streifen.append(Image.open("./try2/" + f))
        print("choosing", f)

composite = compose(cropped(streifen))

composite.save("./composite.tif")
os.system("xviewer composite.tif")
# os.system("display foo.tif")
