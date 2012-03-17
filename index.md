---
layout: homepage
---
<div class="versions row">
  <div class="five columns app">
    NodeBox 1
    <small>Pure Python. Mac OS X only.</small>
  </div>
  <div class="five columns featured app">
    NodeBox 3
    <small>Node-based GUI. Cross-platform.</small>
  </div>
  <div class="five columns app">
    NodeBox OpenGL
    <small>Pure Python. Cross-platform.</small>
  </div>
</div>

<div class="intro row">
  <div class="eight columns">
    <img src="/media/img/home/hero-shot-480.png" alt="NodeBox">
  </div>
  <div class="eight columns">
    <p><big>NodeBox is an open-source, node-based program for creating 2D graphics and animation.<br> <a href="/documentation/">Read more</a>.</big></p>
    <p><a href="/download/" class="hero-button">Download<small>Free and cross-platform</small></a></p>
  </div>
</div>

<div class="gallery row">
  <div class="eight columns">
    <h2>Gallery</h2>
    {% for post in site.categories.gallery %}
      <div class="gallery four columns">
        <a href="{{ post.url }}">
          <img src="/images/gallery/{{ post.thumb }}" alt="{{ post.title }}">
          <span>{{ post.title }}</span>
        </a>
      </div>
    {% endfor %}
  </div>
    
  <div class="eight columns">
    <h2>Signup for the newsletter</h2>
    <p>Stay up to date on NodeBox tips, new releases and exciting projects.</p>
    <form method="post" class="signup-form">
      <label>Email Address</label>
      <input type="email" name="email" />
      <input type="submit" value="Signup" />
      <small>We promise not to spam you.</small>
    </form>
  </div>
</div>

<div class="blog row">
  <div class="eight columns">
    <h2>Latest Blog Posts</h2>
    {% for post in site.categories.blog %}
      <div class="post">
        <a href="{{ post.url }}">{{ post.title }}</a>
        <span class="date">{{ post.date | date_to_string }}</span>
      </div>
    {% endfor %}
  </div>
</div>

