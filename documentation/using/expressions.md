---
layout: documentation
title: Using Expressions
---
**Expressions unlock the power of NodeBox.**  Every parameter in NodeBox can use expressions. This allows you to:

- **Refer to other parameters** on your own node or on other nodes
- **Use basic math** to create interesting effects
- **Use animation** by linking the parameter to the current frame.

The expression language is powerful and has support for arithmetic, functions and lists.

Toggling Expressions
--------------------
To use expressions, you need to toggle it for that parameter.

![Toggle Expression](/media/img/using/expressions-toggle.png)

* Create a **Rect** node.
* For the **Height** parameter, go to the down-arrow menu to the right and select **"Toggle Expression"**.
* The height field now turns into a text field with a yellow background. This means we're using expressions.
* Type "width" (without the quotes) and hit enter.
* Try changing the width parameter. Note that the height also moves, resulting in a square.
* Try **dragging** the edges of the rectangle. Note that you can only move it in a square-like fashion.

Expressions can refer to other parameters using their **short name**. Often, this is the name of the parameter in lowercase, but not always. To see the short name, *hover over the parameter name*:

![Viewing The Internal Name](/media/img/using/expressions-internal-name.png)
<small>Hover over the parameter name to see the <em>short name</em>.</small>

Names are always case-sensitive: differences in upper- and lowercase matter.


Referring To Other Nodes
------------------------
Often it makes sense two have two objects relate to each other.

To relate one parameter to another, between nodes, use the syntax:

    nodename.shortname
    
For example: **rect1.width**

* Create an **Ellipse** node. Set **Y** to **-75.00**.
* Create a **Rect** node. Set **Y** to **-100.00** and **Height** to **150.00**.
* We want the rectangle to move together with the ellipse. In **rect1** set **X** to the expression <pre>ellipse1.x</pre>
* In **elipse1**, drag the **X** parameter. Note that the rectangle follows along.

The node name is the name you see below the node. You can rename nodes by double-clicking the name or right-clicking the node and choosing "Rename". Note that existing expressions will not be changed.

When copy-pasting nodes, expressions are not updated to new, internal names.

Arithmetic Operations
---------------------
You can use basic arithmetic, such as adding, subtracting, dividing etc.

Here's an example:

* Create a **Rect** node.
* Set **Height** to the expression <pre>width * 2</pre>
* Every time you move the width, the height becomes double as large.

![Expressions Arithmetic](/media/img/using/expressions-arithmetic.png)
<small>The height of the rectangle is always double the width.</small>

The [expression reference](../expressions/) has a more detailed explanation of all mathematical operations.

Using Functions
---------------
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


Other Math
----------
A lot of extra math functions are under the “math” package. You can refer to them by prepending “math.”: Those are functions, so use brackets. You can find the complete list of other math functions at the [expression reference page](/documentation/expressions/).

Some examples:
math.sin	The arc sine of an angle.	math.sin(0.5)
math.cos	The arc cosine of an angle.	math.cos(0.3)

Working with Text
-----------------
Pieces of text are called strings. Strings can be used in parameters that expect text, for example the textpath.text parameter.

A string is separated by quotes, like so:
<pre>“hello”</pre>

This is to differentiate it from a keyword, which doesn’t use quotes.

Just as numbers, you can also add strings together:

<pre>“Hello” + “ “ + “there!”</pre>

You always need the quotes, also in functions:

<pre>stamp(“myvalue”, 42)</pre>


Working with Lists
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

Built-in Variables
------------------
NodeBox has a number of built-in variables you can use in expressions. These are all written in UPPERCASE to distinguish them from parameter names. They are:

- **FRAME**: The current frame. See [using animation](animation.html) for more explanation.
- **WIDTH**: Width of the document, as defined in the document properties.
- **HEIGHT**: Height of the document, as defined in the document properties.

Errors in Expressions
---------------------
It happens. You make a mistake in an expression and the node turns red. How can we fix this error?

NodeBox reports expression errors in the *source pane*. But due to a bug, the pane does not update automatically. In the *network pane* you have to click away from the node (by clicking on the background), then click again on the node with the error.

Let's show this in action by referring to a parameter that does not exist:

* Create a **Rect** node.
* Set **Height** to the expression (notice the typo) <pre>wit</pre>
* The node turns red indicating there's an error. 
* Click *away* from the node, on the network pane background. This deselects the node.
* Now click the node *again*. You should see the following error in the source pane:

![Expressions Error](/media/img/using/expressions-error.png)

The errors are often cryptic. Here, NodeBox is complaining about not being able to access "wit", which should provide some clue that the parameter name is wrong.

More Information
----------------
Some of the expressions have a separate page. More information on copy stamping, data stamping and animation is on these pages:

* Read the [copy stamping](copy-stamping.html) page for general information on copy stamping.
* Read the [animation](animation.html) page for general information on animation.
* Read the [expression reference](/documentation/expressions/) for detailed information on all built-in expressions.
* The NodeBox expression engine is built using MVEL, an open-source expression language. Everything MVEL supports, NodeBox supports. Check out the [MVEL Language Guide](http://mvel.codehaus.org/Language+Guide+for+2.0) for more information.
