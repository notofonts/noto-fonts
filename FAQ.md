# Frequently Asked Questions

### How do I file a bug?

Visit our project’s [bug list](https://github.com/googlei18n/noto-fonts/issues). Please be sure to give as much detail as possible. If it’s a technical issue then list the software and operating system being used as well as versions. If it’s a design issue then images and diagrams are very helpful.


### Is there a discussion group?

Development and user discussions happen on the [noto-font Google Group](https://groups.google.com/d/forum/noto-font).


### When will language or script X be supported by Noto?

We do intend to support all scripts encoded by Unicode. That takes time and the ordering is based on a complex changing mix of factors including but not limited to: complexity of the script, product and project needs, availability of script experts and designers, and number and responsiveness of language reviewers.


### Why did you do a font for script X before script Y?

No matter what order you choose to develop the fonts some scripts will come before others. Think of it like serving a banquet meal for 1000 people. You can either serve the meals as they are ready which means that some will get served before others or you can wait until all the meals are ready before you serve anybody. We’ve taken the approach of serving as each is ready.


### What is the Noto design?

Noto provides pan-language harmony, yet maintains authenticity. The goal is great online readability across languages without losing the character that makes each script special. The intention is to create the equivalent of the stylish yet conservative item of clothing that you can keep in your wardrobe forever rather than the highly stylish item that goes out of style in a single season.


### Who designs Noto?

Google provides the direction, planning, and final aesthetic decisions. We employ and collaborate with “native speakers” with type and design experience and some of the best talent in the font industry to develop fonts for each script to meet the Noto design goals.


### How is a Noto font developed?

Noto fonts for each script are developed in a collaborative approach. We work together with font foundries, design houses, and talented designers to develop requirements for each script and for the languages that use that script. Those requirements then lead to design proposals. We then work with reviewers who are native readers of the languages (for living languages) for which the fonts are being designed (often they are experts in the language or it’s typography) to refine the design proposals. Sometimes this requires working through conflicting design reviews and the careful tweezing out of personal preference. Once the design proposal has been fully vetted, a cycle of font development along with review at each step goes on. How long this takes will vary for each script based on a range of factors including the complexity, number and responsiveness of reviewers, number of glyphs required, and conflicting resource allocation. At the end of all this a technical review of the font is made to hopefully catch any issues. This isn’t foolproof and just like every shipping software system on the planet there will be issues. If you find one then file a bug and we’ll look after it.


### Where are the fonts?

All the Noto fonts are included in this GitHub repository. Exceptions: Noto CJK fonts are in [noto-cjk](https://github.com/googlei18n/noto-cjk); Noto Emoji and Noto Color Emoji are in [noto-emoji](https://github.com/googlei18n/noto-emoji); tools for testing are in [nototools](https://github.com/googlei18n/nototools). Some other source files are available in [noto-source](https://github.com/googlei18n/noto-source).


### Is Noto just a copy of font X?

Noto Sans for Latin was designed by the same person, Steve Matteson, who has worked with us on other Latin script fonts before. Noto Sans for Latin and these earlier designs have some of the same design goals and with the same designer working on them they do share some resemblance.


### What’s the difference between the UI and non-UI versions?

These fonts were initially prepared for use in Android’s UI. They have tighter vertical metrics, and some glyphs that would therefore be clipped are redrawn to fit within the constrained space. They can be used anywhere that has limited vertical space. There are no UI verions of scripts that do not need such adjustment, and the non-UI versions should be preferred for use in body text. 


### What about Han unification?

Whether or not Han unification is a good thing is really a moot point at this time. It’s a fact of life that needs to be worked with when designing fonts or text processing systems for the CJK languages. We are building fonts to be used in systems that exist now and that means working within the frameworks that exist. If somebody would like to change those frameworks then they should get involved with the standards bodies and contribute to the development of the standard and change the direction they are going.

### When will Google support Klingon / Elvish / etc.?

Once Klingon / Elvish / etc. is included in Unicode :). Please [contact the Unicode consortium](http://www.unicode.org/contacts.html) to encourage them to support your favourite invented language.


### How does Noto relate to Droid?

Google’s Droid fonts have been superseded by Noto. Noto began as Droid, and all updates are now made to the Noto fonts. Today, Noto gives better support to all languages covered by Droid, with more characters and fewer bugs, and it covers many more languages.  Both Android and ChromeOS have switched to Noto, and we strongly recommend everyone to replace Droid with Noto. Similarly, the Droid Sans Fallback font is superseded by Noto Sans CJK, available from [noto-cjk](https://github.com/googlei18n/noto-cjk).
