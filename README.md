nodebox.net
===========
This is the website for NodeBox.

Frameworks
----------
* [Jekyll][] - Transform dynamic content into a static site.
* [Normalize][] - An alternative to CSS reset which keeps sane browser defaults and makes them consistent across browsers.
* [Skeleton][] - A responsive CSS grid that scales nicely to mobile sizes.

Installing on Mac
-----------------
Install [Xcode][] first.

    sudo gem update --system
    sudo gem install rake jekyll RedCloth
    sudo easy_install pygments

Installing on Ubuntu
--------------------

    sudo apt-get install ruby rubygems
    sudo gem install rubygems-update
    sudo gem install rake jekyll RedCloth
    sudo easy_install pygments

Running
-------
To build the website:

    rake

To run the built-in server:

    rake server
    
To deploy to the live server:

    rake deploy

License
-------
Text & images on this blog are licensed under the [Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License][cc].

[Jekyll]: http://github.com/mojombo/jekyll
[Normalize]: https://github.com/jonathantneal/normalize.css
[Skeleton]: http://www.getskeleton.com/
[Xcode]: http://itunes.apple.com/us/app/xcode/id422352214
[cc]: http://creativecommons.org/licenses/by-nc-nd/3.0/