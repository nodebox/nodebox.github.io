---
layout: documentation
title: Basic Animation
---
TODO
====
* another animation example will be added later.

Let's create a [moire effect](http://en.wikipedia.org/wiki/Moire_pattern) and automate it by using a first simple animation procedure.

Create an [ellipse node](/node/reference/corevector/ellipse.html).

* Set **Width** to **5.0**.
* Set **Height** to **5.0**.

Create a [grid node](/node/reference/corevector/grid.html)

* Set **Rows** to **30.0**.
* Set **Columns** to **30.0**.

Create a [translate node](/node/reference/corevector/translate.html)

* Connect ellipse1 to the **Shape** port.
* Connect grid1 to the **Translate** port.

Create a [colorize node](/node/reference/corevector/colorize.html)

* Change the fill parameter and select a color.
* Send translate1 to the colorize1 node.

Moiree effects appear when two or more identical grids are placed on top of each other and then rotated. In order to make this happen:

Create a [copy node](/node/reference/corevector/copy.html)

* Connect colorize1 to copy1.
* Set **Copies** to **2**
* Set **Rotate** to **45.0**

![Moiree effect step 1](animation-moiree-stepa.png)

In order to remove the parts without overlap:

* Create a [delete node](/node/reference/corevector/delete.html).
* Create an [ellipse node](/node/reference/corevector/ellipse.html) and set **Width** to **300.0** and **Height** to **300.0**
* Connect copy1 to **Shape** port.
* Connect ellipse2 to **Bounding**.
* Set **Scope** to **Paths**.
* Toggle off the **Delete Selected** parameter.

![Moiree effect step 2](animation-moiree-stepb.png)

Last step is the implementation of the animation itself. Look at the lower left corner where you can find the animation toolbar.

![Animation toolbar](animation-toolbar.png)

Create a [frame node](/node/reference/core/frame.html).

* Connect frame1 to the **Rotate** port of copy1.
* Press the play button in the animation toolbar and have a look at the result.

<object classid="clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B" width="452"
        height="388" codebase="http://www.apple.com/qtactivex/qtplugin.cab">
        <param name="src" value="moiree.mp4" />
        <param name="autoplay" value="true" />
        <param name="controller" value="true" />
        <param name="loop" value="true" />
        <embed src="moiree.mp4" width="452" height="388" autoplay="true" 
        controller="true" loop="true" pluginspage="http://www.apple.com/quicktime/download/">
        </embed>
</object>


