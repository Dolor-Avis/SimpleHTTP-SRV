from twisted.internet import reactor
from twisted.web import static, server
from twisted.web.server import Site, GzipEncoderFactory
from twisted.web.resource import EncodingResourceWrapper
from twisted.python import log


class WebServer(static.File):
    def getChild(self, path, request):
        child = static.File.getChild(self, path, request)
        return EncodingResourceWrapper(child, [GzipEncoderFactory()])

    def loger(path):
        log.startLogging(open(f'{path}', 'w'))


if __name__ == "__main__":
    WebServer.loger("./resources/file.log")
    root = server.Site(WebServer('./resources','text/html'))
    site = Site(root)
    reactor.listenTCP(8090, site)
    reactor.run()

