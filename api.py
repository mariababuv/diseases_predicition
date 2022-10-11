from flask import Blueprint,request
from database import *
import demjson
from keras.models import load_model
from keras.backend import clear_session
from core import load_image
import numpy as np
import uuid


api=Blueprint('api',__name__)
@api.route('/login/',methods=['get','post'])
def login():
	data={}
	username=request.args['username']
	password=request.args['password']
	q="select * from login where  username='%s' and password='%s'" %(username,password)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return  demjson.encode(data)

@api.route('/register/',methods=['get','post'])
def register():
	data={}
	
	first_name = request.args['firstname']
	last_name = request.args['lastname']
	gender = request.args['gender']
	dob = request.args['dob']
	place = request.args['place']
	pincode = request.args['pincode']
	phone = request.args['phone']
	lati = request.args['lati']
	longi = request.args['longi']
	username = request.args['username']
	password = request.args['password']
	
	q = "insert into login values(null,'%s','%s','farmer')" % (username,password)
	login_id = insert(q)
	q = "insert into farmers values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (login_id,first_name,last_name,dob,gender,lati,longi,place,pincode,phone)
	print(q)
	insert(q)
	data['status'] = 'success'
	return demjson.encode(data)




@api.route('/viewenquiry/',methods=['get','post'])
def viewenquiry():
	data={}
	logid=request.args['logid']
	
	q="select * from enquiry where  farmer_id=(select farmer_id from farmers where login_id='%s')" %(logid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="viewenquiry"
	return  demjson.encode(data)


@api.route('/addenquiry/',methods=['get','post'])
def addenquiry():
	data={}
	
	enquiry = request.args['enquiry']
	logid = request.args['logid']
	
	q = "insert into enquiry values(null,(select farmer_id from farmers where login_id='%s'),'%s','NA',curdate())" % (logid,enquiry)
	insert(q)
	data['status'] = 'success'
	data['method'] = 'addenquiry'
	return demjson.encode(data)


@api.route('/get_model/')
def get_classess():
	data= {}
	q = "select * from model"
	res = select(q)
	data['data'] = res
	data['status'] = 'success'
	return demjson.encode(data)


@api.route('/upload_image/',methods=['get','post'])
def upload_image():
	data={}
	image = request.files['image']
	login_id = request.form['login_id']
	filename = "static/uploads/" + str(uuid.uuid4()) + "." + "jpg"
	image.save(filename)
	model_id = request.form['model_id']
	q = "select * from model where model_id='%s'" % model_id
	res = select(q)
	clear_session()
	model = load_model(res[0]['model_path'])
	# filename = "Data/Tomato_Bacterial_spot/00416648-be6e-4bd4-bc8d-82f43f8a7240___GCREC_Bact.Sp 3110.JPG"
	image = load_image(filename,(224,224))
	image = np.expand_dims(image, axis=0)
	result = model.predict(image)
	index = np.argmax(result)
	q = "select * from label where model_id='%s'" % model_id
	res = select(q)
	q = "insert into photos values(null,(select farmer_id from farmers where login_id='%s'),'%s',curdate())" % (login_id,filename)
	insert(q)
	data['data'] = [res[index]]
	data['status'] = 'success' 
	return demjson.encode(data)


@api.route('/viewgreenhouse/',methods=['get','post'])
def viewgreenhouse():
	data={}
	logid=request.args['logid']
	
	q="select * from greenhouses where  farmer_id=(select farmer_id from farmers where login_id='%s')" %(logid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="viewgreenhouse"
	return  demjson.encode(data)


@api.route('/greenhouse/',methods=['get','post'])
def greenhouse():
	data={}
	
	area = request.args['area']
	crop = request.args['crop']
	date = request.args['date']
	facilities = request.args['facilities']
	logid = request.args['logid']
	
	q = "insert into greenhouses values(null,(select farmer_id from farmers where login_id='%s'),'%s','%s','%s','%s')" % (logid,area,crop,date,facilities)
	insert(q)
	data['status'] = 'success'
	data['method'] = 'greenhouse'
	return demjson.encode(data)

@api.route('/viewnotification/',methods=['get','post'])
def viewnotification():
	data={}
	
	q="select * from notification" 
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="viewnotification"
	return  demjson.encode(data)

@api.route('/viewkrishibhavans/',methods=['get','post'])
def viewkrishibhavans():
	data={}
	
	q="select * from krishibhavan" 
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="viewkrishibhavans"
	return  demjson.encode(data)