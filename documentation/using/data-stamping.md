---
layout: documentation
title: Data Visualization using Data Stamping
---
data set: tallest buildings in the world?

The functionality of the data stamp is powerful, but might take some time to understand. In this tutorial, we'll walk you through creating a simple data visualization.

The datastamp node can work in two ways. You can use a template to define where the different shapes will appear. The number of points in the template should match the number of rows in the file (minus the header row).
You can also use the datastamp node without the template. This allows for more powerful visualizations, but might require a bit more of upfront thinking. In this case, we have to move the shapes in place ourselves. We can do this using a transform node, for example. Use the expression stamp("data_row_index", 0) or stamp("data_row_position", 0) as the expression for the X or Y coordinate.


0. make sure the NDBX file and CSV file are in the same directory. For this, create a new file and save it immediately in your project folder. Put the CSV file in the same project folder.
1. Create a new "datastamp" node. This node will be the "rendered" node during the course of our project.
2. In the datastamp node, select the file button (the "..." button) and choose the CSV file.
3. The datastamp node is now active, but nothing is showing yet, because there's no shape to repeat.
4. Create a textpath node and connect it to the *shape* of the datastamp node. 
5. Make the datastamp node the rendered node. If you look carefully, you can see that the text appears fatter. This is because multiple text objects are created on top of each other.
7. Create a line node. Set the number of points to "20" and the angle to 90.
8. Connect the line node to the *template* of the data stamp node.
9. Double-click the datastamp node to make it the rendered node. You should now see the world "hello" appear 20 times, below eachother.

So, where is our data? Well, NodeBox is executing the datastamp node for each row in our file. However, we haven't told NodeBox yet where to use the data from the file. We can do this using the stamp("data_value_2", 0) expression, where the "2" is the number of the column, starting from 0 (so data_value_0 is column 1 and data_value_2 is actually column 3). We can use the stamp expression everywhere: if the value of the column is a number, you can use it wherever there are numbers (for example, as the X position of a rectangle, or the rotation of a transform, or the number of points in a star). If the value in the column is a piece of text, you could use this for the textpath node. We'll do this now.


10. Click the textpath node once. This will select the textpath but keep the datastamp node rendered. (If this is not the case, double-click the datastamp node to make it rendered again, then click textpath once.)
11. Click the drop-down arrow to the right of the "text" field and choose "Toggle Expression". The text field now turns slightly yellow, indicating that it takes an expression.
12. Remove everything in the field and type:

  stamp("data_value_0", "hello")

And press enter to confirm. If all went well, you should see 20 different text strings, each for every line in the file. Compare it to the data in the file itself. Note that NodeBox skips the header row.

The expression consists of a function call to the stamp expression. The function stamp takes two *arguments*:

- "data_value_0" is the first argument. It means that we want the data value from the first column (remember, NodeBox starts counting from zero) for each row in the file. 
- "hello" is the second argument. It is a *default value*. The stamp expression tries to find the current value of "data_value_0" in the processing context. This value only exists if we're rendering a datastamp node. If the textpath node is the rendered node, there is no "data_value_0" available, and so the stamp function uses the default value.

13. Try changing the expression to 

  stamp("data_value_1", "hello")

  (Don't forget to press enter). You'll notice that we now see the values in the second row instead of the first row.

  After you're done, change it back to:

  stamp("data_value_0", "hello")

The 20 pieces of data are all aligned according to the points of the template. This means that, if we change the look of the template, the data will follow as well.

14. In the line node and change the distance to 200. Note that the text paths are now spaced further apart.
15. In the line node, drag the angle to 45. You'll see that the text paths follow the angle of the line.

Data stamping on a circle.
==========================
It has become sort of a ritual to use circles as a first "cool" data visualization. Let's make one ourselves.

1. Using the previous file, create an ellipse node. Set the width and height to 300.

Just as with the place node, we use the points of the template to place the shapes. However, a normal circle only has a few points. We need a resample node to give us points that lie on the circle.

2. Create a resample node. Set the method to "by amount" and the amount to 20. This will create 20 points, the same as the number of lines in our file.

3. Connect the output of the ellipse to the input of the resample node. 
4. Connect the output of the resample node to the template port of the datastamp node.
5. Double-click the datastamp node to make it the rendered node. 
   You should now see all the textpath, in some kind of circle, but overlapping.

What happened? Well the shapes only get moved to the template point, not rotated according to their position on the circle. Their angle doesn't change and this means they'll overlap. 

We can fix this, not in the template, but in the shape. We'll put a transform node inbetween the textpath and the datastamp and change its angle.

6. Create a transform node (The transform node takes a while to load the first time). Connect the output of the textpath node to the input of the transform node. Then, connect the output of the transform node to the shape port of the datastamp node. The transform node now sits inbetween the textpath and the datastamp.

7. Double-click the datastamp node to make it the rendered node.  Now drag the angle on the transform node. Note that all text paths now rotate equally.

Obviously, each text path should rotate differently. But different to what? We basically want them to create a full circle. A full circle is 360 degrees. So basically, we want to distribute our shapes along 360 degrees. 

To do this, we need to connect the angle to where we are in the file. The first row should not be rotated at all. The middle row (row 10) should be rotated 180 degrees, or half a circle. The last row should complete the circle.

The datastamp node provides two stamp variables that make this possible. The first one, data_row_index, provides the index number of the row. So, for the first row, this number will be 0 (as NodeBox counts from zero). For the second row, the index will be 1, and so forth. If we know the number of lines in the file, we could calculate the relative angle for each index. 

But datastamp can do this for us. The second stamp variable is data_row_position. It is a *relative* value between 0.0 and 1.0. The first row in the file has a position of 0.0. The last row in the file has position 1.0. The middle row (row 10) has a position of 0.5. This is exactly what we need for our project.

8. In the angle parameter, click the drop-down arrow to the right and select "Toggle Expression". Type:

  stamp("data_row_position", 0) * 360

  Voila! The elements are now rotated a full 360 degrees, or a whole circle.

9. Apply finishing touches: select the textpath node and set the alignment to "right".

Multiple elements
=================
So far, we have shown only one element for each row: the textpath. What if we want to show more? For example, we want to show the height of each building using the height of a rectangle.

We need to create a complete element before we pass it to to the datastamp node. This means we should *merge* the output of multiple shapes, like a textpath and rectangle, and connect this merge to the shape of the datastamp node.

Since we're working with a circle, we want both the rectangle and textpath to be rotated. In our example, the merge would go *before* the transform.

1. Create a new rectangle node.
2. Create a new merge node.
3. Connect the rectangle node to the merge node.
4. Connect the textpath node to the merge node.
5. Connect the merge node to the transform node.
6. Double-click the datastamp node to make it the rendered node.

   We now should see a rectangle, together with a textpath, for each row in the file.

   Because we didn't use a stamp expression in the rectangle, we won't see any difference. 
   
The height of each building in our data file is in the second column. This means we can refer to it from NodeBox using stamp("data_value_1", 0).

7. Select "Toggle Expression" in the width field of the rectangle. For the expression, type:

  stamp("data_value_1", 100)

  Why do we use 100 for the second argument here? Basically, the second argument is the value of whatever the parameter was before. In other words, we use the default value for this parameter as the default value for the stamp expression. Because the width parameter was 100, we use 100 here.

  We should now see a different width for each rectangle. However, it looks like they're moving from the middle. This is because all nodes in NodeBox work from the canvas origin: the middle of the composition. The width increases in both directions. 

  We can fix this by using an align node. It will align the rectangle to the left.

8. Create a new align node. Connect the rectangle node to the align node.

   Whenever we connect one node to another, any previous connection is removed automatically. However, since the merge node can take *multiple* connections, this doesn't work. We should remove the original connection from the rectangle to merge first.

9. Click the connection line between rectangle and merge. It should light up blue. Hit backspace to remove it. 

  Alternatively, select the merge node. In the top field, choose the rectangle node and press the minus ("-") button.

10. With the original connection removed, create a connection between the align node and the merge node.

11. Double-click datastamp. The rectangles should now be aligned correctly.



In conclusion, datastamp is powerful, but also pretty stupid. It just creates a new shape for every row in the data file, and sets its stamping variables accordingly. It is your job to use these stamping variables to influence your composition, by using them to influence the size of a shape or text of a textpath.


For more information, refer to the reference documentation on datastamp. It shows you all available stamp variables, as well as some example files.




