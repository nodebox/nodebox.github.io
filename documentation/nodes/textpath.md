---
layout: reference
title: Textpath Node
image: textpath
---
Create a text path.

* **Text**: The text to draw.
* **Font**: The font to use for the text.
* **Size**: The font size, in points.
* **Align**: The text alignment. This is relative to the [origin][] unless a width is set.
* **X**: The X coordinate.
* **Y**: The Y coordinate of the **baseline** of the first line of text.
* **Width**: The width of the text. Any value bigger than 0 wraps the text. 
* **Height**: The height of the text. Not used.
* **Fill**: The fill color. If the alpha value is 0, the shape will have no fill.
* **Stroke**: The stroke color.
* **Stroke Width**: The stroke width. If the width is 0, the shape will have no stroke.

Notes
-----
* NodeBox can use any font available on your system. If you share NodeBox documents with others make sure they have the selected font as well. 
* Windows and Mac users have different default fonts installed (Windows users do not have Helvetica installed by default, for example).

[origin]: /documentation/using/coordinates.html