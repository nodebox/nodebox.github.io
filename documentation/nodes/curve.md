---
layout: reference
title: Curve Node
image: curve
---
Create an arbitrary bezier curve or path.

Once you've created a curve node you can draw in the viewer:

* Click to create straight points.
* Click and drag to create curve points.
* You can click on a point you've created to select it. Drag the point or its control handles to move them. Click the "x" to remove the point.
* Click the last point and press the "pause" button to stop editing. Click again in the viewer to start a new path segment.

<!-- This line is here to make Markdown happy -->

* **Path**: The coordinates of the path. Don't manipulate these yourself: just draw the curve in the viewer and let NodeBox manage the underlying data. Use the "Revert to Default" option to clear the curve.
* **Fill**: The fill color. If the alpha value is 0, the shape will have no fill.
* **Stroke**: The stroke color.
* **Stroke Width**: The stroke width. If the width is 0, the shape will have no stroke.

Notes
-----
* The *actual* amount of points is twice the amount specified in the points parameter. For each *outer* point, star also needs to create an inner point.
* Inner and outer diameter can be reversed.