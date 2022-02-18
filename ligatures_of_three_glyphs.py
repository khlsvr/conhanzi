# load your font, etc…
font = fontforge.open("font_name.otf")

left = ["a", "b", "c",  "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "y", "adieresis", "odieresis", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W", "Y", "Adieresis", "Odieresis"]
top2 = ["a", "b", "c",  "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "y", "adieresis", "odieresis"]
bottom2 = ["a", "b", "c",  "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "y", "adieresis", "odieresis"]


for x in left:
  for y in top2:
    for z in bottom2:

        ligature_name = x + "_" + y + "_" + z
        ligature_tuple = (x, y, z)
        glyph = font.createChar(-1, ligature_name)
        # split ligatures to multiple subtables to avoid max limit ~10000 exceeding
        if x in ("a", "b", "c", "d", "e"):
            glyph.addPosSub('ligatureshi10', ligature_tuple)
        elif x in ("f", "g", "h", "i", "j", "k"):
            glyph.addPosSub('ligatureshi11', ligature_tuple)
        elif x in ( "l", "m", "n", "o", "p", "r"):
            glyph.addPosSub('ligatureshi3', ligature_tuple)
        elif x in ("s", "t", "u", "v", "w", "y"):
            glyph.addPosSub('ligatureshi4', ligature_tuple)
        elif x in ("adieresis", "odieresis", "L", "M", "N"):
            glyph.addPosSub('ligatureshi5', ligature_tuple)
        elif x in ("O", "P", "R", "S", "T"):
            glyph.addPosSub('ligatureshi6', ligature_tuple)
        elif x in ("A", "B", "C", "D", "E"):
            glyph.addPosSub('ligatureshi7', ligature_tuple)
        elif x in ("F", "G", "H", "I", "J", "K"):
            glyph.addPosSub('ligatureshi8', ligature_tuple)
        else:
            glyph.addPosSub('ligatureshi9', ligature_tuple)
        
        pen = font[ligature_name].glyphPen(replace=False);		# Create a pen to draw into glyph
        font[x + ".left"].draw(pen);
        font[y + ".top2"].draw(pen);
        font[z + ".bottom2"].draw(pen);
        pen = None;
        glyph.width = 2048

