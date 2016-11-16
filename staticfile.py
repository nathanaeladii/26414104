    @cherrypy.expose
    def index(self):
        return """<html>
  <head>
    <link 
      href="/static/css/style.css"
      rel="stylesheet">
  </head>
  <body>
    <form method="get" 
          action="generate">
      <input type="text" value="8" 
        name="length"/>
      <button type="submit">
        Give it now!
      </button>
    </form>
  </body>
</html>"""

if __name__ == '__main__':
  conf = {
    '/': {
      'tools.sessions.on': True,
      'tools.staticdir.root': \
        os.path.abspath(os.getcwd())
    },
    '/static': {
      'tools.staticdir.on': True,
      'tools.staticdir.dir': \
        './public
    }
  }

cherrypy.quickstart( \
  StringGenerator(), '/', conf)

