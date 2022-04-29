import MySQLdb
from flask import Flask, Response
from os import environ

conn = MySQLdb.connect(host=environ.get('MYSQL_HOST'),
                        user=environ.get('MYSQL_USER'),
                        passwd=environ.get('MYSQL_PASSWORD'),
                        db=environ.get('MYSQL_DATABASE'))

app = Flask(__name__)

@app.route("/")
def index():
    conn.query("UPDATE `data` SET `value` = `value` + 1 WHERE `key` = 'view_count'")
    conn.query("SELECT `value` FROM `data` WHERE `key` = 'view_count'")
    result = conn.store_result()
    view_count = result.fetch_row()[0][0]
    conn.commit()
    return Response(f"Viewed {view_count} time{'s' if view_count != 1 else ''}!"), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')