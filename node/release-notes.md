---
layout: default
title: NodeBox 3 Release Notes
section: node
---
Version 3.0.38 (24 Jan 2014)
----------------------------
* Add round_segments node.
* Access to external audio through the mic line-in.
* Improved SVG handling.
* Some cosmetic user interface changes.

Version 3.0.37 (1 Nov 2013)
---------------------------
* Unified export: all export features now support the canvasWidth/Height/X/Y values in document settings.
* The viewer can show export bounds.

Version 3.0.36 (3 Sep 2013)
----------------------------
* Support for high-resolution screens.
* Nodes can have comments.
* Better icons.
* General bug-fixes.

Version 3.0.35 (29 Apr 2013)
----------------------------
* Add built-in examples.

Version 3.0.34 (14 Mar 2013)
----------------------------
* Add the [stack node](/node/reference/corevector/stack.html).
* Add the [filter data node](/node/reference/data/filter_data.html).

Version 3.0.33 (24 Feb 2013)
----------------------------
* Add full-screen support.
* Nice GUI for device support.
* Audio analysis is built in.
* More icons.
* Lookup node can do nested lookups using the period (e.g. "bounds.x")
* Distinct node can optionally use a lookup key.
* Various code cleanups.

Version 3.0.32 (4 Feb 2013)
---------------------------
* Fix errors in network view.
* Fix errors in HTTP get node.
* The export viewer can capture mouse events.
* Data sheet is faster.

Version 3.0.31 (3 Feb 2013)
---------------------------
* Experimental support for external devices (over OSC).
* Experimental support for network requests + JSON parsing.
* More robust multi-threaded render.
* Fix bug with spaces in paths.

Version 3.0.30 (29 Jan 2013)
----------------------------
* Subnetworks always render the root node, making working with subnetworks more logical.
* Performance improvements in node processing + rendering.
* New list icons.
* New viewer implementation, removing dependency on the (obsolete) Piccolo library.
* Optimize point memory usage.
* Nodes for string manipulation (thanks to [Dave Addison](https://github.com/djaddison)).
* Clean up confusion between nodes and networks.

Version 3.0.29 (17 Dec 2012)
----------------------------
* We've dropped the "a" in the version number: we think NodeBox 3 is stable enough to drop the "alpha" tag.
* Network view: alt-dragging a node now copies and moves it.
* Zooming: Use Cmd+plus and Cmd+minus to zoom in/out.
* Cmd+P and Cmd+Shift+P play/pause and rewind the animation.
* You can pick the image format when exporting.
* Added a [running total](/node/reference/math/running_total.html) node.
* The [snap node](/node/reference/corevector/snap.html) now returns correct results for curved paths.
* The [line node](/node/reference/corevector/line.html) allows you to specify the amount of points.
* You can choose whether to set the fill / stroke properties in the colorize node.
* Transparent colors are easier to set.
* Right-click a node and choose "Help" to go to the documentation page for that node.
* More robust CSV parsing.

Version 3.0a28 (15 Nov 2012)
----------------------------
* Fix movie export.
* Made executing the network faster by caching function retrieval.
* Expose the root node which makes creating custom nodes easier.

Version 3.0a27 (7 Nov 2012)
---------------------------
* Fix viewer bug where zooming in would make the content dissappear.

Version 3.0a26 (6 Nov 2012)
---------------------------
* Copy node returns a list of geometries.
* Readme points to nodebox.net (instead of beta.nodebox.net).

Version 3.0a25 (4 Nov 2012)
---------------------------
* Big "clean-up" release: we've consolidated nodes, fixed port names and added better reference documentation.
* Remove various libraries that will be bundled separately (L-systems, packing)
* The [repeat node](/node/reference/list/repeat.html) allows per-item repetition.
* File upgrades require less code, making migrations easier.
* Add the [zip_map node](/node/reference/list/zip_map.html).
* Various improvements to the color picker.

Version 3.0a24 (8 Oct 2012)
---------------------------
* Better node descriptions makes finding a node easier.
* Fix bugs with subnetwork creation.
* The [csv node](/node/reference/data/import_csv.html) can accept various CSV "dialects".
* The [delete node](/node/refernce/corevector/delete.html) can now handle Geometry and Path objects, as well as a single list of Point values.
* Nodes that take in geometry can also take in a list of points.
* Double clicking ndbx files will open them on Windows.
* Add the [skew node](/node/reference/corevector/skew.html).

Version 3.0a23 (27 Sep 2012)
----------------------------
* Better support for nested lists.
* Add categories to the node selection dialog.
* Random now looks ["more random"](http://blog.42.nl/articles/when-random-isnt-as-random-as-expected). 
* Add document properties dialog, useful for setting canvas width / height.
* Rename `delete_bounding` to [delete node](/node/reference/corevector/delete.html).
* Renaming a node now updates the references of published ports on the parent network.
* String ports can accept any kind of input.
* Add a [pi node](/node/reference/math/pi.html) and [e node](/node/reference/math/e.html).
* Re-enable handles.
* Hide ports that accept lists in parameter pane.
* Create "value" nodes for [string](/node/reference/string/string.html), [color](/node/reference/color/color.html), [number](/node/reference/math/number.html), [integer](/node/reference/math/integer.html), [boolean](/node/reference/math/boolean.html), [point](/node/reference/corevector/point.html).
* Selected nodes can be grouped into a network automatically.
* Add [floor](/node/reference/math/floor.html), [ceil](/node/reference/math/ceil.html), [wave](/node/reference/math/wave.html) and [pow](/node/reference/math/pow.html) nodes.
