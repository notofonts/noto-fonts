* Use this template for filing a defect report. For feature requests and other matters, you can use part of the template and delete what you don't need.
* Title (should be brief but contain essential information -- delete this line once Title is added)

* Font name (full name, e.g. NotoSansArmenian-regular.ttf). You can upload the problem font here unless it is a Chinese, Japanese or Korean font.

* Where you downloaded the font file and when, e.g.

Site: https://noto-website-2.storage.googleapis.com/pkgs/NotoSansArmenian-hinted.zip
Date: 2017-04-10 (preferred format)
Note: Write the OS version and build ID if the font is pre-installed on an OS (usually available in the Settings apps)

* Version info (or OS version and build if the font is pre-installed in a build)

  * Mac - right mouse click on a font and try Preview to see version info
  * Win -- right mouse click on a font (Local Disc > Windows > Fonts) and see version info on Properties
  * Linux -- use (Gnome) Font Viewer: open a font and click on Info tab

* Your OS name and version

* Application name (and version if know)  if an issue is observed on a specific app

* Issue summary (if you are filing a defect report)

(Summarize the issue briefly -- one paragraph preferred.)

  1. include reproduction steps: Step 1. …, Step 2. …, etc.
  2. Observed results
  3. Expected results
  4. Other relevant information (Unicode chart, technical specs, shaping info, comparison with non-Noto fonts, comparison with earlier version of the same font (regression cases)

* Include real characters data to illustrate your issue -- Unicode codepoints are helpful
Developers who might not know the language/script can copy/paste the text to reproduce the issue.

* Include a screenshot or an image illustrating the issue -- added annotations are very helpful

  * You can use use tools like hb-view (to see graphically how ligatured characters shape) and hb-shape (to convert strings into positioned glyphs). They are part of HarfBuzz distribution and can help isolate if an issue is in an app/OS, shaping engine or in the font.  
  * You can use Fontview to attach an screenshot how a sample text displays. If you want to show how 2 versions of the same fonts differ in display of the same text, you can use Fontdiff.

Note: These tools are all available at: https://github.com/googlei18n/
