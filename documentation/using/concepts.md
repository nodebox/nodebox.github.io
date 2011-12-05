---
layout: documentation
title: NodeBox Concepts
---

NodeBox uses a different model from traditional applications such as Photoshop or Illustrator. It is easy to visualize: imagine an **assembly line** of workers. Each worker does one thing, and one thing only. After he or she has done their operation, the object is passed on to the next person who does his thing.

![The Ford Assembly Line](/media/img/using/concepts-assembly-line.jpg)

In the NodeBox assembly line **nodes** are the workers. They are the basic building blocks of the application.

NodeBox has two basic types of nodes:

* **Generator nodes** do not take in another shape. They are used to create shapes from scratch. Examples are rect, ellipse or star.
* **Filter nodes** take in other shapes and change them. They are used to manipulate shapes. Examples are wiggle, transform or copy.

![A typical NodeBox script](/media/img/using/concepts-nodebox-network.png)

<small>A typical NodeBox network. line1 and rect1 are generators. The other nodes are filters.</small>

By connecting nodes together, you create your own assembly line where a new shape goes in and a complex result comes out. Every step along the way can be changed and animated.

Nodes are connected using their **ports**. Geometry (vector data) moves through a connection from the output port to the input port. The behavior of a node is controlled by its **parameters**.

Each node has a **prototype**, or base node, it inherits from. When creating a new node, all data from the prototype node, such as the parameters and ports is copied over in the new node. To keep NodeBox files small, only changes between your node and the prototype are saved.

The "core" nodes in NodeBox are created in the same way: they inherit from the **root node** and add their own parameters, ports and code. The core nodes are stored in a document that is loaded when NodeBox starts up. They are not "special" in any way. **Any node can function as a template for a new node**. You can [customize existing nodes](metadata.html) or [build nodes from scratch](../advanced/programming-nodes.html) and create your own libraries that are loaded when NodeBox starts.
