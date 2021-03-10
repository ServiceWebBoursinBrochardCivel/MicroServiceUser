from flask import Flask,send_from_directory
from flask_cors import CORS
from Router.userApi import user_api
from Router.ConnectApi import connect_api
from flask_swagger_ui import get_swaggerui_blueprint

app=Flask(__name__)
CORS(app)


app.register_blueprint(user_api)
app.register_blueprint(connect_api)


@app.route('/Router/<path:path>')
def send_api(path) :
    return send_from_directory('Router',path)


SWAGGER_URL = '/spec'
API_URL = '/Router/swagger.json'
swaggerui_api = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name' : "UsersApi"
    }
)
app.register_blueprint(swaggerui_api,url_prefix=SWAGGER_URL)

if __name__ =='__main__' :
    app.run(port=5001)