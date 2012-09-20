---
layout: documentation
title: NodeBox Concepts
---
TODO
====
* List Matching
* Port types
* Nodes are functions, visual functional programming
* Type conversions


NodeBox uses a different model from traditional applications such as Photoshop or Illustrator. It is easy to visualize: imagine an **assembly line** of workers. Each worker does one thing, and one thing only. After he or she has done their operation, the object is passed on to the next person who does his thing.

![The FSO Assembly Line](/media/img/using/concepts-assembly-line.jpg)
<small><a href="http://en.wikipedia.org/wiki/Warszawa_(car)">Warszawas</a> assembled at <a href="http://en.wikipedia.org/wiki/Fabryka_Samochod%C3%B3w_Osobowych">FSO</a> in the early 1950s.</small>

In the NodeBox assembly line **nodes** are the workers. They are the basic building blocks of the application.

By connecting nodes together, you create your own assembly line where a new shape goes in and a complex result comes out. Every step along the way can be changed and animated.

There are different *types* of nodes. Some nodes deal only with numbers: adding them, subtracting them, calculating the average of a list of numbers. Some other nodes deal with visual data: these are called geometry nodes. They do things like creating ellipses or scaling geometry.

You connect nodes through their **ports**. There are different types of ports:

* **Floating-point numbers** are numbers we use everywhere: as the distance beween two points, the size of an object, ...
* **Integer numbers** are numbers without a fractional part. They are used to specify amounts: 10 copies, 50 points, etc.
* **Strings** are pieces of text. They are the text of a textpath node, or the values of the rows in a CSV file.
* **Points** are two-dimensional points in space. They contain an X and Y value.
* **Colors** contain red, green and blue values. They are used for example in the "colorize" node.

Lists
-----
NodeBox deals with **lists**. All ports take in lists. Each node outputs a list. You can always look at the output contents of a node by clicking on the "data" tab in the viewer.

In general, if a node takes a list of size x, it will generate a list of size x. For example, if you have a list of three rectangles, connecting them to the colorize node will generate three colored rectangles.

It becomes a bit more complex once we connect multiple input ports. If the input lists are not of the same size, NodeBox stops processing if the *shortest* list runs out of elements.

For example, imagine we have a "make points" node. If we connect a list of 10 numbers to the X port, and a list of 2 numbers to the Y port, only two points are generated.

If you want to generate more points, either make list 2 bigger, or use a "cycle" node to loop the shorter lists, endlessly.


Node Prototype
--------------
*(You only need to know this if you're creating your own nodes)*

Each node has a **prototype**, or base node, it inherits from. When creating a new node, all data from the prototype node, such as the parameters and ports is copied over in the new node. To keep NodeBox files small, only changes between your node and the prototype are saved.

Even NodeBox's built-in nodes are created in the same way: they inherit from a base node and add their own parameters, ports and code. The built-in nodes are stored in a document that is loaded when NodeBox starts up. They are not "special" in any way. **Any node can function as a template for a new node**. You can [customize existing nodes](metadata.html) or [build nodes from scratch](../advanced/programming-nodes.html) and create your own libraries that are loaded when NodeBox starts.
