---
layout: reference
library: data
node: lookup
title: Lookup
image: lookup.png
---
Look up a value in a table or object.

* **List**: The input value.
* **Key**: The key to lookup.


## Notes
* This node is often used after a [import CSV](/node/reference/data/import_csv.html) node to retrieve the values of specific columns.
* An advanced feature is to use it to retrieve the properties of graphics objects, like the width of a piece of text. For that, type `bounds.width` in the key field. Use the [keys](/node/reference/list/keys.html) node to discover all possible properties of objects.