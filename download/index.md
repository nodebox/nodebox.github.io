---
layout: default
title: Download NodeBox
section: download
---
<div class="download-button" id="download-windows">
  <a href="https://github.com/downloads/nodebox/nodebox/nodebox-2.1-setup.exe" class="hero-button">Download NodeBox<small>Windows – Version 2.2</small></a>
</div>

<div class="download-button" id="download-mac">
  <a href="https://github.com/downloads/nodebox/nodebox/NodeBox-2.2.zip" class="hero-button">Download NodeBox<small>Mac OS X – Version 2.2</small></a>
</div>

<div class="download-button" id="download-linux">
  We don't have a package ready, but executing the following commands in the terminal will get you going:
  <pre>
    sudo apt-get install git-core openjdk-6-jdk ant
     git clone git://github.com/nodebox/nodebox.git
     cd nodebox
     ant run
  </pre>
</div>

While the software is downloading, take a look at the [getting started page](/documentation/tutorial/getting-started.html).

Problems downloading? Try the [GitHub Downloads Page](http://github.com/nodebox/nodebox/downloads).

<script>
  var os = 'other';
  if (navigator.appVersion.indexOf('Win')!=-1) os = 'windows';
  if (navigator.appVersion.indexOf('Mac')!=-1) os = 'mac';
  if (navigator.appVersion.indexOf('Linux')!=-1) os = 'linux';

  $('#download-' + os).show();
</script>
