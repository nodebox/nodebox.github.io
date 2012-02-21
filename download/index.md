---
layout: default
title: Download NodeBox
section: download
---
<div class="download-button" id="download-windows">
  <h3>Windows</h3>
  <a href="https://github.com/downloads/nodebox/nodebox/nodebox-3.0a12-setup.exe" class="hero-button">Download NodeBox<small>Windows - Version 3.0a12</small></a>
</div>

<div class="download-button" id="download-mac">
  <h3>Mac OS X</h3>
  <a href="https://github.com/downloads/nodebox/nodebox/NodeBox-3.0a12.zip" class="hero-button">Download NodeBox<small>Mac OS X – Version 3.0a12</small></a>
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

Click the button above to start the download.

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
