from flask import *
from database import *
public=Blueprint('public',__name__)
@public.route('/',methods=['get','post'])
def index():
	return render_template('index.html')
@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		username=request.form['uname']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		if res:
			if res[0]['usertype']=="agdept":
				return redirect(url_for('agdept.agdepthome'))
	return render_template('login.html')