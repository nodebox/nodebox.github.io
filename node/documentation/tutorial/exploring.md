---
layout: documentation
title: Exploring Nodes
---
TODO
====
* Update screenshots into steps
* Less examples

Spirograph Example
-------------------

Let's make a drawing based on the [Spirograph](http://en.wikipedia.org/wiki/Spirograph) principle. 

In short: we will **create a shape** and **copy it** a few times on top of each other with a difference in rotation.

![Exploring Spirograph](/media/img/tutorial/exploring_spirograph.png)

Create a [Freehand](../nodes/freehand.html) node and draw a small line in order to have a reference for the rest of the procedure. You can **draw by clicking and dragging the mouse** in the viewer pane.

Create a [Reflect](../nodes/reflect.html) node and send the output of freehand1 to it. 

* Change the **Angle** parameter to **90.00**. You should see the change in location of the reflected shape.
* Change the **X** parameter to **0.0**. Dito.

Create a [Copy](../nodes/copy.html) node and send the output of reflect1 to it.

* Change the **Copies** parameter to **20**.
* Change the **Rotate** parameter to **18.0**. The calculation of the rotation angle is based on the equation 360.0 / number of copies.

Render copy1 and click once on freehand1. Start drawing anything and see the spirograph appear. **Not pleased with the result?** You can **start over** and empty the path by selecting all numbers in the path parameter then press backspace and the return key.

**Try out:**

* Different settings for the parameters in copy1 to create more or less complex spirograph drawings.
* Insert a [Color](../nodes/color.html) node between the freehand1 and reflect1 to experiment with colors.  
* Copy the four nodes, make a few variations and group them by sending all of them to a [Merge](../nodes/merge.html) node.

![Exploring Spirograph Advanced](/media/img/tutorial/exploring_spirograph_advanced.png)

Resample and place.
-------------------

Every node has a geometry object as output which means that you have access to the points. The [Resample](../nodes/resample.html) node creates a new set of points for an input geometry based on the distance between points or on a certain amount of points. 

Lets create a text effect that works on that principle.

![Exploring Resample Place](/media/img/tutorial/exploring_resample_place.png)

Create a [Textpath](../nodes/txtpath.html) node 

* Change **Text** parameter to **NODE**. 
* Set the **Font** to **Helvetica Bold**.
* Set **Size** to **170**.

Copy textpath1. You can **copy and paste nodes** by drawing a rectangle around the nodes that you want to copy. Use normal copy/paste shortkeys (e.g ctrl-c / ctrl-v) to create a duplicate.

* Change **Text** parameter to **Box**. 
* Change the **Y** parameter to **-200**.
* Set **Size** to **230**.

Create a [Merge](../nodes/merge.html) node to bring both previous nodes together.

![Exploring Resample Place Step1](/media/img/tutorial/exploring_resample_place_step1.png)

Create a [Resample](../nodes/resample.html) node. Connect merge1 to it.

* Set **Method** to **by length**.
* Set **Length** to **2**.

Create an [Ellipse](../nodes/ellipse.html) node.

* Change the **Alpha** amount of the fill color to **2.0**. You have access to the different color channels by clicking the color widget.
![Exploring Resample Place Fill](/media/img/tutorial/exploring_resample_place_fill.png)
* Change the stroke color to a semitransparent orange.
* Change the **Stroke Width** to **0.2**.

Create a [Place](../nodes/place.html) node. As you can see it has **two input ports** instead of one. The upper port is called **Shape** and receives the shape that has to be placed/copied. The second port is called **Template** and receives a template on which the shape has to be placed/copied on.

* Connect ellipse1 to the shape port of place1.
* Connect resample1 to the template port of place1.

What you should see is that NodeBox **draws an ellipse on each point of the template**. The visual effect is created by layering all these transparent ellipses.

**Try out:**

* Different amount of points in resample1. Change the method to **by Amount** and set an amount to the points parameter. See what results from that. Try the "Per Contour" option.
* Change the ellipse into an other shape. 

![Exploring Resample Place Advanced](/media/img/tutorial/exploring_resample_place_advanced.png)

A pattern example.
-------------------

Creating patterns is fairly easy in NodeBox 2. A key node for building networks that create patterns is the [Align](../nodes/align.html) node. It allows you to change the centerpoint of a geometry. The base for these operations on the vertical and horizontal axes is the origin which you can toggle on/off in the viewer pane.

Lets create an example:

![Exploring Pattern](/media/img/tutorial/exploring_pattern.png)

Create a [Polygon](../nodes/polygon.html) node. A triangle should appear.

* Set **Radius** to **12.00**.
* Set **Sides** to **3**.

Visualize the origin (in the viewer pane). The polygon is centered in its center point. The idea is to change it's position so the triangle is on top of the horizontal line and at the right of the vertical line. We could do this manually by changing X and Y parameters. Using an align node is better practice.

Create an [Align](../nodes/align.html) node and connect polygon1 to it.

* Set **Horizontal Align** to **Left**.
* Set **Vertical Align** to **Bottom**.

Create a [Copy](../nodes/copy.html) node to create a few copies. We will create a shell shape.

* Set **Copies** to **18**.
* Set **Rotate** to **20.00**.
* Set **Scale X** to **10.00**.
* Set **Scale Y** to **10**.


![Exploring Pattern Shell](/media/img/tutorial/exploring_pattern_shell.png)

We will do the previous functions another time but with a few alterations in both nodes.

Create an [Align](../nodes/align.html) node. Connect copy1 to it.

* Set **Horizontal Align** to **Right**.
* Set **Vertical Align** to **Middle**.

Create a [Copy](../nodes/copy.html) node to create a few copies. Connect align2 to it.

* Set **Copies** to **4**.
* Set **Rotate** to **90.00**.

![Exploring Pattern Shell 4](/media/img/tutorial/exploring_pattern_shell_4.png)

We will transform this pattern by sending it to a [Snap](../nodes/snap.html) node. **Create one** and Set the **Distance** parameter to **50.0**

Create a [Grid](../nodes/gid.html) node. This grid will be used as a template to place a copy of the snap1 result on each one of its points.

* Set **Rows** to **3**.
* Set **Columns** to **3**.

Create a [Place](../nodes/place.html) node. Send snap1 to **Shape** and grid1 to **Template**.

Render the place node for the final result.

**Try out:**

* Change **Rotation** parameter in copy1.
* Change **Distance** parameter in snap1.
* Change some other parameters..

![Exploring Pattern Advanced](/media/img/tutorial/exploring_pattern_advanced.png)

Node order.
-----------

A very import thing to keep your eyes on is the node order. The chronology of nodes and the way they are connected to each other, sometimes makes a big difference in the final result. Following example will show how it works.

![Exploring Nodeorder](/media/img/tutorial/exploring_nodeorder.png)

We are going to create two procedures for copying and transforming a shape. 

* The **first** one will **create a shape**, than **transform it** over a [Wiggle](../nodes/wiggle.html) node to finally **be copied** 6 times through a [Copy](../nodes/copy.html) node.
* The **second** one will start from **the same shape** as in procedure one but will reverse the order of wiggle and copy so we will **copy** the node 6 times first and then **wiggle** the result.

Lets start with creating a shape:

Create a [Rect](../nodes/rect.html) node and leave the parameters as default.

Create an [Ellipse](../nodes/ellipse.html) node and leave the parameters as default.

Create a [Compound](../nodes/compound.html) node which does binary operations on two different shapes. Connect rect1 to the first input/port and connect ellipse1 to the second port. Change **Function** to **difference**.

You should see the difference path of the rectangle and the ellipse. Lets put an ellipse in the center of it.

Create an [Ellipse](../nodes/ellipse.html) node.

* Set **Width** to **50.00**
* Set **Height** to **50.00**

**Bring it together** by creating a [Merge](../nodes/merge.html) node.

![Exploring Nodeorder Shape](/media/img/tutorial/exploring_nodeorder_shape.png)

Now we will do a few things twice:

Create **two** [Copy](../nodes/copy.html) nodes. One for each procedure.

* Set **Copies** to **6**.
* Set **Translate X** to **130.00**.

Create **two** [Wiggle](../nodes/wiggle.html) nodes. Again one for each procedure.

* Set **Scope** to **contours**. This setting will only change the location of each contour within the shape.
* Set **Wiggle X** to **10.00**.
* Set **Wiggle Y** to **10.00**.
* Select a seed.

Now **connect merge1 to the copy1** AND **connect merge1 to wiggle2**.

The first procedure takes a copy first, the second wiggles the shape first.

Now **connect copy1 to wiggle1** and **connect wiggle2 to copy2**.

The first procedure wiggles the copied shapes which results in a variation for each shape while the second procedure copies a wiggled shape hence produces a copy which looks the same for each one of them.

Lets put them beneath each other.

Create a [Transform](../nodes/transform.html) node to relocate copy2. Set **Translate Y** to **130.00**.

Create a [Merge](../nodes/merge.html) node to bring the two procedures together.

**Try out:**

* Create a grid of 4 * 4 to have an other template.
* Change the starting shape.

![Exploring Nodeorder Advanced](/media/img/tutorial/exploring_nodeorder_advanced.png)

