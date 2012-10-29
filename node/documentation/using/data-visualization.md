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
* Create a line node.


![data random numbers](data-visualization-random-numbers.png)