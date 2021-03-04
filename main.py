from flask import Flask
from ApiFiles.userApi import user_api
from ApiFiles.SearchApi import search_api

app=Flask(__name__)

app.register_blueprint(user_api)
app.register_blueprint(search_api)

if __name__ =='__main__' :
    app.run()