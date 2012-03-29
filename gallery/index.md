---
layout: default
section: gallery
title: Gallery
---
{% for post in site.categories.gallery %}
  {% include post.html %}
{% endfor %}
