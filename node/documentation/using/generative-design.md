---
layout: documentation
title: Creating Generative Design
---

Nodebox is ideal for creating generative designs. We've covered a few of them before (f.e the arab tilling principle). 

Suppose i want to recreate something like the invader example as decribed on the [subnetworks page](../concepts/subnetworks.html). In stead of using simple rectangles i will create a few shapes to work with.

* Create a rect node and set **Width** to **100.0** and **Height** to **100.0**. Additionally set **Roudness** to **20.0** and **20.0**.
* Create an other rect node and set **Width** to **100.0** and **Height** to **150.0**. Change the **position** on the x-axis to **50.0**.
* Create a rotate node and set the **angle** to **-45.0**. Connect rect2 node with this angle node.
* Create a compound node and send rect1 to the **shape1** port, send rotate1 to the **shape2** port. Set **function** to **Difference**.

Output should be the half of the original rectangle (rect1 node):

![generative step 1](generative-a.png)

I want to be able to use this shape with a difference in rotation. Therefore:

* Create a rotate node. Connect compound1 to it.
* Create a range node. Set **Start** to **0.0**, End to **360.0** and step to **90.0**. Rendering this node will result in a list of numbers: 0,90,180,270.
* Connect range1 to the **angle** port of the rotate node. This will result in 4 paths (have a look at the **data** view to proof this right) all on top of each other but with a variety in rotation. The first one rotates 0 degrees, the second one 90 and so on.
* Create a colorize node and give a **Fill** color and a **Stroke** color. Make shure to set the **Strokewidth** which is **0.0** by default. Set it to **1.0**. The last step will enable you to see the layers better in the viewer pane.

![generative step 2](generative-b.png)

Now let's create something that may represent an eye. 

* Create an ellipse node. Set **Width** to **80.0** and **Height** to **80.0**.
* Create a compound node. Connect rect1 to **Shape1** and ellipse1 to **Shape2**. Set the function to **Difference**.
* Create a colorize node. Connect compound2 to it's **Shape** port.
* I will use ellipse1 for the pupil as well. Create a scale node and set **Scale** to **20.0** and **20.0**.
* Create a combine node and send colorize2 to it's first port, scale1 to it's second one.
* The output of combine1 consists of two paths. Create a group node and send combine1 to it to create a geometry object.

In a later stage i want to be able to select one of these shapes. Next few nodes make this happen:

* Create a combine node and connect colorize1 to it's first port. Connect group1 to it's second one.
* Create a slice node and connect combine2 to it. Set **Size** to **1**. Change the **Start_index** to obtain a different path. From 0 to 3 will select the triangle shapes with their difference in rotation. 4 will return the 'eye' shape.

![generative step 3](generative-c.png)

Our network is getting a bit big so let's create a subnetwork.

* Select all nodes by dragging over them.
* Right-click one of them and choose “group into network”.
* This will leave you with one node, subnet1. Right-click it again a rename "unit".

Let's get back in the childnodes to implement a few modifications. I want to be able to send a number to the **Start_index** of slice1 so i need to publish this specific parameter. I also want to be able to give a unit a location so i will have to implement and publish a translate node:

* Right-click on **Start_index** port (in the networkview) of slice1 and choose "Publish" and give it an appropriate name.
* Create a translate node. Connect slice1 to it's **shape** port.
* Right-click on **translate** port of this new translate node and select "Publish". Select it as rendered node.
* Click on the root tab in the adress bar or right-click somewhere on the network view to choose "Go Up".

Back in the root you should be able to see a modification in the unit node. It has two port: a first one referring to the **Start_index** (a gray one meaning it expects a value) and a second one to **Translate** (a blue one meaning it expects a point).

![generative step 4](generative-d.png)


