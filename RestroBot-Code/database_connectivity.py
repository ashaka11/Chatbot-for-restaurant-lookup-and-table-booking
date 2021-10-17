import mysql.connector
from restrodetails import RFetchId
from restrodetails import RFetchCapacitySlot
from decimal import Decimal

def DataUpdateUser(uname,number):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()

	sqlquery='INSERT INTO user (uname,phonenumber) VALUES ("{0}","{1}");'.format(uname,number)

	mycursor.execute(sqlquery)

	mydb.commit()

	return

def DataFetchUsername(number):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()

	sqlquery='SELECT uname FROM user WHERE phonenumber = {};'.format(number)

	mycursor.execute(sqlquery)

	myresult = mycursor.fetchone()
	
	mydb.commit()

	print("Myresult = {}".format(myresult))
	if myresult is None:
		return "nodata"

	for row in myresult:
		return row


def DataFetchUserId(number):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()

	sqlquery='SELECT userid FROM user WHERE phonenumber = {};'.format(number)

	mycursor.execute(sqlquery)

	myresult = mycursor.fetchone()
	
	mydb.commit()

	print("Myresult = {}".format(myresult))
	if myresult is None:
		return "nodata"

	for row in myresult:
		return row

def BookTable(ddict):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	rid=RFetchId(ddict["restro"])
	userid=DataFetchUserId(ddict["usernum"])

	sqlquery='INSERT INTO booking (rid,userid,bookingdate,timeslot,numofpeople) VALUES ("{0}","{1}","{2}","{3}","{4}");'.format(rid,userid,ddict["date"],ddict["time"],ddict["nop"])

	mycursor.execute(sqlquery)

	mydb.commit()

	return

def getCount(uid):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	sqlquery='SELECT COUNT(*) FROM booking WHERE userid={}'.format(uid)

	mycursor.execute(sqlquery)
	myresult = mycursor.fetchone()
	mydb.commit()
	for row in myresult:
		return row

def UpdateBookingTable(ddict):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	rid=RFetchId(ddict["restro"])
	# tsid=ddict["timeslot"]
	# date=ddict["bookingdate"]
	people=ddict["nop"]
	people = Decimal(people)
	scid=getscid(ddict)
	avcap=RFetchCapacitySlot(ddict) 
	avcap=avcap-people
	sqlquery='UPDATE slotcapacity SET availaiblecap={0} WHERE scid= {1}'.format(avcap,scid)
	mycursor.execute(sqlquery)

	mydb.commit()

	return


def getscid(ddict):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	rid=RFetchId(ddict["restro"])
	tsid=ddict["time"]
	date=ddict["date"]
	noofpeople=ddict["nop"]

	sqlquery='SELECT scid FROM slotcapacity WHERE rid= {0} AND tsid LIKE "{1}" AND date ="{2}" ;'.format(rid,tsid,date)
	mycursor.execute(sqlquery)
	
	myresult = mycursor.fetchone()

	mydb.commit()
	for row in myresult:
		return row