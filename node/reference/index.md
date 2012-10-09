---
layout: documentation
title: Node Reference
notes: AUTO-GENERATED - DO NOT EDIT. Use the autoref.py script to re-generate this file.
---
Color
-----
* [Color](/node/reference/color/color.html): Create a color value that can be used as a variable.
* [Gray Color](/node/reference/color/gray_color.html): Create a gray color.
* [Hsb Color](/node/reference/color/hsb_color.html): Create a HSB color.
* [Rgb Color](/node/reference/color/rgb_color.html): Create a RGB color.

Core
----
* [Frame](/node/reference/core/frame.html): Output the value of the current frame. Used for animating ports.
* [Network](/node/reference/core/network.html): Create an empty subnetwork.

Geometry
--------
* [Generator](/node/reference/corevector/generator.html): Template for creating nodes that generator vector data.
* [Filter](/node/reference/corevector/filter.html): Template for creating nodes that manipulate vector data.
* [Align](/node/reference/corevector/align.html): Align a shape in relation to the origin.
* [Arc](/node/reference/corevector/arc.html): Create an arc.
* [Centroid](/node/reference/corevector/centroid.html): Calculate the geometric center point of a shape.
* [Colorize](/node/reference/corevector/colorize.html): Change the color of a shape.
* [Compound](/node/reference/corevector/compound.html): Add, subtract or intersect geometry.
* [Connect](/node/reference/corevector/connect.html): Connect all points in a path.
* [Copy](/node/reference/corevector/copy.html): Create multiple copies of a shape.
* [Delete](/node/reference/corevector/delete.html): Delete points or paths that lie within the given bounding shape.
* [Distribute](/node/reference/corevector/distribute.html): Distribute shapes on a horizontal or vertical axis.
* [Draw Path](/node/reference/corevector/draw_path.html): Draw Bezier Paths.
* [Ellipse](/node/reference/corevector/ellipse.html): Create an ellipse or circle.
* [Fit](/node/reference/corevector/fit.html): Fit a shape within bounds.
* [Fit To](/node/reference/corevector/fit_to.html): Fit a shape to another shape.
* [Freehand](/node/reference/corevector/freehand.html): Draw directly on the canvas using the mouse.
* [Geonet](/node/reference/corevector/geonet.html): A network of geometry nodes.
* [Grid](/node/reference/corevector/grid.html): Create a grid of points.
* [Group](/node/reference/corevector/group.html): Combine multiple geometries together.
* [Import Svg](/node/reference/corevector/import_svg.html): Import geometry from a SVG file.
* [Line](/node/reference/corevector/line.html): Create a line between two points.
* [Line Angle](/node/reference/corevector/line_angle.html): Create a line between one point and an angle + distance.
* [Link](/node/reference/corevector/link.html): Generate a visual link between two shapes.
* [Make Point](/node/reference/corevector/make_point.html): Create a point from X/Y coordinates.
* [Null](/node/reference/corevector/null.html): Do nothing.
* [Point](/node/reference/corevector/point.html): Create a point value that can be used as a variable.
* [Point On Path](/node/reference/corevector/point_on_path.html): Calculate a point on a path.
* [Polygon](/node/reference/corevector/polygon.html): Create a multi-sided polygon.
* [Quad Curve](/node/reference/corevector/quad_curve.html): Create a quadratic curve with one off-curve point.
* [Rect](/node/reference/corevector/rect.html): Create a rectangle, square or rounded rectangle.
* [Reflect](/node/reference/corevector/reflect.html): Mirror the geometry around an invisible axis.
* [Resample](/node/reference/corevector/resample.html): Distribute points along a shape.
* [Resample By Amount](/node/reference/corevector/resample_by_amount.html): Distribute a number of points along a shape.
* [Resample By Length](/node/reference/corevector/resample_by_length.html): Distribute points evenly along a shape.
* [Rotate](/node/reference/corevector/rotate.html): Rotate the shape according to the given angle.
* [Scale](/node/reference/corevector/scale.html): Resize the shape by scaling it.
* [Scatter](/node/reference/corevector/scatter.html): Generate points within the boundaries of a shape.
* [Shape On Path](/node/reference/corevector/shape_on_path.html): Copies shapes on a path.
* [Skew](/node/reference/corevector/skew.html): Skew the shape.
* [Snap](/node/reference/corevector/snap.html): Snap geometry to a grid.
* [Sort](/node/reference/corevector/sort.html): Sort points or shapes using different sorting methods.
* [Star](/node/reference/corevector/star.html): Create a star shape.
* [Text On Path](/node/reference/corevector/text_on_path.html): Create a text path that follows a shape.
* [Textpath](/node/reference/corevector/textpath.html): Create a path out of text.
* [To Points](/node/reference/corevector/to_points.html): Extract the points from a given shape.
* [Translate](/node/reference/corevector/translate.html): Move the shape, changing its position.
* [Ungroup](/node/reference/corevector/ungroup.html): Decompose the input geometry into its paths.
* [Wiggle](/node/reference/corevector/wiggle.html): Shift points by a random amount.
* [Wiggle Points](/node/reference/corevector/wiggle_points.html): Shift points by a random amount.
* [Wiggle Contours](/node/reference/corevector/wiggle_contours.html): Shift paths by a random amount.
* [Wiggle Paths](/node/reference/corevector/wiggle_paths.html): Shift paths by a random amount.

Data
----
* [Import Csv](/node/reference/data/import_csv.html): Import a comma-separated value file containing tabular data.
* [Lookup](/node/reference/data/lookup.html): Look up a value in a table or object.

List
----
* [Combine](/node/reference/list/combine.html): Combine multiple lists into one.
* [Count](/node/reference/list/count.html): Count the number of items in the list.
* [Cull](/node/reference/list/cull.html): Cull the list.
* [Distinct](/node/reference/list/distinct.html): Remove all duplicate items from the list.
* [Filter](/node/reference/list/filter.html): Filter the list.
* [First](/node/reference/list/first.html): Take the first item of the list.
* [Last](/node/reference/list/last.html): Take the last item of the list.
* [Pick](/node/reference/list/pick.html): Pick items from the list in random order.
* [Repeat](/node/reference/list/repeat.html): Repeat the list a number of times.
* [Rest](/node/reference/list/rest.html): Take all but the first item of the list.
* [Reverse](/node/reference/list/reverse.html): Reverse the list.
* [Second](/node/reference/list/second.html): Take the second item of the list.
* [Shift](/node/reference/list/shift.html): Move items at the beginning of the list to the end.
* [Shuffle](/node/reference/list/shuffle.html): Randomize the ordering of items in the list.
* [Slice](/node/reference/list/slice.html): Take a portion of the list.
* [Sort](/node/reference/list/sort.html): Sort items in the list.
* [Switch](/node/reference/list/switch.html): Switch between multiple inputs.
* [Take Every](/node/reference/list/take_every.html): Take every nth element of the list.

Math
----
* [Abs](/node/reference/math/abs.html): Convert every number to a positive number.
* [Add](/node/reference/math/add.html): Add two numbers.
* [Angle](/node/reference/math/angle.html): Calculate the angle between two points.
* [Average](/node/reference/math/average.html): Calculate the average of a list of numbers.
* [Boolean](/node/reference/math/boolean.html): Create a boolean value that can be used as a variable.
* [Ceil](/node/reference/math/ceil.html): Round up the value of a number.
* [Compare](/node/reference/math/compare.html): Select between two values by comparing them.
* [Convert Range](/node/reference/math/convert_range.html): Convert a value from one range to another.
* [Coordinates](/node/reference/math/coordinates.html): Calculate a new point based on the angle and distance from an original point.
* [Cos](/node/reference/math/cos.html): Calculate the trigonometric cosine of an angle.
* [Degrees](/node/reference/math/degrees.html): Convert radians to degrees.
* [Distance](/node/reference/math/distance.html): Calculate the distance between two points.
* [Divide](/node/reference/math/divide.html): Divide two numbers.
* [E](/node/reference/math/e.html): The value of the mathematical constant e, the base of the natural logarithm.
* [Floor](/node/reference/math/floor.html): Round down the value of a number.
* [Integer](/node/reference/math/integer.html): Create an integer value that can be used as a variable.
* [Log](/node/reference/math/log.html): Calculate the natural logarithm of a value.
* [Make Numbers](/node/reference/math/make_numbers.html): Transform a string to a list of numbers.
* [Max](/node/reference/math/max.html): Select the largest value from a list of numbers.
* [Min](/node/reference/math/min.html): Select the smallest value from a list of numbers.
* [Mod](/node/reference/math/mod.html): Calculate the modulo by dividing two numbers and keeping the remainder.
* [Multiply](/node/reference/math/multiply.html): Multiply two numbers.
* [Negate](/node/reference/math/negate.html): Change the sign of a number by negating it.
* [Number](/node/reference/math/number.html): Create a floating-point value that can be used as a variable.
* [Pi](/node/reference/math/pi.html): The value of the mathematical constant pi.
* [Pow](/node/reference/math/pow.html): Calculate the power of a number.
* [Radians](/node/reference/math/radians.html): Convert degrees to radians.
* [Random Numbers](/node/reference/math/random_numbers.html): Create a list of random numbers.
* [Range](/node/reference/math/range.html): Generate a range of numbers.
* [Reflect](/node/reference/math/reflect.html): Calculate a new point based on the angle and distance from an original point.
* [Sample](/node/reference/math/sample.html): Generate numbers within the given bounds.
* [Sin](/node/reference/math/sin.html): Calculate the trigonometric sine of an angle.
* [Sqrt](/node/reference/math/sqrt.html): Calculate the square root of a number.
* [Subtract](/node/reference/math/subtract.html): Subtract two numbers.
* [Sum](/node/reference/math/sum.html): Add up all numbers in the list.
* [To Integer](/node/reference/math/to_integer.html): Convert a floating-point number to an integer.
* [Wave](/node/reference/math/wave.html): Calculate a value based on wave equations.

String
------
* [String](/node/reference/string/string.html): Create a string value that can be used as a variable.
* [Concatenate](/node/reference/string/concatenate.html): Add strings together.
* [Length](/node/reference/string/length.html): Count the number of characters in a string.
* [Make Strings](/node/reference/string/make_strings.html): Create a list of strings.
* [Word Count](/node/reference/string/word_count.html): Count the number of words in a string.

