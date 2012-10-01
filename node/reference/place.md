---
layout: reference
title: Place Node
image: place
---
Place shapes on points of the template shape. This copies the input from the shape port onto the points of the template port.

The place node is extremely useful because it allows to create many copies based on template geometry. Any shape can be used as the template. It is often convenient to use the [resample](resample.html) node to evenly distribute points on the template shape. See the [copy stamping page](../using/copy-stamping.html) for an example.

* **Copy Stamping**: If checked, use [copy stamping](../using/copy-stamping.html). 
* **Expression**: An optional copy stamping expression.