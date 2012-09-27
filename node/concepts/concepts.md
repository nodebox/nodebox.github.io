---
layout: documentation
title: How NodeBox Works
---
NodeBox uses a different model from traditional applications such as Photoshop or Illustrator. Imagine an **assembly line** of workers. Each worker does one thing, and one thing only. After he or she has done their operation, the object is passed on to the next person who does his thing.

![The FSO Assembly Line](/media/documentation/concepts/concepts-assembly-line.jpg)
<small><a href="http://en.wikipedia.org/wiki/Warszawa_(car)">Warszawas</a> assembled at <a href="http://en.wikipedia.org/wiki/Fabryka_Samochod%C3%B3w_Osobowych">FSO</a> in the early 1950s.</small>

In the NodeBox assembly line **nodes** are the workers. They are the basic building blocks of the application.

By connecting nodes together, you create your own assembly line where a new shape goes in and a complex result comes out. Every step along the way can be changed and animated.

Here's an example:

1. We create a **rect node**. This node is a generator: it *generates* a new shape.
  ![Step 1](/media/documentation/concepts/concepts-step1.png)
2. We connect a **color node** to the rect node. This color node takes the output of the rect node and changes its color. We call it a filter node, since it *filters* an existing shape.
  ![Step 2](/media/documentation/concepts/concepts-step2.png)
3. Finally we create a **rotate node** and connect it to the color node. It takes the output of the color node and changes its rotation. This is also a filter node, it filters the colored rectangle node.
  ![Step 3](/media/documentation/concepts/concepts-step3.png)

We can *examine* what each worker node is doing by changing the **rendered node**. The rendered node is the one that's displayed in the viewer. You can render a node by double-clicking it.

Ports
=====
Nodes can send data to each other using their **ports**. Ports represent the inputs and output of a node. A node takes data in from its inputs, processes it, and sets a value in its output port, ready to be picked up by the next node.

The input and output ports of a node are displayed in the network view. The input ports are also displayed in the port view:

![Dual views of the node](/media/documentation/concepts/concepts-ports-dual-view.png)
<small>Ports are displayed both in the port view (vertically) and the network view (horizontally).</small>

Whenever a port is connected, the port view indicates that the value for this port comes from another node:

![Connected ports](/media/documentation/concepts/concepts-ports-connected.png)
<small>The values for the width and height ports come from another node.</small>

Port Types
----------
Each port expects a certain type of values:

* **Floating-point numbers** are numbers with a fractional part. They are used to specify dimensions: the width / height of an object, the distance between two points, etc.
* **Integer numbers** are numbers *without* a fractional part. They are used to specify amounts: 10 copies, 50 points, etc.
* **Strings** are pieces of text. They are used wherever we need textual input: the filename of a SVG file, the lookup value for a CSV file or the text in a textpath node.
* **Points** are two-dimensional coordinates in space. They contain an X and Y value. They are used to specify a place in 2D space: the position of a rectangle, the scale of an object, etc.
* **Colors** contain red, green and blue values. They are used to specify color information: the fill color of an object, the stroke color of a line, etc.
* **Booleans** are values that can be either true or false. They are used to specify logical conditions: whether something is enabled or visible, whether elements need to be filtered out or not, etc.
* **Geometry** are shapes. They contain information about curves, lines and points. They are the primary visual building blocks of NodeBox.

The color of a port indicates its type. The background color of a node is the color of its output type.

Type Conversions
----------------
NodeBox automatically converts between types of ports. For example, if you connect a number to the text of the textpath, NodeBox converts the number into a string so it can be rendered as text.

![Automatic Type Conversion](/media/documentation/concepts/concepts-type-conversion.png)
<small>The integer output gets converted automatically to a string for the textpath node.</small>

Not all inputs and outputs are compatible. Here's an overview of which output ports (on the left side) can be converte to which input ports (on the top).

<table id="type-conversions">
  <tr>
    <th class="small">To &rarr;<br>&darr;From</th>
    <th>Integer</th>
    <th>Float</th>
    <th>String</th>
    <th>Boolean</th>
    <th>Color</th>
    <th>Point</th>
    <th>Geometry</th>
  </tr>
  <tr>
    <th>Integer</th>
    <td>&equals;</td>
    <td>&rarr;</td>
    <td>&rarr;</td>
    <td>&rarr;</td>
    <td>&rarr;</td>
    <td>&rarr;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <th>Float</th>
    <td>&rarr;</td>
    <td>&equals;</td>
    <td>&rarr;</td>
    <td>&rarr;</td>
    <td>&rarr;</td>
    <td>&rarr;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <th>String</th>
    <td>&rarr;</td>
    <td>&rarr;</td>
    <td>&equals;</td>
    <td>&rarr;</td>
    <td>&rarr;</td>
    <td>&rarr;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <th>Boolean</th>
    <td>&rarr;</td>
    <td>&rarr;</td>
    <td>&rarr;</td>
    <td>&equals;</td>
    <td>&rarr;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <th>Color</th>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&rarr;</td>
    <td>&nbsp;</td>
    <td>&equals;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <th>Point</th>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&rarr;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&equals;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <th>Geometry</th>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&rarr;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&rarr;</td>
    <td>&equals;</td>
  </tr>
</table>


Lists
=====
In essence, NodeBox is a list processing machine. Although initially invisible, the input and output of all nodes are lists.

If you wonder why NodeBox does not have a "for loop" like in programming, that's because looping is implicit: generally, if a node receives a list of data, NodeBox will execute that node for each element in the list, and give back a list with the same size.

![A grid node connected to an ellipse node](/media/documentation/concepts/concepts-grid-network.png)
<small>The grid node provides a list of positions for the ellipse node.</small>

A grid with three by three columns executes the ellipse node 9 (3 x 3) times:

![A grid of 3 by 3 ellipses](/media/documentation/concepts/concepts-grid-3x3.png)

A grid with ten by ten columns executes the ellipse node 100 (10 x 10) times:

![A grid of 10 by 10 ellipses](/media/documentation/concepts/concepts-grid-10x10.png)

The grid node doesn't do the looping: it just gives back a list of points. The NodeBox engine takes care that the ellipse node gets executed for as many elements as there are in the list:

A short list of 9 points for a 3 x 3 grid:

![The points of a grid of 3 by 3](/media/documentation/concepts/concepts-points-3x3.png)

A long list of 100 points for a 10 x 10 grid:

![The points of a grid of 10 by 10](/media/documentation/concepts/concepts-points-10x10.png)

The output of the ellipse node is – again – a list: a list of 9 paths for a 3 x 3 grid, and a list of 100 paths for a 10 x 10 grid.

List Matching
-------------
So far, we've only connected one port on a node. The behavior should now be obvious: execute the input node as many times as there are elements in the list. But what if we have more than one connected port? What if the lists have different sizes? NodeBox **matches** lists in a smart way.

Imagine that you want to change the colors of a number of textpaths. You have five text paths (A-E) and three colors: red, green and blue:

![Five letters, three colors](/media/documentation/concepts/concepts-list-matching-inputs.png)
<small>Five text paths, three colors.</small>

NodeBox executes the colorize node (which is what we're using to change the color of the text paths) as many times as there are elements in the **longest list**. If other lists run out of data, they wrap around:

![List wrapping](/media/documentation/concepts/concepts-list-matching-result.png)
<small>Red and green are re-used for letters D and E</small>

Another example: say we have create 10 ellipses on a line (I use a grid node with one row and ten columns):

![10 ellipses, 1 size value](/media/documentation/concepts/concepts-list-matching-ellipse-1.png)

I can connect a **sample** node to the width and the height. The network now looks like this:

![Ellipse network](/media/documentation/concepts/concepts-list-matching-ellipse-network.png)

The amount of numbers wraps around:

![10 ellipses, 10 size values](/media/documentation/concepts/concepts-list-matching-ellipse-10.png)
<small>10 ellipses, 10 size values</small>

![10 ellipses, 9 size values](/media/documentation/concepts/concepts-list-matching-ellipse-9.png)
<small>10 ellipses, 9 size values</small>

![10 ellipses, 5 size values](/media/documentation/concepts/concepts-list-matching-ellipse-5.png)
<small>10 ellipses, 5 size values</small>

![10 ellipses, 2 size values](/media/documentation/concepts/concepts-list-matching-ellipse-2.png)
<small>10 ellipses, 2 size values</small>

![10 ellipses, 1 size value](/media/documentation/concepts/concepts-list-matching-ellipse-1.png)
<small>10 ellipses, 1 size value</small>

Note that the last one is the same as specifying one value: the value list "wraps around" for every ellipse, effectively providing only one value.


A Visual Programming Language
=============================
NodeBox is actually a *visual functional progamming language*. It is inspired by a number of textual functional programming languages, notably Clojure and Haskell. 

In functional programming, the *functions* take a central role, **transforming data from one representation to the next**.

Note that in NodeBox, we haven't really talked about classical object-oriented programming constructs such as classes and objects. Instead, the objects of NodeBox are really holding places for data. The functions take in the data and generate new data.

Internally, nodes have a reference to a function: a piece of code written in Java, Python or Clojure.
