---
layout: documentation
title: Getting Started
---
Downloading NodeBox
-------------------
If you haven't done this yet, you should [download](/download/) NodeBox first.

To install on Windows, double-click the installer and walk through the steps. On Mac OS X, drag the icon to your Applications folders (or anywhere you like).

Creating your first node
------------------------
Open the application. After a short loading time, NodeBox opens a new document window that looks like this:

![A new NodeBox window](/media/img/tutorial/new-nodebox-window.png)

NodeBox documents are composed of **networks of connected nodes**.

Click the highlighted **New Node** button. This pops up the node selection window:

![Node Selection Dialog](/media/img/tutorial/node-selection-dialog.png)

From this window, create the Star node. You can do this in two ways:

* Scroll through the (sorted) list until you find the Star node, then double-click it.
* Enter the first letters ("st") and press enter when the Star node is selected.

![NodeBox window with one star node](/media/img/tutorial/star-node.png)


The NodeBox document window consists of four panels. These are (clockwise, from the top):

* **The Viewer Pane**, showing the composition you're working on.
* **The Parameters Pane**, allowing you to adjust the parameter values of a node.
* **The Network Pane**, showing all nodes and their connections.
* **The Source Pane**, containing the source code of the currently selected node. (We won't use it in this tutorial.)

NodeBox called the new star node "star1". That's because each node in NodeBox needs to have a unique name.

Let's change some parameters:

* Double-click the **Points** field (where it says "20"), type **40**, and press enter. The star should now have forty points.
* Drag the **Inner Diameter** field (where it says "100.00"), and drag it to the left until it says **50.00**.

Your screen should look like this:

![A pointier Star](/media/img/tutorial/star-pointier.png)

Connecting nodes
----------------
The power of NodeBox comes from connecting nodes together. In this example, we're going to filter the output of the star node and snap all its points to a grid.

Click the **New Node** button again, and choose the **Snap** node. Double-click it to place it in the network.

You should see a grid in the viewer pane, but your star is gone. We can connect one to the other by dragging from the output port of the star1 node to the input port of the snap1 node.

![Star and snap node, connected together](/media/img/tutorial/star-snap-connected.png)

Once the two are connected, you should see the star appear again, over the grid, looking funny. This is because the snap node forces every point of the star shape to snap to a predefined grid. The size, position and strength of this grid can be changed:

* Change the **distance** to **40.00** by dragging the number to the right. You should see the grid getting larger, and the points of the star path moving.
* Drag the **strength** field from 100.0 to 0.0, then back to 100.0. You should see that the star morphs between its original and snapped form.

![Snap Distance of 40](/media/img/tutorial/snap-40.png)

NodeBox nodes (such as snap) are like Photoshop filters: they change the output of another node. However, unlike Photoshop, you can keep changing the parameter values long after the node was created. Nodes can be chained together to create powerful, custom filters.

Rendered and Selected Node
--------------------------
NodeBox can only show the output of **one node at a time**. We see the output of this **rendered node** in the viewer pane. Currently, snap1 is the rendered node.

We can look at one node while working on the parameters of another node. We'll keep the snap1 node rendered while selecting another node.

Click the star1 node **once**. The star1 node has a blue glow, indicating it is selected. The parameters pane updates with the parameters of the star path. We've now selected it.

Click the black fill rectangle to change the color. Set it to dark green by dragging the green component to 100. Note that the color of the star changes while we're dragging the color.

We've just updated the star1 node, but we're still looking at the results of the snap1 node. This means the changed output of star1 is passed on to serve as the input of snap1. This is the core idea behind NodeBox: *nodes passing visual geometry to other nodes*.

To recap:

* In the viewer, we look at the **rendered node**. In the network panel, the rendered node has a yellow bar at the top of the node. To change the rendered node, **double-click** a node.
* In the parameter panel, we look at the **selected node**. In the network panel, the selected node has a blue glow around it. To change the selected node, **click** a node once.

The Copy Node
-------------
Click the **New Node** button again, and choose the **Copy** node. Double-click it to place it in the network.

Connect the output of the snap1 node to the input of the copy1 node.

With the copy1 node selected and rendered:

* Change the **Rotate** to **36.00** by dragging the number to the right or double-clicking the number, typing 10, and pressing enter.
* Change the **Copies** to **10**.

NodeBox now creates ten copies, rotates them and placed them on top of each other:

![Star Copies](/media/img/tutorial/star-snap-copy.png)

Explore
-------

Now that we have some nodes to play with, we can change the settings and see the effect they have.

While we're exploring, keep the copy1 node rendered.

* In **star1**, change the **X** to **300.00**. The output will probably be too big to fit in the viewer. Use the *mouse wheel* to zoom in or out.
* In **star1**, change the **Y** to **50.00**.
* In **snap1**, drag the **Distance** to **52.00**.

![Star, snapped and copied](/media/img/tutorial/star-explored.png)

Saving and Exporting
--------------------
NodeBox saves documents in the .ndbx file format. These files can only be opened by NodeBox. If you want to use NodeBox compositions in other programs, **export** the document to PDF. You can use these PDF files in other graphic programs such as Adobe Photoshop or Illustrator. NodeBox preserves all vector information so your compositions won't be pixellated.

Before exporting, it's a good idea to change the document settings. This allows you to crop your composition to the preferred width and height and change the the background color.

To change the document settings, click on an empty space in the network view. Change them like this:

* Change the **Document Width** to **750.00**.
* Change the **Document Height** to **750.00**.

Once we've changed the document settings, export the document:

* Choose "Export..." from the File menu
* Navigate to the Desktop
* Export as "snapped.pdf" (without the quotes).
  (The first time might take a while). 
* Open this file by going to the desktop and double-clicking it. Zoom in to verify that all lines are still smooth.

NodeBox will export the rendered node. In our example, if we just wanted to render the star, we need to double-click the star1 node to make it rendered, then export again.

Next Steps
----------
Now that you've seen the basics, you can:

* [Explore Further](exploring.html): Build and explore interesting examples:  of basic nodes and how to use them together.
* [Animate](animation.html): See the basics of animation.
* [Learn the GUI](../using/gui.html): Discover all functionality of the NodeBox GUI.

