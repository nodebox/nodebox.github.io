---
layout: reference
title: Star Node
image: star
---
Create a star shape.

* **X**: The X coordinate.
* **Y**: The Y coordinate.
* **Points**: The amount of outer points on the star.
* **Outer Diameter**: The diameter of the outer points.
* **Inner Diameter**: The diameter of the inner points.
* **Fill**: The fill color. If the alpha value is 0, the shape will have no fill.
* **Stroke**: The stroke color.
* **Stroke Width**: The stroke width. If the width is 0, the shape will have no stroke.

Notes
-----
* The *actual* amount of points is twice the amount specified in the points parameter. For each *outer* point, star also needs to create an *inner* point.
* Inner and outer diameter can be reversed.