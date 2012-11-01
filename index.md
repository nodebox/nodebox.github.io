---
layout: base
title: NodeBox
section: home
---
<div class="hero row">
  <div class="sixteen columns">
    <div class="hero-text">
      <h1>Tools to help designers.</h1>
      <p>The NodeBox family of tools gives you the leverage to create generative design the way you want.</p>
    </div>
  </div>
</div>

<div class="versions row">
  <div class="eight columns featured app">
    <a href="/node/">
      <img src="/media/homepage/nodebox-3.jpg" alt="NodeBox 3 screenshot">
      <h2>NodeBox 3</h2>
      <small>Acquire, Transform, Visualize</small>
      <p>Cross-platform, node-based GUI for efficient data visualizations and generative design.</p>
    </a>
  </div>
  <div class="four columns app">
    <a href="/code/">
      <img src="/media/homepage/nodebox-1.jpg" alt="NodeBox 1 screenshot">
      <h2>NodeBox 1</h2>
      <small>Code, Iterate, Print</small>
      <p>Create 2D visuals (static, animated or interactive) using Python programming code.</p>
    </a>
  </div>
  <div class="four columns app">
    <a href="/opengl/">
      <img src="/media/homepage/nodebox-opengl.jpg" alt="NodeBox OpenGL screenshot">
      <h2>NodeBox OpenGL</h2>
      <small>Code, Animate</small>      
      <p>Fast cross platform graphics library.</p>
    </a>
  </div>
</div>

<div class="gallery row">
  <div class="eight columns">
  <h2>Gallery</h2>
  {% for post in site.categories.gallery limit: 2 %}
    {% include post.html %}
  {% endfor %}
  </div>
  <div class="eight columns">
  <h2>Blog</h2>
  {% for post in site.categories.blog limit: 2 %}
    {% include post.html %}
  {% endfor %}
  </div>
</div>
  
<div class="connect row">
  <div class="eight columns">
    <h2>Newsletter</h2>
    <p>Sign up for the monthly newsletter.</p>
    <form method="post" class="signup">
      <input type="email" placeholder="Email address" />
      <input class="button" type="submit" value="Signup" />
    </form>
  </div>
  <div class="eight columns">
    <h2>Workshops</h2>
    <p>The creators of NodeBox have organized workshops internationally since 2004. These one-week sessions focus on learning the software combined with insights into the principles of generative art, data visualization and cognitive science.</p>
    <a class="button" href="http://www.emrg.be/teaching/">Read more</a>
  </div>
</div>

<div class="emrg row">
  <h2 class="fourteen columns offset-by-two">EMRG</h2>
  <div class="two columns">
    <a href="http://www.emrg.be/"><img src="/media/homepage/emrg-logo.png" alt="Logo of EMRG"></a>
  </div>
  <div class="six columns">
    <p>NodeBox is developed by the <strong>Experimental Media Research Group</strong>, a cross-domain research group associated with the <a href="http://www.sintlucasantwerpen.be/">Sint Lucas School of arts</a> of the <a href="http://www.kdg.be/">Karel de Grote-Hogeschool</a> (Antwerp, Belgium). </p>
    <p><strong>EMRG</strong> has been active since 2004 developing NodeBox and doing cutting-edge research in the domain of computer graphics, user experience, creativity, but also in artificial intelligence and natural language processing.</p>
    <p><a href="http://www.emrg.be/">www.emrg.be</a></p>
  </div>
</div>

