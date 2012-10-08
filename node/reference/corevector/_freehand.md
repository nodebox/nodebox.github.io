---
layout: reference
title: Freehand Node
image: freehand
---
Draw lines directly on the canvas.

* **Path**: The coordinates of the path. Don't manipulate these yourself: just draw in the viewer and let NodeBox manage the underlying data. Use the "Revert to Default" option to clear the path.
* **Fill**: The fill color. If the alpha value is 0, the shape will have no fill.
* **Stroke**: The stroke color.
* **Stroke Width**: The stroke width. If the width is 0, the shape will have no stroke.

Notes
-----
* You can draw multiple segments.
* Undo undoes the last segment you've drawn, not the whole path.