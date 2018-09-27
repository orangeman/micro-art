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
            (50, 0, s.size[0]/2 - 50, s.size[1])))
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
