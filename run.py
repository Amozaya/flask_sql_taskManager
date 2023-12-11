import os
from taskmanager import app

def test_connection(self):
    with app.app_context():
    if __name__ == "__main__":
        app.run(
            host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG")
        )