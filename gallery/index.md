---
layout: default
section: gallery
title: Gallery
---
{% for post in site.categories.gallery %}
<li class="thumb four columns">
  <a href="{{ post.url }}"><img src="/images/gallery/{{ post.thumb }}" alt="{{ post.title }}">
  {{ post.title }}
  </a>
</li>
{% endfor %}
