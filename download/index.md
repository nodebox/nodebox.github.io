---
layout: page
title: Download NodeBox
section: download
---
NodeBox 1
---------
Download

NodeBox OpenGL
---------
Download

NodeBox 3
---------
Download

<div class="download-button" id="download-windows">
  <h3>Windows</h3>
  <a href="https://github.com/downloads/nodebox/nodebox/NodeBoxSetup.exe" class="hero-button">Download NodeBox<small>for Windows</small></a>
</div>

<div class="download-button" id="download-mac">
  <h3>Mac OS X</h3>
  <a href="https://github.com/downloads/nodebox/nodebox/NodeBox.zip" class="hero-button">Download NodeBox<small>for Mac OS X</small></a>
</div>

<div class="download-button" id="download-linux">
  <h3>Linux</h3>
  We don't have a package ready, but executing the following commands in the terminal will get you going:
  <pre>
    sudo apt-get install git-core openjdk-6-jdk ant
     git clone git://github.com/nodebox/nodebox.git
     git checkout immutable-nodes
     cd nodebox
     ant run
  </pre>
</div>

While the software is downloading, take a look at the [getting started page](/documentation/tutorial/getting-started.html).

Problems downloading? Try the [GitHub Downloads Page](http://github.com/nodebox/nodebox/downloads).

<script>
  $('.download-button').hide();
  var os = 'other';
  if (navigator.appVersion.indexOf('Win') != -1) os = 'windows';
  if (navigator.appVersion.indexOf('Mac') != -1) os = 'mac';
  if (navigator.appVersion.indexOf('Linux') != -1 || navigator.userAgent.indexOf('Linux') != -1 || navigator.userAgent.indexOf('Unix') != -1) os = 'linux';

  $('#download-' + os).show();
</script>
