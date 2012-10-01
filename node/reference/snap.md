---
layout: reference
title: Snap Node
image: snap
---
Snap geometry to a grid.

The snap node aligns each individual point of the geometry to the grid.

* **Distance**: The size of the grid.
* **Strength**: The strength of the "attraction" to the grid. At 0.00, points are not snap to the grid at all. At 100.0, points are fully snapped to the grid.
* **X**: The grid X offset.
* **Y**: The grid Y offset.

Notes
-----
* Snap also snaps curve points to the grid. This means that curves can look funny. If you want straight lines, use snap in combination with [resample](resample.html) which converts a curve straight lines.