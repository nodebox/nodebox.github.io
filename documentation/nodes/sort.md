---
layout: reference
title: Sort Node
image: sort
---
Changes the order of points or paths using different sorting methods. The [geometry documentation page](../using/geometry.html) explains the use for sorting elements.

* **Scope**: The sorting scope:
  * *Paths within geometry*: Sort draw order of paths within the geometry retaining path geometries and color information.
  * *Points within geometry*: Sorts all available points discarding path geometries and color information. When using geometry as templates you'd want to select this.
  * *Points within a contour*: Sort points within each contour retaining path geometries and color information.
  * *Points within a path*: Sort points within each path discarding path geometries but retaining color information.
  * *Contours within a path*: Sort draw order of contours within each path retaining path geometries and color information.
* **Order**: The sorting method:
  * *Unchanged*: Does not change the sort order.
  * *By X*: Sort based on the X coordinates from left to right.
  * *By Y*: Sort based on the Y coordinates from top to bottom.
  * *Random*: Randomly shuffle the elements. Use the Seed to choose a different variation.
  * *Reversed*: Reverse the ordering of the elements.
  * *Shift*: Shift the ordering so elements at the end of the elements are moved to the front.
  * *Proximity To Point*: Sort elements based on their closeness to the given coordinate.
  * *Angle To Point*: Sort elements based on the angle of the given coordinate.
* **Seed**: For random sorting, the [random seed](../using/randomness.html).
* **Offset**: For shift sorting, the shifting offset. This value wraps around.
* **X**: For proximity / angle to point, the X coordinate.
* **Y**: For proximity / angle to point, the Y coordinate.
