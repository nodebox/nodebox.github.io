---
layout: documentation
title: Node Reference
notes: AUTO-GENERATED - DO NOT EDIT. Use the extract_reference.py script to re-generate this file.
---
Color
-----
* [Color](color/color.html): Create a color value that can be used as a variable.
* [Gray Color](color/gray_color.html): Create a gray color.
* [Hsb Color](color/hsb_color.html): Create an HSB color.
* [Rgb Color](color/rgb_color.html): Create a RGB color.

Core
----
* [Frame](core/frame.html): Output the value of the current frame. Used for animating ports.
* [Network](core/network.html): Create an empty subnetwork.

Geometry
--------
* [Generator](corevector/generator.html): Template for creating nodes that generator vector data.
* [Filter](corevector/filter.html): Template for creating nodes that manipulate vector data.
* [Align](corevector/align.html): Align a shape in relation to the origin.
* [Arc](corevector/arc.html): Create an arc.
* [Centroid](corevector/centroid.html): Calculate the geometric center point of a shape.
* [Colorize](corevector/colorize.html): Change the color of a shape.
* [Compound](corevector/compound.html): Add, subtract or intersect geometry.
* [Connect](corevector/connect.html): Connect all points in a path.
* [Copy](corevector/copy.html): Create multiple copies of a shape.
* [Delete](corevector/delete.html): Delete points or paths that lie within the given bounding shape.
* [Distribute](corevector/distribute.html): Distribute shapes on a horizontal or vertical axis.
* [Draw Path](corevector/draw_path.html): Draw Bezier Paths.
* [Ellipse](corevector/ellipse.html): Create an ellipse or circle.
* [Fit](corevector/fit.html): Fit a shape within bounds.
* [Fit To](corevector/fit_to.html): Fit a shape to another shape.
* [Freehand](corevector/freehand.html): Draw directly on the canvas using the mouse.
* [Geonet](corevector/geonet.html): A network of geometry nodes.
* [Grid](corevector/grid.html): Create a grid of points.
* [Group](corevector/group.html): Combine multiple geometries together.
* [Import Svg](corevector/import_svg.html): Import geometry from a SVG file.
* [Line](corevector/line.html): Create a line between two points.
* [Line Angle](corevector/line_angle.html): Create a line between one point and an angle + distance.
* [Link](corevector/link.html): Generate a visual link between two shapes.
* [Make Point](corevector/make_point.html): Create a point from X/Y coordinates.
* [Null](corevector/null.html): Do nothing.
* [Point](corevector/point.html): Create a point value that can be used as a variable.
* [Point On Path](corevector/point_on_path.html): Calculate a point on a path.
* [Polygon](corevector/polygon.html): Create a multi-sided polygon.
* [Quad Curve](corevector/quad_curve.html): Create a quadratic curve with one off-curve point.
* [Rect](corevector/rect.html): Create a rectangle, square or rounded rectangle.
* [Reflect](corevector/reflect.html): Mirror the geometry around an invisible axis.
* [Resample](corevector/resample.html): Distribute points along a shape.
* [Resample By Amount](corevector/resample_by_amount.html): Distribute a number of points along a shape.
* [Resample By Length](corevector/resample_by_length.html): Distribute points evenly along a shape.
* [Rotate](corevector/rotate.html): Rotate the shape according to the given angle.
* [Scale](corevector/scale.html): Resize the shape by scaling it.
* [Scatter](corevector/scatter.html): Generate points within the boundaries of a shape.
* [Shape On Path](corevector/shape_on_path.html): Copies shapes on a path.
* [Skew](corevector/skew.html): Skew the shape.
* [Snap](corevector/snap.html): Snap geometry to a grid.
* [Sort](corevector/sort.html): Sort points or shapes using different sorting methods.
* [Star](corevector/star.html): Create a star shape.
* [Text On Path](corevector/text_on_path.html): Create a text path that follows a shape.
* [Textpath](corevector/textpath.html): Create a path out of text.
* [To Points](corevector/to_points.html): Extract the points from a given shape.
* [Translate](corevector/translate.html): Move the shape, changing its position.
* [Ungroup](corevector/ungroup.html): Decompose the input geometry into its paths.
* [Wiggle](corevector/wiggle.html): Shift points by a random amount.
* [Wiggle Points](corevector/wiggle_points.html): Shift points by a random amount.
* [Wiggle Contours](corevector/wiggle_contours.html): Shift paths by a random amount.
* [Wiggle Paths](corevector/wiggle_paths.html): Shift paths by a random amount.

Data
----
* [Import Csv](data/import_csv.html): Import a comma-separated value file containing tabular data.
* [Lookup](data/lookup.html): Look up a value.

List
----
* [Combine](list/combine.html): Combine multiple lists into one.
* [Count](list/count.html): Count the number of items in the list.
* [Cull](list/cull.html): Cull the list.
* [Distinct](list/distinct.html): Remove all duplicate items from the list.
* [Filter](list/filter.html): Filter the list.
* [First](list/first.html): Take the first item of the list.
* [Last](list/last.html): Take the last item of the list.
* [Pick](list/pick.html): Pick items from the list in random order.
* [Repeat](list/repeat.html): Repeat the list a number of times.
* [Rest](list/rest.html): Take all but the first item of the list.
* [Reverse](list/reverse.html): Reverse the list.
* [Second](list/second.html): Take the second item of the list.
* [Shift](list/shift.html): Move items at the beginning of the list to the end.
* [Shuffle](list/shuffle.html): Randomize the ordering of items in the list.
* [Slice](list/slice.html): Take a portion of the list.
* [Sort](list/sort.html): Sort items in the list.
* [Switch](list/switch.html): Switch between multiple inputs.
* [Take Every](list/take_every.html): Take every nth element of the list.

Math
----
* [Abs](math/abs.html): Convert every number to a positive number.
* [Add](math/add.html): Add two numbers.
* [Angle](math/angle.html): Calculate the angle between two points.
* [Average](math/average.html): Calculate the average of a list of numbers.
* [Boolean](math/boolean.html): Create a boolean value that can be used as a variable.
* [Ceil](math/ceil.html): Round up the value of a number.
* [Compare](math/compare.html): Select between two values by comparing them.
* [Convert Range](math/convert_range.html): Convert a value from one range to another.
* [Coordinates](math/coordinates.html): Calculate a new point based on the angle and distance from an original point.
* [Cos](math/cos.html): Calculate the trigonometric cosine of an angle.
* [Degrees](math/degrees.html): Convert radians to degrees.
* [Distance](math/distance.html): Calculate the distance between two points.
* [Divide](math/divide.html): Divide two numbers.
* [E](math/e.html): The value of the mathematical constant e, the base of the natural logarithm.
* [Floor](math/floor.html): Round down the value of a number.
* [Integer](math/integer.html): Create an integer value that can be used as a variable.
* [Log](math/log.html): Calculate the natural logarithm of a value.
* [Make Numbers](math/make_numbers.html): Transform a string to a list of numbers.
* [Max](math/max.html): Select the largest value from a list of numbers.
* [Min](math/min.html): Select the smallest value from a list of numbers.
* [Mod](math/mod.html): Calculate the modulo by dividing two numbers and keeping the remainder.
* [Multiply](math/multiply.html): Multiply two numbers.
* [Negate](math/negate.html): Change the sign of a number by negating it.
* [Number](math/number.html): Create a floating-point value that can be used as a variable.
* [Pi](math/pi.html): The value of the mathematical constant pi.
* [Pow](math/pow.html): Calculate the power of a number.
* [Radians](math/radians.html): Convert degrees to radians.
* [Random Numbers](math/random_numbers.html): Create a list of random numbers.
* [Range](math/range.html): Generate a range of numbers.
* [Reflect](math/reflect.html): Calculate a new point based on the angle and distance from an original point.
* [Sample](math/sample.html): Generate numbers within the given bounds.
* [Sin](math/sin.html): Calculate the trigonometric sine of an angle.
* [Sqrt](math/sqrt.html): Calculate the square root of a number.
* [Subtract](math/subtract.html): Subtract two numbers.
* [Sum](math/sum.html): Sum a list of numbers.
* [To Integer](math/to_integer.html): Convert a floating-point number to an integer.
* [Wave](math/wave.html): Calculate a value based on wave equations.

String
------
* [String](string/string.html): Create a string value that can be used as a variable.
* [Concatenate](string/concatenate.html): Add strings together.
* [Length](string/length.html): Count the number of characters in a string.
* [Make Strings](string/make_strings.html): Create a list of strings.
* [Word Count](string/word_count.html): Count the number of words in a string.

