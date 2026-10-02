import sys
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
site,out=sys.argv[1],sys.argv[2]
for src,name,w in [("big-shoulders-display-latin","bs900",900),("big-shoulders-display-latin","bs800",800),("inter-latin","inter500",500)]:
    f=TTFont(f"{site}/fonts/{src}.woff2"); f.flavor=None
    inst=instantiateVariableFont(f,{"wght":w},updateFontNames=False); inst.save(f"{out}/{name}.ttf"); print(name,"ok")
