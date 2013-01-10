---
layout: documentation
title: Programming your own Nodes
---
![Under Construction](/media/img/under-construction.png)
<small>This page is still under construction.</small>

Once you get the hang of it, it becomes fairly easy to build networks and hide lengthy procedures behind a subnetwork facade. Nonetheless, sometimes there are cases where you wish you could write your own nodes. 

Maybe you want to reuse a cool piece of code in NodeBox that you've written. Maybe NodeBox is missing some key piece of functionality that you need. Or maybe you just want to experiment with writing a new node from scratch. This tutorial will show you how.

The first steps.
================
First off, let's see how we could create a node where we just reference a piece of code that is already inside NodeBox. This is really easy. Start off by:

- Create a new **'node' node**. It will automatically be named node1.
  This is the most basic of the available nodes and it's also the one from which all other nodes are derived. All it does is output 0.0. It's basically a blank slate node.

- With **node1** selected, press the **Metadata button** on top of the parameter panel. This will bring up the metadata panel.

The metadata panel always relates to one specific node, in this case node1. The sidebar on the left shows items that relate to node and port settings. Our node has no input ports yet so the only item you can select here is 'Settings'. If you click on it you can see a few input fields displaying information about the current node. These the metadata of the node. We ignore these for now and add two new ports:
- Press the **+ button** below the left sidebar. 
- In the dialog that appears, enter **value1** in the name field and choose **float** as the type. Then press 'OK'. This creates a new port and brings up an overview of its port metadata.
- Repeat the previous step to add a port named **value2**. Note that each time you add a new port, the parameter panel adds a new parameter field widget below the last one. With the metadata panel open it's not yet possible to change their values. 
-Press **Ok** to apply the changes. You can now drag the value1 and value2 values but the viewer still shows 0.0. We still have to tell our node what to do with the values we provide it:
- With node1 still selected press the **Metadata button** again.
- On the left, select 'Settings'. The **Function** field contains by default the value 'core/zero'. This means that the node refers to a function named zero and this function resides in a namespace called core. A namespace can be seen as some kind of container of functions that are related to each other. For example the namespace 'math' contains functions like add, multiply, sin, cos, etc...
- Change the value of Function to **math/add**.
- Press Ok to close the metadata panel.

You can now drag the value1 and value2 values around and see the results change in the viewer: the two values are added together. If you return to the metadata panel and change the value of Function to math/multiply, you will see that the two values are being multiplied instead. 

If you would add a third port however, this would result in an error (of which NodeBox will inform you) because the functions math/add and math/multiply take exactly two arguments. So the number of ports in a node always has to be the same as the number of arguments the corresponding function takes. 

If you want to, you can rename your 'node1' node to something more comprehensible, like 'add' or 'multiply' (by right clicking and choosing rename)

Link to external python code.
=============================

todo...
