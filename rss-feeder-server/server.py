import web
import feedparser
import validators
from web.wsgiserver import CherryPyWSGIServer
        
urls = (
    '/feed', 'feed'
)
app = web.application(urls, globals())
render = web.template.render('templates/')

class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

class feed:
	def GET(self):
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Credentials', 'true')
		i = web.input()
		try:
			url = str(i['url'])
		except:
			# Signals that no url key was passed
			return {}

		#validate url here
		if not self.validate_url(url):
			return {}
		
		feed = feedparser.parse(url)
		if feed['feed'] == {}:
		# Signifies that the url given might not be a RSS endpoint
			return {}
		return self.get_feed_data(feed)

	def get_feed_data(self, feed=None):
		if feed is None:
			return {}
		feed_data = []
		for i in feed.entries:
			feed_item = {}
			feed_item['text'] = (i.link)
			feed_item['id'] = (i.id)
			feed_item['strapline'] = 'date'
			feed_item['published'] = (i.published)
			feed_item['summary'] = (i.summary)
			feed_item['title'] = (i.title)
			feed_item['summary_detail'] = (i.summary_detail)
			feed_data.append(feed_item)
		import json
		return json.dumps(feed_data)

	def validate_url(self, url=None):
		if url is None:
			return False
		return validators.url(url)

if __name__ == "__main__":
    app = MyApplication(urls, globals())

    # ssl_cert = 'myserver.crt'
    # ssl_key = 'myserver.key'
    # CherryPyWSGIServer.ssl_certificate = ssl_cert
    # CherryPyWSGIServer.ssl_private_key = ssl_key
    app.run(port=8888)
