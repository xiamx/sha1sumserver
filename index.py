import web
import hashlib
urls = (
    '/(.*)', 'index'
)
app = web.application(urls, globals())

class index:
    def GET(self, text):
        if not text:
            text = 'World'
        h = hashlib.new('sha1')
        h.update(text)
        for i in range(10000):
            h.update(h.hexdigest())
        return h.hexdigest()

if __name__ == "__main__":
    app.run()
