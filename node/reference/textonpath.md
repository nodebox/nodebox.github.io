---
layout: reference
title: Textonpath Node
image: txtonpath
---
Create text that follows a path.

* **Text**: The text to draw.
* **Font**: The font to use for the text.
* **Size**: The font size, in points.
* **Start**: The start position along the path. From 0.00 to 100.00.
* **Loop**: If checked, loops around the path. Due to a bug in NodeBox, this parameter has no effect.
* **Vertical Distance**: The offset distance from the original path. Text is placed according to its baseline.
* **Fill**: The fill color. If the alpha value is 0, the shape will have no fill.
* **Stroke**: The stroke color.
* **Stroke Width**: The stroke width. If the width is 0, the shape will have no stroke.
* **Keep Geometry**: If checked, retains the original input geometry. Otherwise only the text path is output.

Notes
-----
* NodeBox can use any font available on your system. If you share NodeBox documents with others make sure they have the selected font as well. 
* Windows and Mac users have different default fonts installed (Windows users do not have Helvetica installed by default, for example).
