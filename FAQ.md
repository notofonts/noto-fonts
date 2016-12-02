# Frequently Asked Questions

### What does Noto mean?

When text is rendered by a computer, sometimes characters display as little boxes because your device doesn't have a font that has images for them— these boxes are known as “tofu.”  The name Noto is to convey Google’s goal that users see “**no** more **to**fu.”


### How do I file a bug?

Visit our project’s [bug list](https://github.com/googlei18n/noto-fonts/issues). Please be sure to give as much detail as possible. If it’s a technical issue then list the software and operating system being used as well as versions. If it’s a design issue then images and diagrams are very helpful.


### How do I contribute?

Clone the repositories, try out the fonts, and report bugs. If you wish to contribute tools, please fill out the contributor's agreement which you'll find in the tools repositories.  See below for the various repositories.


### Where are the fonts?

The fonts are in multiple repositories.

* Most of the Noto fonts are in [this GitHub repository](https://github.com/googlei18n/noto-fonts).
* Noto CJK fonts are in [noto-cjk](https://github.com/googlei18n/noto-cjk).
* Noto Emoji and Noto Color Emoji are in [noto-emoji](https://github.com/googlei18n/noto-emoji).

The comprehensive set of Noto fonts and tools are available in [these GitHub repositories](https://github.com/googlei18n?query=noto).


### Is there a discussion group?

Development and user discussions happen on the [noto-font Google Group](https://groups.google.com/d/forum/noto-font).


### What writing systems does Noto support?

As of September 2016, Noto fonts support all scripts/writing systems defined in Unicode 6.1.
* For all major living scripts, Noto provides two weights (regular and bold) and both UI and non-UI fonts. UI fonts are for text display in UI elements (e.g. buttons, menus) that have a height limit.
* For many major living scripts, Noto provides multiple typeface styles. For example, there are sans-serif and serif styles for Latin, Greek, Cyrillic, Indic (Devanagari, Tamil, Telugu etc), Armenian, Georgian, Thai, Khmer, and Lao; Naskh and Kufi styles for Arabic; and Eastern, Western, Estrangela styles for Syriac.
* For many major living scripts, Noto includes both hinted and unhinted fonts: hinted fonts for Windows and Linux, and unhinted fonts for Android and Mac. (Note however that NotoSansSymbols is unhinted).
* For historical scripts, Noto has unhinted fonts with one weight (regular).


### The hinted version of the font is missing

If your favorite font is in the Noto's unhinted directory, but is missing from the [hinted directory](https://github.com/googlei18n/noto-fonts/tree/master/hinted), first please check [noto-hinted](https://github.com/lemzwerg/noto-hinted). It might be already there. If it is not there, then you can help to make it by running the hinting process using [ttfautohint](https://www.freetype.org/ttfautohint/). The process is described in the [noto-hinted README](https://github.com/lemzwerg/noto-hinted/blob/master/README.md).  Note however that this tool does not work on all scripts, and in particular, not on many of the living scripts we do not provide hinted veresions for.  Please see [extending ttfautohint with new wscripts](https://www.freetype.org/ttfautohint/doc/ttfautohint.html#extending-ttfautohint-with-new-scripts) on the freetype website if you are so inclined.


### What are Google's plans for Noto (so called "Phase 3")?
* We plan to extend character/script coverage to cover 100% of Unicode 9.0 except for CJK. For CJK, we plan to cover Plane 0 (BMP) CJK characters in Unicode 9.0
* We plan to extend Noto from two weights (regular and bold) and one width to a number of weights (thin to heavy) and a number of widths (condensed to normal). 
* we plan to open source glyph and other source data for all Noto fonts (except CJK fonts whose source is owned by Adobe), and provide a pipeline to build binary fonts from these sources. With the font sources and pipeline, everyone can build their own fonts and use Noto as the base font for free.


### When will language or script X be supported by Noto?

We do intend to support all scripts encoded by Unicode. That takes time and the ordering is based on a complex changing mix of factors including but not limited to: complexity of the script, product and project needs, availability of script experts and designers, and number and responsiveness of language reviewers.


### Why did you do a font for script X before script Y?

No matter what order you choose to develop the fonts some scripts will come before others. Think of it like serving a banquet meal for 1000 people. You can either serve the meals as they are ready which means that some will get served before others or you can wait until all the meals are ready before you serve anybody. We’ve taken the approach of serving as each is ready.


### What is the Noto design?

Noto provides pan-language harmony, yet maintains authenticity. The goal is great online readability across languages without losing the character that makes each script special. The intention is to create the equivalent of the stylish yet conservative item of clothing that you can keep in your wardrobe forever rather than the highly stylish item that goes out of style in a single season.


### Who designs Noto?

Google provides the direction, planning, and final aesthetic decisions. We employ and collaborate with “native speakers” with type and design experience and some of the best talent in the font industry to develop fonts for each script to meet the Noto design goals.


### How is a Noto font developed?

Noto fonts for each script are developed in a collaborative approach. We work together with font foundries, design houses, and talented designers to develop requirements for each script and for the languages that use that script. Those requirements then lead to design proposals. We then work with reviewers who are native readers of the languages (for living languages) for which the fonts are being designed (often they are experts in the language or its typography) to refine the design proposals. Sometimes this requires working through conflicting design reviews and the careful tweezing out of personal preference. Once the design proposal has been fully vetted, a cycle of font development along with review at each step goes on. How long this takes will vary for each script based on a range of factors including the complexity, number and responsiveness of reviewers, number of glyphs required, and conflicting resource allocation. At the end of all this a technical review of the font is made to hopefully catch any issues. This isn’t foolproof and just like every shipping software system on the planet there will be issues. If you find one then file a bug and we’ll look after it.


### Is Noto just a copy of font X?

Noto Sans for Latin was designed by the same person, Steve Matteson, who has worked with us on other Latin script fonts before. Noto Sans for Latin and these earlier designs have some of the same design goals and with the same designer working on them they do share some resemblance.


### What’s the difference between the UI and non-UI versions?

The UI fonts were initially prepared for use in Android’s UI. They have tighter vertical metrics, and some glyphs that would be clipped are redrawn to fit within the constrained space. They can be used anywhere that has limited vertical space. There are no UI verions of scripts that do not need such adjustment, and the non-UI versions should be preferred for use in body text. 


### What about Han unification?

Whether or not Han unification is a good thing is really a moot point at this time. It’s a fact of life that needs to be worked with when designing fonts or text processing systems for the CJK languages. We are building fonts to be used in systems that exist now and that means working within the frameworks that exist. If somebody would like to change those frameworks then they should get involved with the standards bodies and contribute to the development of the standard and change the direction they are going.


### When will Google support Klingon / Elvish / etc.?

Once Klingon / Elvish / etc. is included in Unicode :). Please [contact the Unicode consortium](http://www.unicode.org/contacts.html) to encourage them to support your favourite invented language.


### How does Noto relate to Droid?

Google’s Droid fonts have been superseded by Noto. Noto began as Droid, and all updates are now made to the Noto fonts. Today, Noto gives better support to all languages covered by Droid, with more characters and fewer bugs, and it covers many more languages.  Both Android and ChromeOS have switched to Noto, and we strongly recommend everyone to replace Droid with Noto. Similarly, the Droid Sans Fallback font is superseded by Noto Sans CJK, available from [noto-cjk](https://github.com/googlei18n/noto-cjk).


### Could you provide a single font file that covers every language (or at least as many scripts as possible)?	

A single file is not possible, because there are many more glyphs in Noto than can fit into a single font. CJK alone is as large as it can get. In addition, different scripts prefer different line metrics. Noto tries to provide suitable line metrics for each script rather than forcing all scripts to fit one. The UI fonts are an exception to this, however, so using them we could generate a single font sharing a single line height. However, we are working on a possible repackaging of the fonts into a few files. We can probably get one for CJK, one for common scripts in living languages, and one for obscure scripts-- depends if Tangut pushes us over the limit of what non-CJK we can fit into a single font. There are tools that can be used to merge fonts but the devil is in the details-- some common characters are in a few source fonts and if they behave differently we'd have to work that out.


### Are there any Noto YouTube videos I could share with others?

Some of the videos on Noto which one can find on YouTube are
* [Creating Noto for Google](https://www.youtube.com/watch?v=16_NYHUZ1kM)
* [Google’s International Fonts Noto — One Font to Rule Them All](https://www.youtube.com/watch?v=AAzvk9HSi84)
