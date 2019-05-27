# rss-feeder
This is a simple rss-feeder which takes URL as an input parameter and displays the feed.
It is a full stack application with Angular 2 in the front end and Python in the back end.

Libraries used for Python:
-web.py
-feedparser
-pyOpenSSL
-validators

The UI has been taken from a pen from codepen.io and is under the MIT license.

In order to run this locally, simply take the pull of the repo. Pip install the requirements.txt in the rss-feeder-server folder.

- To run the server:
1.Browse to the rss-feeder-server folder.
2.Run 'python server.py'.
3.If PEM passphrase is asked: enter '1234'

- To run the dashboard:
1.Browse to the rss-feeder folder.
2.Run npm install
3.Run ng serve -o
