from flask import Flask, render_template, app


@app.route('/')
def senddata():
    name = 'world'
    return render_template('FrameWorld.html', data=name)


# from flask import Flask
#
# App = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     return '''<!DOCTYPE HTML><html>
#   <head>
#     <title>Flask app</title>
#   </head>
#   <body>
#     <h1>Hello Flask!</h1>
#   </body>
# </html>'''
#
#
# @app.route('/about')
# def about():
#     return 'About 페이지'