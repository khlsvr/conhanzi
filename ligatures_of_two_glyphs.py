# load your font, etc…
font = fontforge.open("font_name.otf")

top = ["a", "b", "c",  "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "y", "adieresis", "odieresis", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W", "Y", "Adieresis", "Odieresis"]
bottom = ["a", "b", "c",  "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "y", "adieresis", "odieresis"]


for x in top:
  for y in bottom:

    ligature_name = x + "_" + y
    ligature_tuple = (x, y)
    glyph = font.createChar(-1, ligature_name)
    if x in ("a", "b", "c",  "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "y", "adieresis", "odieresis"):
        glyph.addPosSub('ligatureshi', ligature_tuple)
    else:
        glyph.addPosSub('ligatureshi2', ligature_tuple)
    
    pen = font[ligature_name].glyphPen(replace=False);
    font[x + ".top"].draw(pen);
    font[y + ".bottom"].draw(pen);
    pen = None;
    glyph.width = 2048

