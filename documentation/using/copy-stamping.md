---
layout: documentation
title: Creating Variations using Copy Stamping
---
When we use nodes such as [copy](/documentation/nodes/copy.html) and [place](/documentation/nodes/place.html) to generate many results, they repeat the exact same input shape. That's because NodeBox takes the output of the node and copies it as many times as needed:

![Copy Stamping Turned Off](/media/img/using/copy-stamping-off.png)

How do we create a grid where every rectangle has a different color and rotation? In other words, how do we create variation for each single input shape? For this, we need copy stamping.

![Copy Stamping Turned On](/media/img/using/copy-stamping-on.png)

Copy stamping changes nodes in the network before the copy stamp node. That means that the NodeBox engine goes back and changes the outputs of input nodes every time it loops through the network.

![Copy Stamping Network](/media/img/using/copy-stamping-network.png)

<small>When copy stamping is turned on, the nodes marked in red are re-evaluated for each copy.</small>

For people used to programming: nodes such as copy and place work as a loop. Copy stamping gives you variables that  input nodes can use as arguments for their parameters.

Let's build the example above.

* Create a **Rect** node. Set **Width** to **10.00** and **Height** to **10.00**.
* Create a **Transform** node. Set **Rotation** to **45.00**.
* Connect **rect1** to **transform1**.
* Create a **Grid** node. Set **Width** to **500.00** and **Height** to **150.00**. Set **Rows** to **12** and **Columns** to **40**.
* Create a **Place** node.
* Connect **transform1** to **place1 (shape)**.
* Connect **grid1** to **place1 (template)**.

We've now created the first step in our example: a lot of rectangles, all with the same color and rotation. Let's use copy stamping to create variation.

![Copy Stamping Example: Step 1](/media/img/using/copy-stamping-example-1.png)

To use copy stamping:

1. Turn on copy stamping in the copy / place node.
2. Use the stamp expression in the parameter we want to change.

The trick with copy stamping is to ask yourself: what do I want to change for every step? In our case, the **rotation** of every shape needs to be different. We can change the rotation by modifying transform1's rotate parameter: that's the parameter that needs copy stamping.

* In **place1**, turn **Copy Stamping** on.
* In **transform1**, set **Rotate** to the expression <pre>stamp("CNUM", 45)</pre>

**Voila!** Every rectangle now has a different rotation.

![Copy Stamping Example: Step 2](/media/img/using/copy-stamping-example-2.png)

By turning copy stamping on, NodeBox revisits every node that's connected to the shape port: if the node uses a *stamp expression*, NodeBox recalculates the node with the new value in place.

The **stamp expression** is the key to use copy stamping. Let's examine it in detail:

    stamp("CNUM", 45)
    
The expression consists of two parts:

* The **variable name** ("CNUM"): We can create custom variables (the expression parameter in the place node) or use the built-in CNUM that NodeBox provides for us. 
* The **default value** (45): If copy stamping is turned off, or if we're just rendering the translate1 node, we don't have access to the CNUM variable. In that case, we need a default value. **As a rule, use the value that was there before**. In our case, the rotate parameter was set to 45, so we'll use the number 45 here as well.

CNUM is the **copy number**. For every copy we make, NodeBox assigns a unique index number that we can refer to:

* For the first copy, CNUM will be 0. (NodeBox starts counting at zero)
* For the second copy, CNUM will be 1.
* For the third copy, CNUM will be 2, and so on.

In our example, we'll link the rotation to CNUM so the value of the rotate parameter changes for every copy:

* For the first copy, the rotation is 0.
* For the second copy, the rotation is 1.
* For the third copy, the rotation is 2.


Color
-----
Copy stamping can be used anywhere, but colors require a special mention since they require nested expressions.

* In **rect1**, set **Fill** to the expression <pre>hsb(stamp("CNUM", 0) / 480, 1, 1)</pre>
* Instant rainbow!

![Copy Stamping Rainbow](/media/img/using/copy-stamping-rainbow.png)

The **hsb** function provides using hue, saturation and brightness. The saturation and brightness are set to 1. For the hue, we've used a stamp expression:

    stamp("CNUM", 0) / 480

We use the copy number and divide this value by 480. First off, 480 is the number of copies: one for each point in a grid of 12 x 40. Colors range from 0.0 to 1.0. If we would use the copy number, it would go from 0 to 480. By dividing by 480, we convert values in the range 0 - 480 to the 0.0 - 1.0 range, needed for colors.

We can use the stamp expression in any part of the hsb expression:

* In **rect1**, set **Fill** to the expression <pre>hsb(1, stamp("CNUM", 0) / 480, 1)</pre>
* Set the **Document Background** to Red = 50, Green = 0, Blue = 75

![Copy Stamping With Saturation](/media/img/using/copy-stamping-saturation.png)

We now used copy stamping to change the saturation of each copy.


Point Numbers
-------------
Note that the rotation begins at zero in the top left and moves to the right, then to the next row, and so on. This order is defined by the **point order** of the template node. You can see this point order by double-clicking grid1 and turning on Point Numbers in the viewer.

![Copy Stamping: Point Numbers](/media/img/using/copy-stamping-point-numbers.png)

We can use the [sort](/documentation/reference/sort.html) node to change the ordering of the point numbers, creating interesting effects:

* If you have point numbers turned on, turn it off again.
* Double-click **place1** to make it the rendered node.
* To make the effect more pronounced, we'll move the rectangles off-center. In **rect1** set **Y** to **5.00**.
* Create a new **Sort** node. Set **Scope** to **Points within geometry**.
* Connect **grid1** to **sort1**.
* Connect **sort1** to **place1 (template)**.
* In **sort1** set **Order** to **Proximity To Point**. Note that the points start rotating from the center.
* Drag the handle to change the center of the sorting. 
* Play around with the different order options. (such as Shift, Angle To Point, etc.)

![Copy Stamping Point Sorted](/media/img/using/copy-stamping-point-sorted.png)

The [geometry](geometry.html) page has more details on point numbers and their implications.


Finishing Off
-------------
To create the initial example:

* In **sort1** set **Order** to **Random**.
* In **rect1** set **Y** back to **0.00**.

![Copy Stamping On](/media/img/using/copy-stamping-on.png)
