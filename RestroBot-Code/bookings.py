import mysql.connector
from decimal import Decimal
from restrodetails import RFetchName
from datetime import *
def getBookings(uid):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	bid=getBidB(uid)
	rid=getRidB(bid)
	restroname=RFetchName(rid)
	bookingdate=getDateB(bid)
	numofpeople=getNumofpeopleB(bid)

	ddict={
		"bid":bid,
		"rname":restroname,
		"date":bookingdate,
		"numofpeople":numofpeople
	}
	
	return ddict

def getBidB(uid):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	sqlquery='SELECT bid FROM booking WHERE userid = "{}";'.format(uid)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchone()
	mydb.commit()

	for row in myresult:
		return row

def getRidB(bid):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	sqlquery='SELECT rid FROM booking WHERE bid = "{}";'.format(bid)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchone()
	mydb.commit()

	for row in myresult:
		return row

def getDateB(bid):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	sqlquery='SELECT bookingdate FROM booking WHERE bid = "{}";'.format(bid)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchone()
	mydb.commit()

	for row in myresult:
		return row

def getNumofpeopleB(bid):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	sqlquery='SELECT numofpeople FROM booking WHERE bid = "{}";'.format(bid)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchone()
	mydb.commit()

	for row in myresult:
		return row

def BcheckBid(ddict):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	bid=ddict["bid"]
	uid=ddict["uid"]

	mycursor = mydb.cursor()
	sqlquery='SELECT bid FROM booking WHERE userid = "{}";'.format(uid)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchall()
	mydb.commit()

	bid=Decimal(bid)
	for row in myresult:
		data=Decimal(row[0])
		print("row[0]={}".format(data))
		print("bid = {}".format(bid))
		if data == bid :
			return bid

	print("NOne returning")	
	return None


def cancelBooking(bid):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	print("from cancel booking bid = {}".format(bid))
	sqlquery='DELETE FROM booking WHERE booking.bid = {};'.format(bid)
	mycursor.execute(sqlquery)
	mydb.commit()
	print("deleted")
	return

def getAllBookings(ddict):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)
	mycursor = mydb.cursor()

	count=ddict["count"]
	userid=ddict["userid"]

    #bid  rname date 
	
  
	sqlquery='SELECT bid,rid,bookingdate FROM booking WHERE userid = "{}";'.format(userid)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchall()
	mydb.commit()

	Liist=[]
	i=0
	for row in myresult:
		print(row)
		Allbid = []
		data=Decimal(row[0])
		Allbid.insert(0,data)
		rname=RFetchName(row[1])
		Allbid.insert(1,rname)
		Allbid.insert(2,row[2])
		print(Allbid)
		Liist.insert(i,Allbid)
		i=i+1
	print(Liist)
	
	return Liist

def BCheckDate(userdate):
	
	currentdate = datetime.now()
	year=currentdate.strftime("%Y")
	day=currentdate.strftime("%d")
	month=currentdate.strftime("%B")

	userdate = datetime.strptime(userdate, "%Y-%m-%d")
	useryear= userdate.strftime("%Y")
	usermonth= userdate.strftime("%B")
	userday= userdate.strftime("%d")

	if currentdate > userdate :
		if (useryear == year) and (usermonth == month and userday == day) :
			return "ok"
		else :
			return "invalid" 

def BCheckDateInterval(userdate):
	
	currentdate = datetime.now()
	validdate = currentdate + timedelta(days = 7)
	userdate = datetime.strptime(userdate, "%Y-%m-%d")
	if validdate < userdate :
		return "invalid"

def BCheckTime(timevar,userdate):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	print("time={} date={}".format(timevar,userdate) )

	currenttime = datetime.now()
	print("Current time={}".format(str(currenttime)))

	year=currenttime.strftime("%Y")
	month=currenttime.strftime("%B")
	day=currenttime.strftime("%d")

	currenthour=int(currenttime.strftime("%H"))
	currentminutes=int(currenttime.strftime("%M"))
	print("Current hour= {} minutes={}".format(currenthour,currentminutes))

	userdate=datetime.strptime(userdate, "%Y-%m-%d")
	useryear= userdate.strftime("%Y")
	usermonth= userdate.strftime("%B")
	userday= userdate.strftime("%d")
	
	mycursor = mydb.cursor()
	sqlquery='SELECT openingtime FROM timeslots WHERE tsid = "{}";'.format(timevar)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchall()
	mydb.commit()

	for row in myresult:
		print("openingtime={}".format(row[0]))

		usertime=str(row[0])
		hourandmin=usertime.split(':')
		userhour=int(hourandmin[0])
		userminutes=int(hourandmin[1])
		print("User selected hour= {} minutes={}".format(userhour,userminutes))

		if (useryear == year) and (usermonth == month and userday == day) :
			if userhour < currenthour :
				return "invalid"
			elif  userhour == currenthour :
				if userminutes <= currentminutes :
					return "invalid"