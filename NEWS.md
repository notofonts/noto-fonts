November 06, 2018

New and updated fonts
=====================

We're releasing new fonts to support Music and the following scripts: Ahom,
Bassa Vah, Bhaiksuki, Caucasian Albanian, Duployan, Grantha, Gurmukhi,
Hatran, Khudawadi, Linear A, Mahajani, Manichaean, Marchen, Mende Kikakui,
Miao, Modi, Mro, Multani, Nabataean, Newa, Old Hungarian, Old North Arabian,
Old Permic, Pahawh Hmong, Palmyrene, Pau Cin Hau, Psalter Pahlavi, Sharada,
Sora Sompeng, Takri, Tamil Slanted, Tibetan, Tirhuta, and Warang Citi.

We're releasing updated versions of about 108 Noto families for about 90 scripts,
built from sources using our open source pipeline.  Many of these have
additional weights, and some have multiple widths as well: Sans Kannada,
Sans Malayalam and Serif Sinhala now have 36 styles, Serif Kannada now has 9 styles.
A single font family Noto Sans Syriac replaced all three existing Syriac fonts.

Some number of families have not yet been updated, we will get to those as the
phase 3 work continues.  Others are obsoleted by newer designs.  We will
eventually move the fonts that will not get new updates to a new location to
more clearly distinguish them.

The new fonts, although .ttf, are built on a 1000 upem grid.  This means they
cannot be merged with the older fonts built with the standard ttf 2048 upem.
This is a problem for those who wish to build a single font file from multiple
Noto fonts.  Eventually this will improve, for now our apologies.  We are also
looking at other packaging to make using the fonts easier.

September 19, 2017

Phase 3 font update
===================

We're releasing updated versions of about 75 Noto families, built from sources
using our open source pipeline.  Many of these have additional weights, and some
have multiple widths as well.  The result is the number of font files has
increased about 10x over the previous set.

Most of the new fonts follow the original designs, but a few are new designs.

A number of families have not yet been updated, we will get to those as the
phase 3 work progresses.  Others are obsoleted by newer designs.  We will
eventually move the fonts that will not get new updates to a new location to
more clearly distinguish them.

The new fonts, although .ttf, are built on a 1000 upem grid.  This means they
cannot be merged with the older fonts built with the standard ttf 2048 upem.
This is a problem for those who wish to build a single font file from multiple
Noto fonts.  Eventually this will improve, for now our apologies.  We are also
looking at other packaging to make using the fonts easier.


September 29, 2015

All Noto fonts now licensed under Open Font License 1.1
=======================================================

With the new release we have moved from Apache 2.0 to Open Font License 1.1 (OFL 1.1).  We
are making this change because it makes it easier for you, the end users of Noto, to use
the fonts that we produce.  When we first released the Noto fonts the OFL license was
still a bit of an unknown entity and the Apache license looked familiar to us.  Over the
years the OFL license has become the most commonly used and understood license to use for
open source fonts.

All of our fonts going forward from this release will be available only under the OFL
license.  If you still want the fonts under the Apache license you can get them from the
repo using the tag 'v2015-09-29-license-apache'.  However, new fonts and updates to
existing fonts will use the OFL license.
