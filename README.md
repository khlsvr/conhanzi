# Conhanzi

A constructed alphabetic writing system

## Overview

Conhanzi script is an alternate alphabetic writing system for languages using the Latin script. Conhanzi is inspired by Chinese and Korean. Conhanzi combines every combination of two or three alphabets into a ligature, consisting a total of 32 500 ligatures.

![conhanzi](/static/conhanzi-eng-wiki-example_900x487.png)

The English Wikipedia page "Radical (Chinese characters)" using the conhanzi font.

## The Chinese radicals

The selection process for the glyphs was mostly based on the pronounciation of the Chinese characters in languages they are used, mostly the initial phonemes associated with the character.

![conhanzi_glyphs](/static/conhanzi-parts_900x165.png)

## How it works

The ligatures are constructed systematically in such that for example a word `ligature` would include a ligature of `lig` followed by a ligature `atu` followed by a ligature of `re`. The alphabet set used in ligatures in this initial version is inclined towards the Finnish, including glyphs and ligatures for the `ä` and `ö` and excluding ligatures for `q`, `x` and `z`. Thus the word `Conhanzi` turns out to be constructed from `Con` + `han` + `z` + `i` glyphs. Capital letters can only appear at the beginning of a ligature.

## Constructing the glyphs

The ligature glyphs are constructed in such way that in a three letter combination the first letter is on the left side of the glyph, the second letter is on the top right, and the third letter is on bottom right. In two letter combinations the first letter is on top and and the second below it.  
  
The letters in ligature glyphs are in set positions and thus generating the ligatures to a font file was fully automated with a program. 

### Construction process

The font construction was done using Fontforge with the help of its script execution feature to automate ligature generation.   

* Instead of a new empty font project, the font work was done on top of a [Code New Roman](https://aur.archlinux.org/packages/otf-code-new-roman) font. Every glyph in that font was transformed to 2048 width, which seems to be more suitable for Chinese characters. 

* Suitable versions of letters were created as their own glyphs the following way: Every letter has a version for position 1, position 2 and position 3 in a three letter combination ligature glyph and versions for positions 1 and 2 on a two letter combination ligature glyph, thus requiring 5 extra glyphs. For the letter `a` for example `a.top`, `a.bottom`, `a.left`, `a.top2` and `a.bottom2` was created. A script [generate_base_chars.py](generate_base_chars.py) was used to automate the generation of these glyphs. A hyphen was inserted as a placeholder for some testing purposes (still present in the generation script provided). After the automated glyph generation, the actual work for creating the appearance of these glyphs was done. The [IPA Gothic](https://archlinux.org/packages/community/any/otf-ipafont/) font was used to copy, paste and modify the selected Chinese radical parts to these glyphs.

* The necessary table and subtables were created for ligatures by executing the contents of the [generate_tables.py](generate_tables.py) from `File -> Execute Script`. Because of a high number of ligatures, creating multiple subtables was necessary to avoid reaching the max limit. [source](https://github.com/fontforge/fontforge/issues/4416).

* The ligatures were created programmatically by iterating through every combination copying the contents of the desired versions of the letters to the glyphs. To copy every three letter combination the contents of the script [ligatures_of_three_glyphs.py](ligatures_of_three_glyphs.py) was executed from the `File->Execute Script` and [ligatures_of_two_glyphs.py](ligatures_of_two_glyphs.py) similarly for the two letter combinations.

## Tips & Tricks

To use the font on-demand on any website, it is possible to create a shortcut key to toggle the font the website provides and the conhanzi (or whatever) font.  

One way to do that in Qutebrowser: After having installed the font to your system create empty.css with no content and toggle_font.css with the content ` * { font-family: "conhanzi" !important; font-size: 1.1rem; }` and place them in the Qutebrowser's config dir. Add a line to the Qutebrowser's config file with the content `config.bind('css', 'config-cycle content.user_stylesheets toggle_font.css empty.css')` to toggle the font with the key binding `css`.   

Same can be achieved in other web browsers too. For example the dotsies website provides a "bookmarklet" method for this. There are probably other ways to do it too.  

To use the font properly in other applications make sure the application supports ligatures in fonts.  

## Legality

Because two (free) fonts namely [IPA Gothic](https://archlinux.org/packages/community/any/otf-ipafont/) and [Code New Roman](https://aur.archlinux.org/packages/otf-code-new-roman) were used in making this font, although heavily modified, I'm not sure whether it is allowed to share the conhanzi font file here. Please let me know if I'm not allowed to share the font file here.


