import os
from compose import *


streifen = []
for f in sorted(os.listdir("./try2")):
    # if f.startswith("ju") and not f.startswith("juf"):
    if f.startswith("juf"):
        streifen.append(Image.open("./try2/" + f))
        print("choosing", f)

composite = compose(cropped(streifen))

composite.save("./composite.tif")
# os.system("xviewer composite.tif")
# os.system("display composite.tif")
