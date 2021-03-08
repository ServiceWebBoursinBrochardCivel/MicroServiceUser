from flask import Flask
from flask_cors import CORS
from Router.userApi import user_api
from Router.ConnectApi import search_api

app=Flask(__name__)
CORS(app)


app.register_blueprint(user_api)
app.register_blueprint(search_api)

if __name__ =='__main__' :
    app.run(port=5001)