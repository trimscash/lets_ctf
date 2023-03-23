from flask import Flask, render_template, request, redirect, url_for, Markup
from markupsafe import escape
from sqlalchemy import create_engine, text

MYSQL_DATABASE="ctfdb"
MYSQL_USER="user"
MYSQL_PASSWORD="password_1111"

engine = create_engine(f'mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@host.docker.internal:3306/{MYSQL_DATABASE}')
app = Flask(__name__)


@app.route("/", methods=["POST"])
def index_post():
    table=""
    with engine.connect() as conn:
        try:
            res = conn.execute(text("SELECT * FROM users WHERE name='{}'".format(request.form["username"])))
        except:
            return render_template('index.html', table=Markup("<font color='red'>SQL Error</font>"))

        for row in res:
            table+=str(row)+"<br>"
    return render_template('index.html', table=Markup(table))

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')


@app.errorhandler(404)
def error_404(error):
    return '''
        <h1>404</h1>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0")
