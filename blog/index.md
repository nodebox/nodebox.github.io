---
layout: default
section: blog
title: Blog
---

{% for post in site.categories.blog %}
<li class="post">
  <a href="{{ post.url }}">{{ post.title }}</a>
  <span class="date">{{ post.date | date_to_string }}</span>
</li>
{% endfor %}
