---
layout: homepage
title: Meet NodeBox.
---
<a class="heroshot" href="#"><img src="media/img/home-nodebox.png" alt="NodeBox Screenshot"></a>

NodeBox is a new software application for creating generative art using procedural graphics. It's a new way to approach graphic design.

<script>
$("a.heroshot").click(function() {
  var screenshots = [
    {href: 'media/img/home-shot1.png',
     title: 'NodeBox is ideal for data visualization.'
    },
    {href: 'media/img/home-shot2.jpg',
     title: 'Animation support is built-in.'
    }];
  $.fancybox(screenshots,
    {
      changeFade: 0
    });
});
</script>

