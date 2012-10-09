---
layout: documentation
title: Working with Math
---
TODO
====
* Trigonometry: sine, cosine
* Absolute values
* Min/max

Nodebox allows you to create a range of different paths and functions based on sine and cosine. The next example shows how to create a Lissajous path which is based on the parametric equations

    A*sin(t)
    B*sin(t/n)

Create a [sample node](/node/reference/math/sample.html) to start with a set of numbers.

* Set **Amount** to **1000**.
* Set **End** to **15.00**.

Create two [multiply nodes](/node/reference/math/multiply.html) and send the sample node to each one of them.

* Set **Value2** to **10.84** for the first one.
* Set **Value2** to **10.00** for the second one.

Create two [sin nodes](/node/reference/math/sin.html) and send the multiply nodes respectively to the first one and the second one.

Create two more multiply nodes and send the sin nodes to them. These two multiply nodes will handle the width and height of the Lissajous path. You can rename them by using right click and select the rename option.

Create a [make point node](/node/reference/math/make_point.html).

* Send the first multiply node to the x port.
* Send the second one to the y port.

Create a [connect node](/node/reference/corevector/connect.html) and send the make point node to it. Finnally create a [colorize node](/node/reference/corevector/colorize.html) to give the path a fill and stroke color.

![Lissajous](math-lissajous.png)


