---
layout: documentation
title: Basic Animation
---

Let's create a [shape moire effect](http://en.wikipedia.org/wiki/Shape_moir%C3%A9) and automate it by using a first animation procedure.

![Basic Animation](/media/img/tutorial/basic-animation.png)

The idea is to make a text path, scale it on the vertical axis and copy it below each other.

Create a [Textpath](../nodes/txtpath.html) node.

* Set **Text** to **ABCD**.
* Select a bold **font**.
* Set **Size** parameter to **120.00**

Create a [Transform](../nodes/transform.html) node and **connect textpath1 to it**. Set **Scale Y** to **6.00** so you end up with an ugly stretched version of textpath1.

Create a [Copy](../nodes/copy.html) node. **Connect transform1 to this node**.

* Set **Copies** to **10**.
* Set **Translate Y** to **12.00**.

You should see this as a result:

![Basic Animation Step1](/media/img/tutorial/basic-animation-step1.png)

Now we will create a pattern to use as a movable overlay over the above result.

Create a [Rect](../nodes/rect.html) node as a basic shape for the pattern.

* Set **Width** to **400.00**.
* Set **Height** to **12.00** (which is the same amount as the value for  translate Y parameter of copy1)

Create a [Copy](../nodes/copy.html) node and make **30** copies with a **Translate Y** parameter set to **13.00**.
**Connect rect1 to this node**.

In order to make it moveable create a [Transform](../nodes/transform.html) node and **connect copy2 to it**. We will change the value for **Translate Y** later.

Create a [Merge](../nodes/merge.html) node and connect copy1 to it. Do the same for transform2. Double click on merge1 to make it the rendered node.

Click once on transform2 and drag the **Translate Y** parameter. Cool..but can't we automate it?

Animation asks for a few new things to be explained.

**Parameters** as we have seen before are editable by using their **widgets**. You can also **make a dynamic variable** by using **expressions**. One of the variables we can call for over an expression is **FRAME** (in capitals - system variables are all in CAPITALS), meaning it calls the number of the frame. Further is more information on expressions but let's implement one now:

* **Click on the transform2** node and look at the **parameter pane**. On the **right of each parameter** is a **small arrow** that is in fact a button. 
* **Click on it** and select **Toggle Expression**. The look of the widget will change from the numberwidget to a textinput window. 
* Enter **-FRAME** en press the enter key. We call for the negative of the frame because i want the group of rectangles to go up.
* On the lower left corner is the "Animation bar". Click the **Play** button to see the animation.

You can **save animation** by going to  the **File tab >> export Movie** where you have a selection of possible formats. Enter a name for the animation and select the number of frames it has to export.

<object classid="clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B" width="400"
        height="400" codebase="http://www.apple.com/qtactivex/qtplugin.cab">
        <param name="src" value="/media/img/tutorial/basic_animation.mp4" />
        <param name="autoplay" value="true" />
        <param name="controller" value="true" />
        <param name="loop" value="true" />
        <embed src="/media/img/tutorial/basic-animation.mp4" width="400" height="400" autoplay="true" 
        controller="true" loop="true" pluginspage="http://www.apple.com/quicktime/download/">
        </embed>
</object>

**Try out:**

* Changing the order so the letters are printed upside down.
* Change the letters in to an svg using an [Import](../nodes/import.html) node. The Eifeltower for instance (from [Wikipedia](http://fr.wikipedia.org/wiki/Fichier:Eiffelturm-outline.svg))
* Change **Text** into an expression over **Toggle Expression** and enter **int(FRAME/10.0)** to see a counting procedure.

![Basic Animation Eifel](/media/img/tutorial/basic-animation-eifel.png)
