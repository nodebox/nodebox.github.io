---
layout: documentation
title: Expressions Reference
---

Basic arithmetic
----------------
<!-- We use HTML here because the operators mess with Markdown. -->
<ul>
  <li><strong>+</strong>: Add two numbers. <pre>2 + 3 //=> 5</pre></li>
  <li><strong>-</strong>: Subtract two numbers. <pre>5 - 4 //=> 1</pre></li>
  <li><strong>*</strong>: Multiply two numbers. <pre>3 * 4 //=> 12</pre></li>
  <li><strong>/</strong>: Divide two numbers. <pre>12 / 3 //=> 4</pre></li>
  <li><strong>%</strong>: Calculate the remainder of dividing two numbers. <pre>12 / 5 //=> 2</pre></li>
  <li><strong>**</strong>: Calculate a number to the nth power: <pre>2 ** 5 //=> 32</pre></li>
</ul>

Numerical expressions
---------------------
* **random**: Create a random value.
* **randint**: Create a random integer.
* **int**: Convert the value to an integer.
* **float**: Convert the value to a floating-point number.
* **clamp**: Forces the number to be in the given range.
* **color**: Create a color using RGBA. Same as the rgb() function.
* **rgb**: Create a color using RGBA.
* **hsb**:Create a color using HSBA.


Animation expressions
---------------------
* wave
* hold
* schedule
* timeloop

Copy stamping
------------
* stamp

Lists
-----
Use the [] syntax to create lists.
  
Math
----
* math.PI
* math.E
* math.abs
* math.acos
* math.atan
* math.atan2
* math.cbrt
* math.ceil
* math.cos
* math.cosh
* math.exp
* math.expm1
* math.floor
* math.getExponent
* math.log
* math.log10
* math.log1p
* math.max
* math.min
* math.pow
* math.rint
* math.round
* math.scalb
* math.signum
* math.sin
* math.sinh
* math.sqrt
* math.tan
* math.tanh
* math.toDegrees
* math.toRadians
* math.ulp

Text
----
* **trim()**: strip off spaces at the beginning and end of the string: <pre>"  hello ".trim() //=> "hello"</pre>

Conditions
----------
* Ternary operator: <pre>width &lt; 50 ? "small" : "large"</pre>

