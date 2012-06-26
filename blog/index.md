---
layout: default
section: blog
title: Blog
---

{% for post in site.categories.blog %}
  {% include post.html %}
{% endfor %}
