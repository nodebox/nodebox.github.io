---
layout: documentation
title: Coordinate System
---
NodeBox works in 2 dimensions. The x dimension goes from left to right. The y dimension goes from top to bottom. The y axis is thus pointed down.

A point in NodeBox space is represented as x, y. For example, the point 30,40 would be located 30 points from the left and 40 points from the top of the origin.

The **origin** is the center of the canvas, point 0,0. All objects in NodeBox are centered around the origin. You can show the origin in the viewer pane by checking the "Origin" box at the top.

When you create a new shape in NodeBox, it will be centered on the origin. As an example, let's create a rectangle. In the viewer, turn the origin on. Note that if we drag the width or height, the object stays centered.

The origin is an important concept because it underlies the functionality of many nodes:


The Transform Node
------------------
The transform node uses the origin to scale and rotate every object around.

* Create a new document and turn the **origin** on in the viewer.
* Create a **rect** node. Set its **x** to **100.00**.
* Create a **transform** node.
* Connect **rect1** to **transform1**.
* In **transform1**, drag the **rotation** to **225.00**.

Note that the rectangle doesn't rotate around its center – it rotates around the origin. The same happens for scale, although the effect is much less notable.

![Function of the origin point in Transform node](/media/img/using/coordinates-transform.png)

The Place Node
--------------
The place node moves object a relative amount from the origin to the template point. It doesn't take the actual bounding box of the object into account.

Here's an example:

* Create a **rect** node. Set its **width** and **height** to **10.00**.
* Create an **ellipse** node. Make its **fill** color semi-transparent (alpha=100) 
* Create a **resample** node. Set the **method** to **"By Amount"** and the **amount** to **20**.
* Connect **ellipse1** to **resample1**. 
* Create a **place** node. 
* Connect **resample1** to **place1**'s **template** port.
* Connect **rect1** to **place1**'s **shape** port.
* Create a **merge** node.
* Connect **place1** to **merge1**.
* Connect **ellipse1** to **merge1**.

Note that each rectangle is centered along the edge of the ellipse. This is because each rectangle is translated from the origin to the template point. This is not the center of the object! 

While keeping the merge node rendered, select the rect node and drag X to 50.0. Note that all rectangles now move off of the ellipse. This is because NodeBox does not take the rectangle's center into account when translating the object, but works in relation to the origin.

![Function of the origin point in Place node](/media/img/using/coordinates-place.png)

Controlling the origin
----------------------
Try to be aware where your objects are in relation to the origin. This makes manipulations further in the network easier.

* Turn the origin on in the viewer to see where your objects are.
* Use an [align](/documentation/nodes/align.html) node to move objects back to the origin after they've "wandered off".
* Use a [fit](/documentation/nodes/fit.html) node to force objects back on the origin and fit them in a specified box as well.
