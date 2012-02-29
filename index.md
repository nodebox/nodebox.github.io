---
layout: homepage
---
<div class="intro row">
  <div class="eight columns alpha">
    <img src="/media/img/home/hero-shot-480.png" alt="NodeBox">
  </div>
  <div class="eight columns omega">
    <p>NodeBox is a node-based program for creating 2D graphics and animation.</p>
  </div>
</div>

<div class="gallery row">
  <div class="eight columns alpha">
    <h2>Gallery</h2>
    {% for post in site.categories.gallery %}
      <div class="gallery four columns alpha">
        <a href="{{ post.url }}">
          <img src="/images/gallery/{{ post.thumb }}" alt="{{ post.title }}">
          <span>{{ post.title }}</span>
        </a>
      </div>
    {% endfor %}
  </div>
    
  <div class="eight columns omega">
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
  <div class="eight columns alpha">
    <h2>Latest Blog Posts</h2>
    {% for post in site.categories.blog %}
      <div class="post">
        <a href="{{ post.url }}">{{ post.title }}</a>
        <span class="date">{{ post.date | date_to_string }}</span>
      </div>
    {% endfor %}
  </div>
</div>

