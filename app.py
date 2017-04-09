from flask import Flask, render_template, request, url_for, json, Response
from db import connection

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form_submit.html')

@app.route('/post/', methods=['POST'])
def hello():
    if request.headers['Content-Type'] == 'application/json':
        data_responce = {'ok':Response().status, 'error':{'code':Response().status_code, 'message':'POST data accepted'} }
        js = json.dumps(data_responce)
        req = request.json
        print (req, type(req), type(request.json))
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

# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
  )

