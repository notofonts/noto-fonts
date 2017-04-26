## Defect Report
Use this template for filing a defect report. For feature requests and other matters, you can use part of the template and delete what you don't need.

### Title 
  > Should be brief but contain essential information.

### Font 
  > Full file name, for example 'NotoSansArmenian-Regular.ttf'.
  > You can upload the problem font here unless it is a Chinese, Japanese or Korean font (these are large).

### Where the font came from, and when
  > For example:
  >   Site: https://noto-website-2.storage.googleapis.com/pkgs/NotoSansArmenian-hinted.zip
  >   Date: 2017-04-10 (preferred format)

### Font Version
  > * Mac - right mouse click on a font and try Preview to see version info.
  > * Win -- right mouse click on a font (Local Disc > Windows > Fonts) and see version info on Properties.
  > * Linux -- use (Gnome) Font Viewer: open a font and click on Info tab.

### OS name and version
  > This is especially important if the font came pre-installed.

### Application name and version
  > If the issue is observed using a specific app.

### Issue
  > Summarize the issue briefly -- one paragraph preferred

  1. Steps to reproduce
  2. Observed results
  3. Expected results
  4. Additional information 
  > Unicode chart, technical specs, shaping info, comparison with non-Noto fonts, comparison with earlier version of the same font (regression cases)

### Character data
  > Please include real character data to illustrate your issue-- Unicode codepoints are helpful.  This makes it possible for developers who don't know the language or script to copy/paste the text to reproduce the issue.

### Screenshot
  > If possible, include a screenshot or an image illustrating the issue.
  > Annotations are also helpful.


## Tools for reporting bugs
  Useful tools for reporting bugs are available at: https://github.com/googlei18n/
  
### Harfbuzz hb-view and hb-shape
  These are part of the HarfBuzz distribution and can help isolate if an issue is in the app/OS, shaping engine, or font.
  * hb-view renders the text with the exact font (for example, to see how ligatured characters shape) using your installed version of HarfBuzz.

For example:
```
  hb-view --font-file {path to font} --text-file {path to text file} --output-file '{sample}.png'
```


* hb-shape shows glyph selection and positioning

### Fontview
  * Fontview displays the text.

### Fontdiff
  * Fontdiff displays the text using two versions of the font side by side.
