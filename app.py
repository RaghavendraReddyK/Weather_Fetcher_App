from flask import Flask
from controllers import (health_check, sign_up)

app = Flask(__name__)

route_list = [

    ['GET', '/health', health_check],
    ['POST', '/signup', sign_up]
    ]

def mount_routes():
    for route in route_list:
        method, path, func = route
        app.add_url_rule(path, view_func=func, methods=[method], strict_slashes=False)
        
mount_routes()

if __name__ == "__main__":
    app.run(debug=True)
