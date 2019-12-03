from flask import Flask
from redis import Redis, RedisError
import socket


app = Flask(__name__)
redis = Redis(host="redis")


@app.route("/")
def hello():
    try:
        visits = redis.incr('counter')
    except RedisError:
        visits = "<i>No se pudo conectar a REDIS</i>"

    html = "<h2>Detalles de visitas</h2>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visitas:</b> {visits}<br/>" \
           "<br/>"

    return html.format(hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
