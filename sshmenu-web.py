import logging
from bottle import route, run,template, static_file,request,redirect
from raven.contrib.bottle import Sentry
import bottle
import json
from raven import Client
app = bottle.app()
app.catchall = False
client = Client('http://413c6240283b405e8bb356b7fa94bfed:336e485eed974c45a51808f3e7e638a0@str.blaq.ru/6')
app = Sentry(app, client)
logging.basicConfig(format=u'[%(asctime)s] %(levelname)-8s %(message)s', level=logging.DEBUG, filename=u'sshmenu.log')
logging.info("Start server: sshmenu-web")


def get_list():
    with open('sshmenu.json') as data_file:
        data = json.load(data_file)
    return data


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='/home/djet/systems/git/sshmenu/static')

@route('/<action>')
def admin(action):
    if action == "login":
        return template('tpl/login.tpl', action=action)
    elif action == "admin":
        list = get_list()
        return template('tpl/admin.tpl', list=str(list))

    else:
        return ('tpl/index.tpl')





@route('/login', method='POST')
def check_login():
    login = request.files.get('login')
    password = request.files.get('password')

    if logging == "admin" and password == "admin":
        redirect("/admin")

run(host='0.0.0.0', port=8080, interval=1, debug=True, reloader=True, app=app)

