---
layout: homepage
title: NodeBox
---
<div class="versions row">
  <h2 class="sixteen columns">Generative Software for Creatives</h2>  
  <div class="eight columns featured app">
    <img src="/media/homepage/nodebox-3.jpg" alt="NodeBox 3 Screenshot">
    <h2>NodeBox 3</h2>
    <small>Node-based GUI. Cross-platform.</small>
    <ul>
      <li>Easy-to-use node-based GUI</li>
      <li>For Windows, Mac OS X and Linux</li>
      <li>Under active development</li>
    </ul>
    <div class="more"><a href="/node/">Read More</a></div>
  </div>
  <div class="four columns app">
    <img src="/media/homepage/nodebox-1.jpg" alt="Nodes">
    <h2>NodeBox 1</h2>
    <small>Pure Python. Mac OS X only.</small>
    <ul>
      <li>Light-weight</li>
      <li>Python</li>
      <li>Mac OS X only</li>
    </ul>
    <div class="more"><a href="/code/">Read More</a></div>
  </div>
 <div class="four columns app">
    <img src="/media/homepage/nodebox-opengl.jpg" alt="Nodes">
    <h2>NodeBox OpenGL</h2>
    <small>Pure Python. Cross-platform.</small>
    <ul>
      <li>Hardware-accelerated</li>
      <li>Ideal for games</li>
      <li>No GUI, just the code</li>
    </ul>
    <div class="more"><a href="/opengl/">Read More</a></div>
  </div>
</div> <!-- .versions -->


<div class="screenshots row">
  <h2 class="sixteen columns">Screenshots</h2>
  <div class="four columns">
    <a class="thumb" href="/media/homepage/nodes.png"><img src="/media/homepage/nodes_sq.png" alt="Nodes"></a>
  </div>
  <div class="four columns">
    <a class="thumb" href="/media/homepage/code.png"><img src="/media/homepage/code_sq.png" alt="Nodes"></a>
  </div>
  <div class="four columns">
    <a class="thumb" href="/media/homepage/animation.png"><img src="/media/homepage/animation_sq.png" alt="Nodes"></a>    
  </div>
  <div class="four columns">
    <a class="thumb" href="/media/homepage/dataviz.png"><img src="/media/homepage/dataviz_sq.png" alt="Data Visualization"></a>
  </div>
</div> <!-- .screenshots -->

<div class="gallery row">
  <div class="four columns gal">
  <h2>Gallery</h2>
  {% for post in site.categories.gallery limit: 2 %}
    {% include post.html %}
  {% endfor %}
  </div>
  <div class="four columns blog">
  <h2>Blog</h2>
  {% for post in site.categories.blog limit: 2 %}
    {% include post.html %}
  {% endfor %}
  </div>
  
  <div class="eight columns community">
    <h2>Stay in touch</h2>
    <div class="four columns omega">
      <h3>Newsletter</h3>
      <p>Sign up for the monthly newsletter.</p>
      <form method="post">
        <input type="email" placeholder="Email address" /><br>
        <input class="sign" type="submit" value="Signup" />
      </form>
    </div>
    <div class="four columns alpha">
      <h3>Community</h3>
      <ul>
        <li><a href="http://forum.nodebox.net/">Forum</a></li>
        <li><a href="http://twitter.com/nodebox">Twitter</a></li>
        <li><a href="http://facebook.com/nodebox">Facebook</a></li>
        <li><a href="https://github.com/nodebox/nodebox">GitHub</a></li>
      </ul>
    </div>
  </div>
  
  
</div> <!-- .gallery -->

<div class="connect row">
  <div class="eight columns emrg">
    <h2>EMRG</h2>
    <p>NodeBox is developed by the <strong>Experimental Media Research Group</strong>, a cross-domain research group associated with the <a href="http://www.sintlucasantwerpen.be/">Sint Lucas School of arts</a> of the <a href="http://www.kdg.be/">Karel de Grote-Hogeschool</a> (Antwerp, Belgium). </p>
    <p><strong>EMRG</strong> has been active since 2004 developing NodeBox and doing cutting-edge research in the domain of computer graphics, user experience, creativity, but also in artificial intelligence and natural language processing.</p>
    <p><a href="http://www.emrg.be/">www.emrg.be</a></p>
  </div>
</div>  <!-- .connect -->

