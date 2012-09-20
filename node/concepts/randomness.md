---
layout: documentation
title: Controlling Randomness
---
TODO
====
* Update screenshots
* Remove part about code (not implemented yet)

Randomness in NodeBox is not really random. It produces pseudo-random values controlled by an initialization value called the **seed**.

Each seed produces a different range of random numbers. **The same seed will always give the same collection of random numbers.** That's why we talk about *controlled* randomness: within a certain collection, the ordering *appears* random:

* Seed 1: 14 85 77 26 50 45 66 79 10 3
* Seed 2: 96 95 6 9 84 74 67 31 61 61
* Seed 3: 24 55 37 61 63 7 2 84 26 24

This is actually very useful. As a designer, you might pick a certain random variation that you think looks good. It wouldn't make much sense if NodeBox would change the output when you reopen the document. The seed gives us a way of *creating variation without giving up control*.

Everywhere a NodeBox node uses a random value, it provides a seed parameter for you. Nodes such as [wiggle][], [scatter][] and [sort][] will always produce the same result for the same seed.

Here's an example:

* Create a **star** node. Set the **X** to **-120.00** to move it to the left.
* Create a **wiggle** node. Set the **Seed** to **1**.
* Connect **star1** to **wiggle1**.
* Select the two nodes, copy them, and paste them again. 
* **Double-click wiggle2** to make it rendered.
* In **star2**, set the **X** to **120.00** to move it to the right.
* Create a **merge** node.
* Connect **wiggle1** to **merge1**.
* Connect **wiggle2** to **merge1**.

If you look at the output of the merge node, you'll see that they both have the same random variation. That's because they share the same random seed.

![Same wiggled stars](/media/img/using/randomness-wiggle.png)

In **wiggle2**, change the **seed** to 2. Note that the two stars now look different.

![Same wiggled stars](/media/img/using/randomness-wiggle2.png)

**The actual number of the seed is unimportant.** Seed 10 is not "more random" than seed 1. See it as the index number of a certain variation.

Using seed in your own nodes
----------------------------
When you're [programming your own nodes](../advances/programming-nodes.html) that use random values, add a "seed" parameter using the metadata menu and add the following line right below the cook method:

<pre>
  from random import seed
  
    def cook(self):
        seed(self.seed)
        ...
</pre>

NodeBox nodes are evaluated lazily, and producing "true" random numbers breaks this model. Using a seed parameter makes your nodes [idempotent](http://en.wikipedia.org/wiki/Idempotence).


[wiggle]: /documentation/nodes/wiggle.html
[scatter]: /documentation/nodes/scatter.html
[sort]: /documentation/nodes/sort.html
