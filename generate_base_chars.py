# load your font, etc…
font = fontforge.open("font_name.otf")

chara = ["a", "b", "c",  "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "y", "adieresis", "odieresis"]


chara2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W", "Y", "Adieresis", "Odieresis"]

for x in chara:
    
    ligature_name = x + ".top"
    glyph = font.createChar(-1, ligature_name)
    pen = font[ligature_name].glyphPen(replace=False);
    font["hyphen"].draw(pen);
    pen = None;
    glyph.width = 2048
    
    ligature_name = x + ".bottom"
    glyph = font.createChar(-1, ligature_name)
    pen = font[ligature_name].glyphPen(replace=False);
    font["hyphen"].draw(pen);
    pen = None;
    glyph.width = 2048
   
    ligature_name = x + ".left"
    glyph = font.createChar(-1, ligature_name)
    pen = font[ligature_name].glyphPen(replace=False);
    font["hyphen"].draw(pen);
    pen = None;
    glyph.width = 2048
   
    ligature_name = x + ".top2"
    glyph = font.createChar(-1, ligature_name)
    pen = font[ligature_name].glyphPen(replace=False);
    font["hyphen"].draw(pen);
    pen = None;
    glyph.width = 2048
 
    ligature_name = x + ".bottom2"
    glyph = font.createChar(-1, ligature_name)
    pen = font[ligature_name].glyphPen(replace=False);
    font["hyphen"].draw(pen);
    pen = None;
    glyph.width = 2048

for y in chara2:
    
    ligature_name = y + ".top"
    glyph = font.createChar(-1, ligature_name)
    pen = font[ligature_name].glyphPen(replace=False);
    font["hyphen"].draw(pen);
    pen = None;
    glyph.width = 2048
    
    ligature_name = y + ".bottom"
    glyph = font.createChar(-1, ligature_name)
    pen = font[ligature_name].glyphPen(replace=False);
    font["hyphen"].draw(pen);
    pen = None;
    glyph.width = 2048
 

