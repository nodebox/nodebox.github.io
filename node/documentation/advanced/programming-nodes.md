---
layout: documentation
title: Programming your own Nodes
---
![Under Construction](/media/img/under-construction.png)
<small>This page is still under construction.</small>

Once you get the hang of it, it becomes fairly easy to build networks, resulting in interesting compositions. Once you know the principle behind subnetworks you're also able to hide lengthy procedures, making it easier to manage networks at the outer level. But maybe there are times that you wish you could write your own nodes. This could be the case if you have a cool piece of code lying around you'd like to reuse in NodeBox. It's also possible that you tried to build something complex in NodeBox and while you've almost achieved what you wanted you noticed some key bits of functionality are missing or hard to find out how. Or maybe you just like to experiment. In all these cases you might have wondered if it's possible to incorporate your own pieces of code in NodeBox. In this tutorial we'll show you the steps involved to achieve this.

The easiest way of making a new node.
=====================================
First off, let's see how we could recreate a node where we just reference a piece of code that is already in NodeBox. This is really easy. Start off by:

- Create a new 'node' node. It will automatically be named node1.
  This is the most basic node and it's also the node of which all other nodes are derived. It has no ports so it's not possible to alter its inputs. All nodes have an output, though, and the 'node' node is no exception, what it does is output a float with value 0.

- With node1 selected, press the Metadata button on top of the parameter panel. 
  The metadata panel appears in the form of a dialog. The metadata panel is always specific to one node and the title bar tells you which one (node1). 
  On the left there is a sidebar divided between Node - Settings and Ports. Because our node is empty and has no input ports yet the only item you can select here is 'Settings'. When you do this you can see some name fields denoting some information about the current node. We call these the metadata of the node. We ignore these for now and add two new ports:

- Press the + button below the sidebar on the left. 
  A new dialog pops up that asks to enter a name for the new port. Enter value1 as a name, for the type choose 'float'. Then press 'OK'.
  You now see a whole bunch of new fields appear that replace our earlier node metadata. These fields are the port metadata.
- Repeat the previous step to add a port named value2.
  Notice that each time you added a new port, a new parameter with a number widget was added in the parameter panel. It's not possible to change them right now, because the metadata panel is still open. Press "Ok" to apply the changes.
Note that when you try changing the values of value1 and value2 nothing happens in the viewer. This is because the base node still links to an internal function that outputs 0.0. Let's change that.
- With node1 still selected press the metadata button again.
- On the left, select 'Settings'.
  The second but last field is named Function and contains by default the value 'core/zero'. What this means is our node refers to a function named zero and this function resides in a namespace called core. A namespace can be seen as some kind of container of functions that are related to each other. For example the namespace 'math' contains functions like add, multiply, sin, cos, etc...
- Change the value of 'Function' to from core/zero to math/add.
- Press Ok to close the metadata panel.

You can now drag the value1 and value2 values around and see the results change in the viewer: the two values are added together.
If you go back in the metadata panel and change the value of Function to math/multiply, you will see that the two values are being multiplied instead. 

If you would add a third port however, this would result in an error (of which NodeBox will inform you) because the functions math/add and math/multiply take exactly two arguments. So the number of ports in a node always has to be the same as the number of arguments the corresponding function takes. 

If you want to, you can rename your 'node1' node to something more comprehensible, like 'add' or 'multiply' (by right clicking and choosing rename)
