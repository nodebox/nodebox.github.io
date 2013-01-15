---
categories: blog
layout: blog
title: Building a kaleidoscope in NodeBox 3
---

A [kaleidoscopic image](http://en.wikipedia.org/wiki/Kaleidoscope) is generated through mirroring and rotating an image source in a typical manner. Unexpected and fascinating results can be achieved by tweaking a small number of parameters. Sounds like the perfect job for NodeBox!

- First we need an image source. Since we're limited to using vector shapes you can either create your own vectors (in NodeBox or elsewhere) one or find an svg file that you can use. The one I used in this tutorial is [cartoon apple with worm](http://openclipart.org/detail/20366/cartoon-apple-with-worm-by-rg1024-20366) from openclipart.org.
- Create a new folder and store your svg file there (if your're just using vectors from nodes you can omit this step).
- In NodeBox, create a new document and save it to the new folder.
- Add an [arc node](/node/reference/corevector/arc.html). Set **width** and **height** to **500** and degrees to **30**. We need an arc shape because we want to cut out an arc-shaped portion of our input shape. An arc is easy to mirror and copy to finally form our kaleidoscope.
- Add an [import_svg node](/node/reference/corevector/import_svg.html). In the **file** field, press the button and locate your svg file. Make sure the imported shape is **centered**.
- Add a [translate node](/node/reference/corevector/translate.html). 
- Connect the output of **import_svg1** to the **shape** port of **translate1**.
- Add an [ungroup node](/node/reference/corevector/ungroup.html). 
- Connect the output of **translate1** to the **shape** port of **ungroup1**. This will break up the original shape in different paths. For our purpose we need to cut out an arc from every single path individually or everything would become one giant blob in one color.

- Add a [compound node](/node/reference/corevector/compound.html). Change the **function** to **Intersection**.
- Connect the output of **ungroup1** to the **shape1** port of **compound1**.
- Connect the output of **arc1** to the **shape2** port of **compound1**.
![Step 1](/media/gallery/kaleidoscope/kaleidostep1.png)

The output of **compound1** still looks quite like the arc we started with. Compound operations typically discard all the color information of the original shapes. We have to reset the colors:
- Add a [lookup node](/node/reference/data/lookup.html) and inside the field for **key**, write down **fill**.
- Connect the output of **ungroup1** to the **list** port of **lookup1**.
- Add a [colorize node](/node/reference/corevector/colorize.html).
- Connect the output of **compound1** to the **shape** port of **colorize1**.
- Connect the output of **lookup1** to the **fill** port of **colorize1**. Note that we now have shapes in different colors but that are still within the bounds of our arc.
![Step 2](/media/gallery/kaleidoscope/kaleidostep2.png)
![Network at Step 2](/media/gallery/kaleidoscope/kaleidostep2network.png)

- Add a [group node](/node/reference/corevector/group.html).
- Connect the output of **colorize1** to the **shapes** port of **group1**.
- Add a [reflect node](/node/reference/corevector/reflect.html). Be careful to choose the one that reflects geometry.
- In **reflect1**, set the value for **angle** to **180** degrees. We now have a basic petal that encompasses 60 degrees.
![Step 3](/media/gallery/kaleidoscope/kaleidostep3.png)

- Add a [copy node](/node/reference/corevector/copy.html). Set **copies** to **6** and **rotate** to **60** degrees.
- Connect the output of **reflect1** to the **shape** port of **copy1**.
- Add another [group node](/node/reference/corevector/group.html).
- Connect the output of **copy1** to the **shapes** port of **group2**.
Congratulations, the individual petals now form a full kaleidoscopic pattern!

The options we have to vary our output are a bit limited though. We can take a different *slice* of our input shape by translating it around:

![Step 4](/media/gallery/kaleidoscope/kaleidostep4.png)
<small>To generate this form, I translated the shape 111 (x) and 126 (y).</small>
![Network at Step 4](/media/gallery/kaleidoscope/kaleidostep4network.png)

What if we want a portion of our input form but taken from a different angle? For this we would need to change the **start_angle** parameter of our arc1 node. However when we try to do this the symmetry starts breaking apart, and more specific so at the level of the **reflect1** node. We need to accomodate this by rotating the wanted slice but in the opposite direction:
- Between the **group1** and **reflect1** nodes, add a [rotate node](/node/reference/corevector/rotate.html).
- Connect the output of **group1** to the **shape** port of **rotate1**.
- Connect the output of **rotate1** to the **shape** port of **reflect1**.
- Add a [number node](/node/reference/math/number.html) and place it somewhere near **arc1**.
- Connect the output of **number1** to the **start_angle** port of **arc1**.
- Add a [negate node](/node/reference/math/negate.html).
- Connect the output of **number1** to the **value** port of **negate1**.
- Connect the output of **negate1** to the **angle** port of **rotate1**.
- Rename the **number1** node to **angle_offset**.

If we render our network now, note that there's now always a smooth transition when we change the value in **angle_offset**.
![Network at Step 5](/media/gallery/kaleidoscope/kaleidostep5network.png)

Another thing we'd like to control is the number of petals in our kaleidoscope. Currently it's fixed to 6 petals. A bit of mathematics can be of help:

- Add an [integer node](/node/reference/math/number.html) and place it near the **angle_offset** node.
- Rename **integer1** to **sides**. Set its **value** to **6**.
- Connect the output of **sides** to the **copies** port of the **copy1** node.
- Add a [divide node]. Set its **value1** to **360**.
- Connect the output of **sides** to the **value2** port of **divide1**.
- Connect the output of **divide1** to the **rotate** port of the **copy1** node.
At this point we're already able to control the number of petals but we also have to update the size of our slice accordingly.
- Add a second [divide node]. Set its **value2** to **2**.
- Connect the output of **divide1** to the **value1** port of **divide2**.
- Connect the output of **divide2** to the **degrees** port of **arc1**.
![Step 6](/media/gallery/kaleidoscope/kaleidostep6.png)
![Network at Step 6](/media/gallery/kaleidoscope/kaleidostep6network.png)
