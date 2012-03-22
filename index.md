---
layout: homepage
---
<div class="versions">
  <div class="grid_4 app">
    <h2>NodeBox 1</h2>
    <small>Pure Python. Mac OS X only.</small>
    <ul>
      <li>Light-weight</li>
      <li>Python</li>
      <li>Mac OS X only</li>
    </ul>
  </div>
  <div class="grid_4 featured app">
    <h2>NodeBox 3</h2>
    <small>Node-based GUI. Cross-platform.</small>
    <ul>
      <li>Easy-to-use node-based GUI</li>
      <li>For Windows, Mac OS X and Linux</li>
      <li>Under active development</li>
    </ul>
  </div>
  <div class="grid_4 app">
    <h2>NodeBox OpenGL</h2>
    <small>Pure Python. Cross-platform.</small>
    <ul>
      <li>Hardware-accelerated</li>
      <li>Ideal for games</li>
      <li>No GUI, just the code</li>
    </ul>
  </div>
</div>

<div class="grid_6 projects">
  <h2>Projects</h2>
  {% for post in site.categories.projects %}
    <div class="grid_3">
      <a href="{{ post.url }}">
          <img src="/media/projects/{{ post.thumb }}" alt="{{ post.title }}">
          <span>{{ post.title }}</span>
      </a>
    </div>
  {% endfor %}
</div>

<div class="grid_6 workshops">
  <h2>Workshops</h2>
  {% for post in site.categories.workshops %}
    <div class="grid_3">
      <a href="{{ post.url }}">
          <img src="/media/workshops/{{ post.thumb }}" alt="{{ post.title }}">
          <span>{{ post.title }}</span>
      </a>
    </div>
  {% endfor %}
</div>


<div class="grid_6 emrg">
  <h2>EMRG</h2>
</div>

<div class="grid_6 emrg">
  <h2>Stay in touch</h2>
  <div class="grid_3 alpha">
    <h3>Newsletter</h3>
    <p>Sign up for the monthly newsletter.</p>
    <form method="post">
      <input type="email" placeholder="Email address" /><br>
      <input type="submit" value="Signup" />
    </form>
  </div>
  <div class="grid_3 omega">
    <h3>Community</h3>
    
  </div>
</div>
  

