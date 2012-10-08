---
layout: reference
title: Edit Node
image: edit
---
Edit points non-destructively.

Edit allows manual tweaks to computer-generated geometry. It is very useful when NodeBox generates something that is not *quite* what you want.

The edit node stores point indices and delta values. That means it records that point 42 was moved 30 pixels left and 40 pixels up. This means that if you make changes to the input geometry, NodeBox will re-apply these changes.

* **Point Deltas**: A list of delta values. It's best to use the edit handle to change these.