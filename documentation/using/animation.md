---
layout: documentation
title: Animation
---

You should already have read the [tutorial on basic animation](/documentation/tutorial/animation.html). This pages goes into more detail and shows tricks and techniques.

Conceptually, NodeBox animation is very easy to understand. Every frame, NodeBox sets the value of FRAME to the current frame number. By referring to FRAME in expressions, you can create animations.

Here's a basic example:

* Create a **Rect** node.
* Create a **Transform** node.
* Connect **rect1** to **transform1**.
* Toggle the **Rotate** parameter to an expression. Type the word <code>FRAME</code> (in capitals) and press enter.
* Press **Play** to start the animation.

![Animation Rotate Expression](/media/img/using/animation-rotate-expression.png)

We've linked the rotation to the current FRAME:

* At frame **1**, the rotation will be **1**.
* At frame **2**, the rotation will be **2**.
* At frame **3**, the rotation will be **3**.
* And so on.

What if we want to make the animation go faster and slower? Expressions allow for math operations, much like Excel formulas.

To make the animation ten times slower, use the expression **FRAME / 10**:

* At frame **1**, the rotation will be **0.1**.
* At frame **2**, the rotation will be **0.2**.
* At frame **3**, the rotation will be **0.3**.

To make the animation ten times faster, use the expression **FRAME * 10**:
  
* At frame **1**, the rotation will be **10**.
* At frame **2**, the rotation will be **20**.
* At frame **3**, the rotation will be **30**.

We deliberately choose the rotate parameter because it loops: a rotation is 360 degrees (a full circle) is equal to a rotation of 0. But not all parameters work this way. If we would connect the rectangle's width to the current frame, it would just keep getting wider. This is where wave expressions become useful.

By the way, if you really want to use animation effectively you should learn how to [use expressions](expressions.html). This page shows expression functions specific to animation.


Wave Expressions
----------------
Wave expressions are basic sine, triangle and sawtooth waves. These are *oscillating* curves: they go from their minimum to their maximum and back. The following waves are built in:

![Built-in Animation Waves](/media/img/using/animation-waves.png)

From the top:

- A **sine wave** performs a smooth movement.<br>
  **wave(SINE, 0, 50, 100)**
- A **triangle wave** performs a linear movement.<br>
  **wave(TRIANGLE, 0, 50, 100)**
- A **square wave** goes from one extreme to the other.<br>
  **wave(SQUARE, 0, 50, 100)**
- A **sawtooth wave** goes linearly from the maximum to the minimum, then jumps back.<br>
  **wave(SAWTOOTH, 0, 50, 100)**

Wave expressions are inevitable for animation. Here's a small example:

* Create a **Rect** node. 
* Set **Width** to **2.00**.
* Set **Y** to the expression <pre>wave(SINE, -100, 100)</pre>

Play the animation. The rectangle now moves smoothly up and down between the Y value -100 and 100. You can change the speed of the animation by adding an extra argument to the function:

* Set **Y** to the expression <pre>wave(SINE, -100, 100, 300)</pre>

This argument defines the time it takes to go from the minimum to the maximum value and back, called the period. The default period is 100. By setting it to 300, we made the animation 3 times slower.

* Create a **Copy** node. Set **Copies** to **50** and **Translate X** to **10.00**.
* Connect **rect1** to **copy1**.

Play the animation. All rectangles move up and down together, since they all use the same start offset. We can change this using [copy stamping](copy-stamping.html).

* In **copy1**, turn on **Copy Stamping**.
* In **rect1**, set **Y** to the expression <pre>wave(SINE, -100, 100, 300, FRAME + stamp("CNUM", 0) * 20)</pre>

Play the animation. All the rectangles now start at a different point in the wave.

![Animation Sine](/media/img/using/animation-sine.png)

Reference: [wave](/documentation/expressions/)


Waiting for the right moment
----------------------------
Sometimes you want to wait with playing an animation until the frame reaches a certain value.

As an example, imagine *a car race where the drivers still need to find the keys to the car*. Each of them would start at a different time.

Each car is represented as a rectangle. We'll need to link the X value to the FRAME. But this means they all start at the same time. Using the FRAME minus a different random value for each car (e.g. FRAME-45) would would make some cars start later, but they would not all start at the same position.

Meet the **hold** expression. It doesn't change the value until the frame reaches a certain threshold. The hold function returns a *default* value (possibly 0) when the frame is smaller than the threshold, and a different value when the frame is larger than the threshold.

![Animation Schedule](/media/img/using/animation-hold.png)

To create our car example:

* Create a **Rect** node. Set **Height** to **45.00**.
* Create a **Copy** node. Set **Copies** to **5** and **Translate Y** to **70.00**.
* Connect **rect1** to **copy1**.
* In **copy1** turn on copy stamping. In **Expression** set **car** &rarr; **CNUM**.
* In **rect1** set **X** to the expression <pre>hold(stamp("car", 0) * 50, FRAME)</pre>

Play the animation. The first car starts moving immediately – the other cars each start a bit later.

Note that we've used a function inside of another function. This is very powerful and potentially confusing. If you haven't yet, read the [expression documentation](expressions.html) for more information.

Further changes:

* The cars always start from top to bottom. To change this, in **copy1** change the expression to **car** &rarr; **random(CNUM, 0, 5)**. Because the index is now random, the order of the cars is also random.

In the next example we use the hold function to schedule elements progressively. By combining *hold* and *wave*, we can create some interesting effects:

* Create a **Rect** node.
* Set **Width** to the expression <pre>hold(stamp("index", 0) * 30, wave(TRIANGLE, 0, 20))</pre>
* Set **Height** to the expression **width**.
* Set **Fill** to transparent white. (Alpha = 200)
* Set the document's **Background Color** to dark blue (Red = 0, Green = 0, Blue = 20)
* Create a **Textpath** node. Set **Size** to **200.00**.
* Create a **Resample** node. Connect **textpath1** to **resample1**.
* Create a **Sort** node. Set **Scope** to **Points within geometry**, **Order** to **Shift** and **Offset** to the expression **FRAME**. Connect **resample1** to **sort1**.
* Create a **Place** node.
* Connect **rect1** to **place1 (shape)**.
* Connect **sort1** to **place1 (template)**.

Play the animation. After a few frames, a rectangle should start following the shape of our textpath. The more we go down our animation, we see more rectangles appear. 

![Advanced Schedule Example](/media/img/using/animation-hold-hello.png)

Let's dissect the arguments to the hold function:

* **startFrame**: stamp("index", 0) * 30  -- Set the start frame to be the index, multiplied by 30. This starts every element 30 frames apart from each other.
* **functionValue**: wave(TRIANGLE, 0, 20) -- A standard triangle wave function.

Reference: [hold](/documentation/expressions/)


Scheduling some time
--------------------
The schedule function is quite similar to the hold function. Hold only has a minimum value: schedule has a *start* and *end* value where the value of the schedule is used. Also, schedule 

A simple example:

* Create a **Rect** node.
* Set **Height** to the expression <pre>schedule(100, 200, FRAME, 10)</pre>

Play the animation. Note that in the first 100 frames, nothing happens (the height uses the default value of 10). Only between frame 100 and 200 does the height increase. This is the function of schedule.

If we have multiple elements on screen, we can use schedule in each of them to make them visible.

However, if you want to make elements visible one after another, you could also use a [switch node](/documentation/reference/switch.html).

Reference: [schedule](/documentation/expressions/)

Looping Time
------------
The timeloop function allows you to go through a list of predefined values at a certain speed.

* Create a **Rect** node.
* Set **X** to the expression <pre>timeloop(10, [0, 10, 20, 30, 40])</pre>

Play the animation. Every 10 frames, timeloop chooses the next element in the list. After the last element the function wraps around and chooses the first element again.

Reference: [timeloop](/documentation/expressions/)


More Information
----------------
* Read the [using expressions](expressions.html) page for general information on expressions. This is also useful when creating animations.
* Read the [expression reference](/documentation/expressions/) for detailed information on every animation function.