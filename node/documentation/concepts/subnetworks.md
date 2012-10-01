---
layout: documentation
title: Subnetworks
---
TODO
====
* Creating a subnetwork from scratch
* Group into Network
* Use case: node organization
* Use case: nodes as functions (with published ports) --> nested lists
* Gear example
* Space invader example

NodeBox networks can become really big. After a while, it becomes harder and harder to find the node you're looking for. Luckily, just like you can group related files in a directory on your hard disk, NodeBox can group related nodes into a network.

NodeBox networks can act as an **organizational** tool, keeping big networks tidy. By grouping a block of nodes into a network, you can box up and name a group of functionality. For example, when working on a data visualisation project, the header and explanatory text  could go in a subnetwork "captions".

NodeBox networks can also act as **custom nodes**, much in the same way as the built-in nodes. 

Good practices
--------------
* Always provide a **position port** for networks that generate new geometry (like the invaders node).
* Test out the network first, without connecting anything to it. If a single copy of e.g. an invader network works, it is likely a grid of them will work as well. Contrary, if moving the position of a single invader doesn't do what you want, fix that first before making a grid out of them.
* When possible, make your network look like a built-in node. A good example of a generating node is the [ellipse node](/node/reference/corevector/ellipse.html); an example of a filtering node is the [translate node](/node/reference/corevector/translate.html).