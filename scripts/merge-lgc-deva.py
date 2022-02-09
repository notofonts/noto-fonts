from fontTools.ttLib import TTFont
from fontTools.merge import Merger
from tempfile import NamedTemporaryFile
from gftools.fix import fix_family
import glob
import re

NAME_13 = "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL"

def fix_up_glyph_names(font):
	# Requires compiling a bunch of the tables, easiest to save/reload
	with NamedTemporaryFile() as ntf:
		font.save(ntf.name)
		font = TTFont(ntf.name)

	# Fixup glyph names.
	mapping = {x: x.replace("#","_") for x in font.getGlyphOrder()}
	mapping[".notdef#1"] = "_notdef_1"
	neworder = [mapping[x] for x in font.getGlyphOrder()]
	font.setGlyphOrder(neworder)
	font["glyf"].glyphOrder = neworder
	font["glyf"].glyphs = {mapping.get(k,k):v for k,v in font["glyf"].glyphs.items()}
	font["hmtx"].metrics = {mapping.get(k,k):v for k,v in font["hmtx"].metrics.items()}
	return font

def fixup_various(font):
	# Vertical metrics
	font["OS/2"].sTypoAscender = font["hhea"].ascender = 1069
	font["OS/2"].sTypoDescender = font["hhea"].descender = -293
	# Missing glyphs for GF Latin Core
	for cmap in font["cmap"].tables:
		cmap.cmap[0x2215] = cmap.cmap[0x2f]  # Division sign <- solidus
		if 0x2212 not in cmap.cmap:
			cmap.cmap[0x2212] = cmap.cmap[0x2d]  # Minus sign <- hyphen-minus
	# name ID 13
	font["name"].setName(NAME_13, 13, 3, 1, 0x409)

LGC = glob.glob("../source/output/Noto Sans/unhinted/ttf/*.ttf")
DEVA = glob.glob("unhinted/ttf/NotoSansDevanagari/*.ttf")

styles = {}

for filename in LGC:
	style = re.search("-(.*?).ttf", filename)[1]
	styles[style] = { "lgc": filename }

for filename in DEVA:
	style = re.search("-(.*?).ttf", filename)[1]
	if style in styles:
		styles[style]["deva"] = filename

outfonts = {}

for style, files in styles.items():
	# Skip the condensed
	if "Condensed" in style or "Display" in style:
		continue
	print("Merging %s" % style)
	if "deva" in files:
		outfont = Merger().merge([files["lgc"], files["deva"]])
		outfonts[style] = fix_up_glyph_names(outfont)
	else:
		ttfont = outfonts[style] = TTFont(files["lgc"])
		# Just keep 3-1-0 cmap
		ttfont["cmap"].tables = [ x for x in ttfont["cmap"].tables if x.platformID == 3]


print("Fixing")
fix_family(list(outfonts.values()),include_source_fixes=True)

for style, outfont in outfonts.items():
	output = "merged/NotoSans-%s.ttf" % style
	fixup_various(outfont)
	print("Saving %s" % style)
	outfont.save(output)

