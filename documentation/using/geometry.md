---
layout: documentation
title: Geometry
---
NodeBox works with vector data. Think points, lines and paths instead of pixels.

- **Geometry** is the top level data. All NodeBox nodes take in and return data geometry objects. Even nodes that create a simple path, such as the rect node, still wrap this path in a geometry object.
- Geometry is composed of **paths**. Paths have a **fill and stroke color** and **stroke width**.
- Paths contain **contours**. As an example, the letter "o" is one path composed of two contours: the inner shape and the outer shape. Contours can be **open** or **closed**.
- Contours are made up of  **points** that store the position of the path. A point contains an X, Y coordinate and also a **type**, used for curves.

Scope: Paths, contours and points
---------------------------------
A lot of nodes can operate on paths, contours or points. Here's an example with the wiggle node:

* Create a **textpath** and set its **size** to **150.00**.
* Create a **wiggle** node.
* Connect **textpath1** to **wiggle1**.

Note the scope in the wiggle node:
* When the scope is set to **points** all the points of the textpath are moved randomly.
* When the scope is set to **contours** the different contours, or subpaths, of the textpath are moved. This includes the insides of the letters "e" and "o".
* When the scope is set to **paths**, the whole path moves as a whole.

![Geometry Scope](/media/img/using/geometry-wiggle.png)

Point numbers
-------------
Each point in a path has an index number. You can see these numbers by turning "Point Numbers" on in the viewer.

Here's a simple example:

* Turn "Point Numbers" on in the Viewer pane.
* Create an **ellipse** node.
* Create a **resample** node. Set the **method** to **By Amount** and the **points** to **20**.
* Create a **sort** node.
* Create a **connect** node. Set the **fill** to transparent (alpha value = 0).

Connect them all together: ellipse1 &rarr; resample1 &rarr; sort1 &rarr; connect1.

![Connect Example](/media/img/using/geometry-connect-network.png)

* Set the connect1 node as rendered. Note that the point numbers go clockwise around the circle, from 0 to 20. 
* In sort1, change the **scope** to **Points within geometry** and the **order** to **By X**. 

The viewer now shows this:

![Connect Example Viewer](/media/img/using/geometry-connect-viewer.png)

*What happened?* The connect node connects points of the incoming geometry, in order. By changing the *order* of the points (using the sort node), the shape changes. The points no longer follow the circle in a clockwise direction but are sorted by their X coordinates, in other words, points are sorted from left to right.

By playing with different sort orders you can get some interesting results. Try "Proximity To Point" and dragging the point handle in the viewer. Changing the ellipse to a text path and see what you can come up with (you might want to increase the text size and the number of points in resample).
