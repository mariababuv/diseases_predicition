from flask import *
from database import *
agdept=Blueprint('agdept',__name__)
@agdept.route('/agdepthome',methods=['get','post'])
def agdepthome():
	return render_template('agdepthome.html')
@agdept.route('/krishibhavan',methods=['get','post'])
def krishibhavan():
	data={}

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=="delete":
		q="delete from krishibhavan where krishibhavan_id='%s'"%(id)
		delete(q)

	if action=="update":
		q="select * from krishibhavan where krishibhavan_id='%s'"%(id)
		res=select(q)
		data['krishi']=res

	if 'update' in request.form:
		latitude=request.form['latitude']
		longitude=request.form['longitude']
		place=request.form['place']
		pincode=request.form['pincode']
		phone=request.form['phone']
		q="update krishibhavan set latitude='%s',longitude='%s',place='%s',pincode='%s',phone='%s' where krishibhavan_id='%s'"%(latitude,longitude,place,pincode,phone,id)
		update(q)
		
	if 'submit' in request.form:
		latitude=request.form['latitude']
		longitude=request.form['longitude']
		place=request.form['place']
		pincode=request.form['pincode']
		phone=request.form['phone']
		q="insert into krishibhavan values(null,'%s','%s','%s','%s','%s')"%(latitude,longitude,place,pincode,phone)
		insert(q)
	q="select * from krishibhavan"
	res=select(q)
	data['krishibhavan']=res
	return render_template('krishibhavan.html',data=data)
@agdept.route('/agnotification',methods=['get','post'])
def agnotification():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=="delete":
		q="delete from notification where notification_id='%s'"%(id)
		delete(q)

	if action=="update":
		q="select * from notification where notification_id='%s'"%(id)
		res=select(q)
		data['upnot']=res

	if 'update' in request.form:
		description=request.form['description']
		q="update notification set description='%s' where notification_id='%s'"%(description,id)
		update(q)

	if 'submit' in request.form:
		description=request.form['description']
		q="insert into notification values(null,'%s',curdate())"%(description)
		insert(q)
	q="select * from notification"
	res=select(q)
	data['notification']=res
	return render_template('agnotification.html',data=data)
@agdept.route('/govtpolicies',methods=['get','post'])
def govtpolicies():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=="delete":
		q="delete from govtpolicies where policy_id='%s'"%(id)
		delete(q)

	if action=="update":
		q="select * from govtpolicies where policy_id='%s'"%(id)
		res=select(q)
		data['upgovt']=res

	if 'update' in request.form:
		title=request.form['title']
		description=request.form['description']
		q="update govtpolicies set title='%s',description='%s' where policy_id='%s'"%(title,description,id)
		update(q)
		return redirect(url_for('agdept.govtpolicies'))

	if 'submit' in request.form:
		title=request.form['title']		
		description=request.form['description']
		q="insert into govtpolicies values(null,'%s','%s')"%(title,description)
		insert(q)
	q="select * from govtpolicies"
	res=select(q)
	data['govtpolicies']=res
	return render_template('govtpolicies.html',data=data)
@agdept.route('/viewfarmer',methods=['get','post'])
def viewfarmer():
	data={}

	q="select * from farmers"
	res=select(q)
	data['viewfarmer']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='greenhouse':
		q="select * from greenhouses where farmer_id='%s'"%(id)
		res=select(q)
		data['greenhouse']=res
	if action=="photos":
		q="select * from photos where farmer_id='%s'"%(id)
		res=select(q)
		data['photos']=res
	return render_template('viewfarmer.html',data=data)
# @agdept.route('/greenhouse',methods=['get','post'])
# def greenhouse():
# 	data={}

# 	q="select * from greenhouses"
# 	res=select(q)
# 	data['greenhouse']=res
# 	return render_template('greenhouse.html',data=data)
# @agdept.route('/photos',methods=['get','post'])
# def photos():
# 	data={}

# 	q="select * from photos"
# 	res=select(q)
# 	data['photos']=res
# 	return render_template('photos.html',data=data)
@agdept.route('/viewenquiry',methods=['get','post'])
def viewenquiry():
	data={}
	if 'update' in request.form:
		reply=request.form['reply']
		id=request.form['id']
		q="update enquiry set reply='%s' where enquiry_id='%s'"%(reply,id)
		update(q)
		return redirect(url_for('agdept.viewenquiry'))
	q="select * from enquiry inner join farmers using(farmer_id)"
	res=select(q)
	data['viewenquiry']=res
	return render_template('viewenquiry.html',data=data)