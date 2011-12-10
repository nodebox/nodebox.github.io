---
layout: documentation
title: Using Expressions
---

**Expressions unlock the power of NodeBox.** They can **create variation** for similar elements or **turn your static poster into a lively animation**.

Getting started
------------------

Expressions dynamically generate parameter values. You turn expressions on per parameter by clicking in the right hand arrow control and selecting “Toggle Expression”.

1. Create a rectangle node: click the “new node” button, type “rect” and press enter.
2. In the height parameter row, click the arrow and choose “Toggle Expression”. The number is now replaced with a yellowish text field.
3. Type the word “width” (without the quotes) and press enter.

The width and height parameters are now linked:

1. Try dragging the width parameter. Note that the height also changes in the viewer.
2. Try dragging the handles on the rectangle. Note that it remains a square.

Using functions
------------------

The NodeBox expression language uses functions for all but the simplest expressions, so it’s good to know what they are.

A function calculates something for you. You call the function with a number of arguments, and it gives you a value back. You can use this value directly, or pass it to another function.

To call a function, write this:

<pre>color(0.3, 0.5, 0.1, 0.95)</pre>

This structure is always the same:

* The first part is the function name. NodeBox has a number of built-in functions, which you can find below.
* After the name come the opening bracket: one at the beginning, one at the end. Even a function with no arguments still uses brackets., i.e. wave()
* Then come the arguments. Each function has a required number of arguments. If you provide too little or too much, NodeBox will complain. You list the arguments in order and separate them using commas.
* Finally, don’t forget the closing bracket!

Here are some other examples of functions:

<pre>hsb(0.5, 0.3, 0.1)</pre> // Create a new color with a hue of 50%, a saturation of 30% and a brightness of 10%. Color values go from 0 to 1.
<pre>random(CNUM, 1, 100)</pre> // Generate a random number between 1 and 100, different for each copy.
<pre>stamp(“mysize”, 100)</pre> // Copy stamp a value. Copy stamping will be explained later.


Combining functions
-------------------

Soon, you will want to **combine multiple functions**. Let’s say that we want to have **a hsb color with a different hue for each copy**. For this, we need to combine functions.

**Combining functions is not special**. You need to apply the same logic as before, but instead you **use a function as an argument**.
Here’s the example:

<pre>hsb(random("CNUM",0.0,1.0), 0.5, 0.8)</pre>

Instead of providing a normal value for the first argument of the hsb function, we provide another function, random, which return a random value for eacht copy between 0.5 and 0.8.

Here’s what NodeBox does to evaluate this:

1. Call the random function. Let’s say this returns the value 0.77.
2. Replace the random function with the output of the function. The function now looks like this: hsb(0.77, 0.5, 0.8)
3. Call the hsb function and return a color object.

To summarize, **NodeBox calculates the inner functions first** and replace the results with the value.

Arithmetic Operators.
--------------------

There are many built-in operators in the NodeBox expression language. Here is a quick reference:

* Add two numbers together.	5 + 3 ==>	8
* Subtract two numbers.	12 - 4 ==>	8
* Divide two numbers.	16 / 2 ==>	8
* Raise a number to a power.	2 ** 3 ==>	8
* Calculates the remainder of a division.	18 % 10	==> 8


Other Math.
----------
A lot of extra math functions are under the “math” package. You can refer to them by prepending “math.”: Those are functions, so use brackets. You can find the complete list of other math functions at the [expression reference page](/documentation/expressions/).

Some examples:
math.sin	The arc sine of an angle.	math.sin(0.5)
math.cos	The arc cosine of an angle.	math.cos(0.3)


Referring to other parameters
-----------------------------

Expressions are useful when they **allow you to link parameters together**.

Let’s say you want to make sure the width and height of an ellipse are always the same. This makes the ellipse into a circle.

We can **link two parameters together by using an expression in one that refers to the other**.

1. Create an ellipse node.
2. Toggle the height parameter to an expression.
3. Type the word “width” (without the quotes) and press ENTER.

The two are now linked. If you drag the width, the height will automatically change. This works both in the viewer and the parameter panel.

What we’ve done is referred to the name of another parameter. **The name is not always the same as the label**, which is what you see in the parameter panel. For example, in the translate node, the **“Scale X”** parameter **is actually called “sx”**.

**To find the name of a parameter, hover your mouse over the label**.

Referring to a parameter from another node.
------------------------------------------

If a parameter is on the same node we can just use the name. But what if we want to refer to a parameter on a different node?
Suppose we want to link the width parameter of two different ellipse nodes together.

1. Create two ellipse nodes.
2. Click on ellipse1 and toggle the width parameter to an expression.
3. Type the word "ellipse2.width" (no quotes) and press ENTER

The two parameters are now linked. Instead of referring to the name of a parameter we referred to (in pseudocode) the_name_of_the_node.the_name_of_the_parameter. The point between them is essential! 

Working with text
-----------------

Pieces of text are called strings. Strings can be used in parameters that expect text, for example the textpath.text parameter.

A string is separated by quotes, like so:
<pre>“hello”</pre>

This is to differentiate it from a keyword, which doesn’t use quotes.

Just as numbers, you can also add strings together:

<pre>“Hello” + “ “ + “there!”</pre>

You always need the quotes, also in functions:

<pre>stamp(“myvalue”, 42)</pre>


Working with lists
------------------

You can create a list by using [] brackets or quotes.

A list can be a word. In this case the n letter of the word hello is called by the number between the brackets.
<pre>"hello"[0]</pre>
returns "h"

A list can be a group of words.
<pre>["word", "sentence", "letter", "paragraph", "book"][3]</pre>
returns "paragraph"

A list can be a group of any type:
<pre>["Verdana", "Zapfino", "Georgia"][1]</pre>
returns  the Zapfino font
<pre>[hsb(.5,.2,.1), hsb(.9,.6,.8)][1]</pre>
returns a pink-like color

You can **call an item in the list** by using a number as shown above or over the stamp function.

Example with copy stamping. 
<pre>["word", "sentence", "letter", "paragraph", "book"][stamp("num", 0)]</pre>


Special Expressions.
--------------------

Some of the expressions have a separate page. More information on copy stamping, data stamping and animation is on these pages:

* Read the [copy stamping](expressions.html) page for general information on copy stamping.
* Read the [animation](animation.html) page for general information on animation.
* Read the [expression reference](/documentation/expressions/) for detailed information on every expression or animation function.
* Look at MVEL language guide: <http://mvel.codehaus.org/Language+Guide+for+2.0>