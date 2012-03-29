---
layout: reference
title: Import Node
image: import
---
Import SVG files as geometric data.

When using Illustrator, select File > Save As... and choose the SVG (svg) format. Choose SVG Tiny 1.2:

![Illustrator Import Options](/media/img/nodes/import-illustrator.png)

SVG Files store their coordinates from the **top left** of the document. You can toggle the "Center of Canvas" to center the imported shape.

* **File**: The SVG file.
* **Center on Canvas**: If checked, centers the geometry on the canvas.
* **X**: The X offset from the origin.
* **Y**: The Y offset from the origin.

Note
----
* **Make sure to save your NodeBox file first** before using the import node. When your NodeBox file is saved, the import node can use a path relative to the NodeBox file. If the NodeBox file is *not* saved yet the import node will store an absolute path, which means your files will not work on other computers.