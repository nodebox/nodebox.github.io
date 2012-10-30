---
layout: documentation
title: Creating Data Visualizations
---

Random numbers.
------------------

Nodebox can be used to create data visuals. We will go over a few prinicples but let's first visualize a set of random numbers.

* Create a random numbers node. Set **Amount** to **15** and **End** to **200.0**.
* Create a rect node. Set **Height** to **20** and connect random numbers1 to **Width**.
* Create a count node and connect random numbers1 to it. We will use this to create a set of random colors and as an amount of points on a line node.
* Create a line node. Set **Point2** to **0.0** and **300.0**, returning a line going straight down.
* Create a resample node to make a list of points on it. Set **Method** to **amount**. Connect count1 to **Points** and connect line1 to **Shape**.
* Create a translate node and connect rect1 to *Shape** and resample1 to **Points**. Double click it to see the result.

![data random numbers step 1](data-visualization-random-numbersa.png)

Let's clean this up a bit with some extra nodes.

* Create a colorize node and put connect rect1 to it. We will give it a colour based on the weight of the random number as a color value.
* Create an align node. Set **Halign** to **Left** and **Valign** to **Middle**. Connect colorize1 to it and connect it to **Shape** of translate1.
* Create a hsb colour node. Set **Hue** to **150.0** and **Saturation** to **173.0**. Connect randomnumbers1 to **Brightness**.
* Connect hsb coulour1 to **Fill** of colorize1.
* Render translate1.
* Change **Seed** of random numbers1 to change the set of random numbers and thus the visualization.

![data random numbers step 2](data-visualization-random-numbersb.png)