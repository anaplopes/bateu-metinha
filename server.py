# -*- coding: utf-8 -*-
# import os
# from core.app import create_app
# from gevent.pywsgi import WSGIServer
# import werkzeug.serving


# app = create_app()
# app.config['PROPAGATE_EXCEPTIONS'] = True

# @werkzeug.serving.run_with_reloader
# def runServer():
#     http_server = WSGIServer(('0.0.0.0', 5000), app)
#     print("Gevent serve forever on", 5000)
#     http_server.serve_forever()

from core.app import create_app as app


if __name__ == '__main__':
    ip = '0.0.0.0'
    port = 5000
    
    app.run(host=ip, port=port, use_reloader=debug)
