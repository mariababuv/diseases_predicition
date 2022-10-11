from flask import Flask
from public import public
from agdept import agdept                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
from api import api
app=Flask(__name__)
app.register_blueprint(public)
app.register_blueprint(agdept,url_prefix='/agdept')
app.register_blueprint(api,url_prefix='/api')
app.run(debug=True,port=5000,host="192.168.43.34")

