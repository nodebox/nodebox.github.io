---
layout: documentation
title: Using Expressions
---
Every parameter in NodeBox can use expressions. This allows you to:

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
The NodeBox expression engine is built using MVEL, an open-source expression library. Everything MVEL supports, NodeBox supports. Check out the [language guide](http://mvel.codehaus.org/Language+Guide+for+2.0) for more information.