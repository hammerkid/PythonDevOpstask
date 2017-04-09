from flask import Flask, render_template, request, url_for, json, Response
from db import connection
from werkzeug.contrib.fixers import ProxyFix

application = Flask(__name__)

application.wsgi_app = ProxyFix(application.wsgi_app)

@application.route('/')
def form():
"""render forms for submit inputed data"""
    return render_template('form_submit.html')

@application.route('/post/', methods=['POST'])
def hello():
"""render submited data if get it from front end, else respond when get a POST request"""
    if request.headers['Content-Type'] == 'application/json':
        data_responce = {'ok':Response().status, 'error':{'code':Response().status_code, 'message':'POST data accepted'} }
        js = json.dumps(data_responce)
        req = request.json
        c, conn = connection()
        c.execute("INSERT INTO data (name, value, date) VALUES (%s, %s, %s)", (req['name'], req['value'], req['date']))
        conn.commit()
        c.close()
        conn.close()
        return js
    else:
        name=request.form['name']
        value=request.form['value']
        date=request.form['date']
        c, conn = connection()
        c.execute("INSERT INTO data (name, value, date) VALUES (%s, %s, %s)", (name, value,date))
        conn.commit()
        c.close()
        conn.close()
        return render_template('form_action.html', name=name, value=value, date=date)

if __name__ == '__main__':
  application.run(
        host="0.0.0.0")


