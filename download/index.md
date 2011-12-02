---
layout: default
title: Download NodeBox
section: download
---
* Use JS to find the correct version Mac / Win.
* Link to GitHub download.

<script>
  var OSName="Unknown OS";
  if (navigator.appVersion.indexOf("Win")!=-1) OSName="Windows";
  if (navigator.appVersion.indexOf("Mac")!=-1) OSName="MacOS";
  if (navigator.appVersion.indexOf("X11")!=-1) OSName="UNIX";
  if (navigator.appVersion.indexOf("Linux")!=-1) OSName="Linux";

  document.write('Your OS: '+OSName);
</script>