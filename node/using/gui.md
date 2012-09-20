---
layout: documentation
title: The Graphical User Interface
---
TODO
====
* Update screenshots

![GUI Panes](/media/img/using/gui-panes.png)

A NodeBox document window consists of these main components:

The Viewer Pane
---------------
![The Viewer Pane](/media/img/using/gui-viewer-pane.png)

The Viewer Pane shows the actual drawing. It also shows handles for the currently selected node. In addition, it can show geometric detail such as the location of the points, their index numbers and the [origin](coordinates.html).

With your mouse in the viewer pane:

- Use the scroll wheel to **zoom** the view in or out.
- Hold the spacebar to **pan** the view.
- Right-click and choose "Reset View" to **reset** the view back to 100% zoom.

Most nodes have **handles**. They allow direct manipulation of the shape, which is generally easier than dragging numbers in the parameter pane. 

![GUI Handles](/media/img/using/gui-handles.png)
<small>Handles for the Star node</small>


The Parameters Pane
-------------------
![The Parameters Pane](/media/img/using/gui-parameters-pane.png)

The parameters pane allows you to change the parameters of the currently selected node. The exact parameters depend on the type of node. Parameters have different **types**: numbers, text, colors, menus, etc.

Numbers are **draggable**. This means that for each number you can:

- **Double-click the number** to enter a new number. Press enter to confirm.
- **Drag the number** to change it in increments of 1.
- **Drag the number while holding the ALT key** to change it in increments of 0.01 (for small changes).
- **Drag the number while holding the SHIFT key** to change it in increments of 10 (for big changes).
- **Click the arrow keys** to nudge it up or down by 1. Holding ALT and SHIFT nudge by 0.01 and 10, respectively.

Each individual parameter has a contextual menu with two options:
![The Parameter Menu](../../media/img/using/gui-parameter-menu.png)
- **Toggle Expression** allows you to work with expressions. [Read more about using expressions](expressions.html).
- **Revert to Default** changes the parameter value back to its original value.

A powerful feature of NodeBox is that you can change the parameters of one node while keeping another node **rendered** in the viewer. This allows you to see the effects of your changes as they propagate through the network. 

The Metadata button allows you to [add your own parameters to a node](metadata.html).

The Network Pane
----------------
![The Network Pane](/media/img/using/gui-network-pane.png)

The network pane is where you connect nodes together to make networks. 

You can zoom and pan the network in the same you manipulate the viewer:

- Use the scroll wheel to **zoom** the view in or out.
- Hold the spacebar to **pan** the view.
- Right-click and choose "Reset View" to **reset** the view back to 100% zoom.

You can copy-paste nodes in one document and between documents. Because names in the network are unique, NodeBox will rename nodes as needed. Note that NodeBox doesn't rewrite expressions: any expressions that refer to other nodes need to be renamed manually.

The difference between the selected and rendered node is explained in the [getting started tutorial](../tutorial/getting-started.html).

To change the **Document Settings** (such as background color and document width / height), deselect all nodes. Do this by clicking on the background area in the network pane.


The Source Pane
---------------
![The Source Pane](/media/img/using/gui-source-pane.png)

The source pane shows the source code that makes up a node. It allows you to change the functionality of any node. The original node is never changed: the moment you start editing, NodeBox makes a copy of the source code.

Here's a small example:

* Create a rect node in the network pane.
* Note that the source pane updates with the source code for the rect node.
* Find the line where it says <code>p.rect(self.x, self.y, self.width, self.height)</code> and change it so it says <code>p.ellipse(self.x, self.y, self.width, self.height)</code>.
* Note that when you change the code, two things happen: the reload button turns red, and the node gets "under construction" banner at the bottom. This means the code for the node has changed, but the changes aren't active yet.
* To make the changes "stick", click the red reload button. The node returns to normal, and the rectangle becomes an ellipse.

![The Source Pane with changed source code](/media/img/using/gui-source-reload.png)

If you make an error while editing the source code, the node gets red bars indicating something is wrong. Click the node to see the messages pane: it tries to explain what went wrong. Understanding these error messages can take some practice.

![The Source Pane with an error](/media/img/using/gui-source-error.png)

If you want to know more about creating your own nodes, read: [programming your own nodes](../advanced/programming-nodes.html).


The Address Bar
---------------
![The Address Bar](/media/img/using/gui-address-bar.png)

The address bar is useful when using sub-networks (also called geonets). It allows you to jump back up a level. [Read more about using geonets](geonets.html).

The Animation Bar
-----------------
![Gui Animation Bar](/media/img/using/gui-animation-bar.png)

The animation bar controls the animation features of NodeBox. You can:

- **Drag the frame number** to scrub through the animation.
- **Double-click the frame number** to go to a specific frame.
- **Click play** to start the animation from the current frame.
- **Click rewind** to stop the animation and go back to frame 1.


NodeBox Documents
-----------------
NodeBox manages documents, much in the same way you work on a Photoshop document. Only in NodeBox we just save the nodes, since we can always recalculate the output of the network.

NodeBox documents use the .ndbx extension. These documents can be opened and saved only in NodeBox. To work with other programs, use the import and export functionality.


Importing Graphics
------------------
To import vector data use the [Import](/documentation/nodes/import.html) node.


Exporting Graphics
------------------
To export the current image, choose File > Export. The export command doesn't ask for an extension but automatically exports as a PDF file. PDF files retain all vector information and can be manipulated in vector programs such as Adobe Illustrator or Inkscape.

If you have an animation, you can export it in two ways:

- As a sequence of images. Use File > Export Range to export a sequence of images. NodeBox will name them progressively, e.g. myimage-1.png, myimage-2.png, ...
- As a movie. Use File > Export Movie to export a movie using a variety of popular formats. 

