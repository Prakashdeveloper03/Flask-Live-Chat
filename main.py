from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "#live-chat#"
socketio = SocketIO(app)

if __name__ == "__main__":
    socketio.run(app, debug=True)
