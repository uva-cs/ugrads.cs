Title: About
url: about.html
save_as: about.html
sortorder: 20

This site is maintained by [Aaron
Bloomfield](http://www.cs.virginia.edu/~asb), and is kept in the
[uva-cs/ugrads.cs github
repository](https://github.com/uva-cs/ugrads.cs).  Feel free to send
him any updates or suggested changes for this site.

Faculty can request to be allowed to directly edit the contents of the
git repo.  They can edit either via git or by editing online directly
via github.com.  Students can suggest changes by submitting a [pull
request](https://help.github.com/articles/about-pull-requests/) or by
emailing the contact above.

The actual HTML pages are built using
[Pelican](http://getpelican.com/) version 4.0.2, and the source is in
[Markdown](https://daringfireball.net/projects/markdown/syntax).
However, one does not need to have Pelican installed to edit the site,
as the [http://ugrads.cs.virginia.edu](http://ugrads.cs.virginia.edu)
site is automatically rebuilt every time content in the git repo is
changed on github.com.

Should you want to build the pages on your local machine, look at the
[Pelican quickstart guide](http://docs.getpelican.com/en/3.7.1/quickstart.html).
The quick overview is that you run `sudo pip install pelican markdown`
to install it, `pelican content -t theme/uvaeng/` to generate the
HTML files, and `python -m pelican.server` from the output/ directory
to be able to view it locally (browse to http://localhost:8000).

The design of this website was taken from the new (as of August 2017)
UVa Engineering website, and the look and feel is intentionally meant
to be the same.  All extra .css and .js files (including trackers)
were removed.
