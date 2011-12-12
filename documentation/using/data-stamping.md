---
layout: documentation
title: Data Visualization using Data Stamping
---
The functionality of the data stamp is powerful, but might take some time to understand. In this tutorial, we'll walk you through creating a simple data visualization.

First off, you need data to visualize. We've provided you with a list of the 14 tallest buildings in the world. Download this file and put it in a project folder. We'll call ours "buildings".

File: [tallest_buildings.csv](/media/ndbx/using/tallest_buildings.csv).

The datastamp node can work in two ways. You can use a template to define where the different shapes will appear. The number of points in the template should match the number of rows in the file (minus the header row).
You can also use the datastamp node without the template. This allows for more powerful visualizations, but might require a bit more of upfront thinking. In this case, we have to move the shapes in place ourselves. We can do this using a transform node, for example. Use the expression stamp("data_row_index", 0) or stamp("data_row_position", 0) as the expression for the X or Y coordinate.

* Make sure the NDBX file and CSV file are in the same directory. For this, create a new file and save it immediately in your project folder. Check that the CSV file is in the same folder.
* Create a **Datastamp** node. Leave this node as the rendered node during the course of the project.
* In datastamp1, select the file button (the "..." button) and choose the CSV file.
* The datastamp1 node is now active, but nothing is showing yet, because there's no shape input.
* Create a **Textpath** node. Connect **textpath1** to **datastamp1** (shape). 
* Make the datastamp node the rendered node. If you look carefully, you can see that the text appears fatter. This is because multiple text objects are created on top of each other.
* Create a **Line** node. Set **Points** to **14** (same as the number of rows in the file), **Angle** to **90.00** and **Distance** to **300.00**.
* Connect **line1** to **datastamp1** (template).
* Double-click **datastamp1** to make it the rendered node. You should now see the world "hello" appear 20 times, below each other.

So, where is our data? Well, NodeBox is executing the datastamp node for each row in our file. However, we haven't told NodeBox yet where to use the data from the file. We can do this using an expression like this:
<pre>stamp("data_value_2", 0)</pre>

The data_value_2 refers to the number of the column, starting from 0 (so **data_value_0** is column 1 and **data_value_2** is actually column 3). 

We can use the stamp expression everywhere: if the value of the column is a number, you can use it wherever there are numbers (for example, as the X position of a rectangle, or the rotation of a transform, or the number of points in a star). If the value in the column is a piece of text, you could use this for the text path node. We'll do this now.

* In **textpath1** set **Text** to the expression <pre>stamp("data_value_0", "hello")</pre>
* Don't forget to press enter after typing the expression to confirm it.

If all went well, you should see 14 different text strings, each for every line in the file. Compare it to the data in the file itself. Note that NodeBox skips the header row.

The expression consists of a function call to the stamp expression. The function stamp takes two *arguments*:

- **data_value_0** is the first argument. It means that we want the data value from the first column (remember, NodeBox starts counting from zero) for each row in the file. 
- **"hello"** is the second argument. It is a *default value*. The stamp expression tries to find the current value of "data_value_0" in the processing context. This value only exists if we're rendering a datastamp node. If the textpath node is the rendered node, there is no "data_value_0" available, and so the stamp function uses the default value.

* In **textpath1** set **Text** to the expression <pre>stamp("data_value_1", "hello")</pre>

You'll notice that we now see the values in the second column (the cities) instead of the first column.

* In **textpath1** set **Text** back to the expression <pre>stamp("data_value_0", "hello")</pre>

The 14 pieces of data are all aligned according to the points of the template. This means that, if we change the look of the template, the data will follow as well.

* In **line1** set **Distance** to **380.00**. Note that the text paths are now spaced further apart.
* Also in **line1** set **Angle** to **45.00**. You'll see that the text paths follow the angle of the line.

Data stamping on a circle.
==========================
It has become sort of a ritual to use circles as a first "cool" data visualization. Let's make one ourselves.

* We'll work on the same file as before.
* Create an **Ellipse** node. Set **width** and **height** to **300.00**.

Just as with the place node, we use the points of the template to place the shapes. However, a normal circle only has a few points. We need a resample node to give us points that lie on the circle.

* Create a **Resample** node. Set **Method** to **By Amount** and **Points** to **14**. This will create 14 points, the same as the number of rows in our file.
* Connect **ellipse1** to **resample1**. 
* Connect **resample1** to **datastamp1** (template).
* Double-click datastamp1 node to make it the rendered node. 

You should now see all the textpath, in some kind of circle, but overlapping. What happened? Well the shapes only get moved to the template point, not rotated according to their position on the circle. Their angle doesn't change and this means they'll overlap. 

We can fix this, not in the template, but in the shape. We'll put a transform node inbetween the textpath and the datastamp and change its angle.

* Create a **Transform** node.
* Connect **textpath1** to **transform1**
* Connect **transform1** to **datastamp1** (shape). The transform node now sits in between the text path and the datastamp.
* Double-click datastamp1 to make it the rendered node. 
* In **transform1** drag the **Angle**. Note that all text paths now rotate equally.

Obviously, each text path should rotate differently. But different to what? We basically want them to create a full circle. A full circle is 360 degrees. So basically, we want to distribute our shapes along 360 degrees. 

To do this, we need to connect the angle to where we are in the file. The first row should not be rotated at all. The middle row (row 10) should be rotated 180 degrees, or half a circle. The last row should complete the circle.

The datastamp node provides two stamp variables that make this possible. The first one, data_row_index, provides the index number of the row. So, for the first row, this number will be 0 (as NodeBox counts from zero). For the second row, the index will be 1, and so forth. If we know the number of lines in the file, we could calculate the relative angle for each index. 

But datastamp can do this for us. The second stamp variable is data_row_position. It is a *relative* value between 0.0 and 1.0. The first row in the file has a position of 0.0. The last row in the file has position 1.0. The middle row (row 10) has a position of 0.5. This is exactly what we need for our project.

* In **transform1** set the **Rotate** to the expression <pre>stamp("data_row_position", 0) * 360</pre>

Voila! The elements are now rotated a full 360 degrees, or a whole circle.

* Apply finishing touches: In **textpath1** set **Align** to **Right**.

Multiple elements
=================
So far, we have shown only one element for each row: the textpath. What if we want to show more? Obviously we want to show the height of each building. We'll create abstract buildings that represent the height of the real building.

We need to create a complete element before we pass it to to the datastamp node. This means we should *merge* the output of multiple shapes, like a textpath and shape, and connect this merge to the shape of the datastamp node.

We have a nice base visualization that we'll built from scratch.

* Make sure the NDBX file and CSV file are in the same directory. For this, create a new file and save it immediately in your project folder. Check that the CSV file is in the same folder.
* Create a **Datastamp** node. Leave this node as the rendered node during the course of the project.
* In datastamp1, select the file button (the "..." button) and choose the CSV file.
* Create a **Line** node. Set **Distance** to **380.00** and **Points** to **14** (the number of rows in the file).
* Connect **line1** to **datastamp1** (template).
* Create a **Rect** node. Set **Width** to **1.00** and **Height** to **10.00**.
* Create a **Copy** node. Set **Copies** to the expression <pre>1+stamp("data_value_2", 1)/10.0</pre>
* In **copy1** set **Translate Y** to **5.00** and **Scale X** to **40.00**.
* Connect **copy1** to **datastamp1** (shape).

![Data Stamping Unaligned](/media/img/using/data-stamping-unaligned.png)

All buildings are represented as symbolic buildings. It starts out at the top as a very small spire and moves down (that's what translate Y does) and becomes wider (that's what scale X does). The number of copies is the height of each building, divided by 10.

The buildings are obviously not aligned to the bottom. Let's change that:

* Create an **Align** node. Set **Horizontal Align** to **Center**.
* Connect **copy1** to **align1**.
* Connect **align1** to **datastamp1** (shape).

Now the buildings are aligned to the origin:

![Data Stamping Unaligned](/media/img/using/data-stamping-aligned.png)

Let's combine them with the text path. The text should be next to the top of the building so it needs to be translated up the same size as each building. Since we create *building height / 10* copies, and each copy is translated 5 points, the total height will be *building height / 2*.

* Create a **Textpath** node. Set **Size** to **10.00**, **Align** to **Left** and **Text** to the expression <pre>stamp("data_value_0","none")</pre>
* Create a **Transform** node. Set **Rotate** to **-45.00** and **Translate Y** set to the expression <pre>-stamp("data_value_2", 0)/2</pre>
* Connect **textpath1** to **transform1**.

And finally we'll merge the two:

* Create a **Merge** node.
* Connect **textpath1** to **merge1**.
* Connect **align1** to **merge1**.
* Connect **merge1** to **datastamp1** (shape)

![Data Stamping Buildings](/media/img/using/data-stamping-buildings.png)

In conclusion, data stamping is powerful and pretty straightforward. It just creates a new shape for every row in the data file, and sets its stamping variables accordingly. It is your job to use these stamping variables to influence your composition by using them as expressions, for instance to change the size of a shape or text of a textpath.

For more information, refer to the [datastamp reference](/documentation/nodes/datastamp.html) which has a list of all available stamp variables.
