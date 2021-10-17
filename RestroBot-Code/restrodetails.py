import mysql.connector

# -----rid from rname
def RFetchId(restroname):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	sqlquery='SELECT rid FROM restaurant WHERE name = "{}";'.format(restroname)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchone()
	mydb.commit()

	for row in myresult:
		return row

# --- rname from rid
def RFetchName(rid):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	sqlquery='SELECT name FROM restaurant WHERE rid = "{}";'.format(rid)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchone()
	mydb.commit()

	for row in myresult:
		return row

#----- image from rname
def RFetchImage(restroname):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	sqlquery='SELECT imageurl FROM restaurant WHERE name = "{}";'.format(restroname)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchone()
	mydb.commit()

	for row in myresult:
		return row

#------ street from rname
def RFetchStreet(restroname):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	sqlquery='SELECT street FROM restaurant WHERE name = "{}";'.format(restroname)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchone()
	mydb.commit()

	for row in myresult:
		return row

# -- area from rname
def RFetchArea(restroname):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	sqlquery='SELECT area FROM restaurant WHERE name = "{}";'.format(restroname)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchone()
	mydb.commit()

	for row in myresult:
		return row	

#--- rating from rname
def RFetchRating(restroname):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	sqlquery='SELECT rating FROM restaurant WHERE name = "{}";'.format(restroname)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchone()
	mydb.commit()

	for row in myresult:
		return row


#--- restro type from rname
def RFetchRType(restroname):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	sqlquery='SELECT type FROM restaurant WHERE name = "{}";'.format(restroname)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchone()	
	mydb.commit()

	for row in myresult:
		return row

# check restro name in db
def RCheckName(restroname):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	sqlquery='SELECT rid FROM restaurant WHERE name = "{}";'.format(restroname)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchone()
	mydb.commit()

	if myresult is None:
		return "nodata"

	for row in myresult:
		return row

#--- foodtype from rname
def RFetchFoodType(restroname):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	sqlquery='SELECT foodtype FROM restaurant WHERE name = "{}";'.format(restroname)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchone()
	mydb.commit()

	for row in myresult:
		return row

#--- capacity from rname
def RFetchCapacity(restroname):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	sqlquery='SELECT capacity FROM restaurant WHERE name = "{}";'.format(restroname)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchone()
	mydb.commit()

	for row in myresult:
		return row

#--- opening time from rname
def RFetchOpeningTime(restroname):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	sqlquery='SELECT openingtime FROM restaurant WHERE name = "{}";'.format(restroname)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchone()
	mydb.commit()

	for row in myresult:
		return row

#---closing time from rname
def RFetchClosingTime(restroname):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	sqlquery='SELECT closingtime FROM restaurant WHERE name = "{}";'.format(restroname)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchone()
	mydb.commit()

	for row in myresult:
		return row

#--- rtype from rname
def RFetchCapacitySlot(ddict):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	timevar=ddict["time"]
	datevar=ddict["date"]
	restvar=ddict["restro"]
	seats=ddict["nop"]

	rid=RFetchId(restvar)

	print("rid={}".format(rid))
	print("timevar={}".format(timevar))
	print("datevar={}".format(datevar))
	print("restvar={}".format(restvar))
	print("seats={}".format(seats))

	sqlquery='SELECT availaiblecap FROM slotcapacity WHERE rid = {0} AND tsid LIKE "{1}" AND date = "{2}" ;'.format(rid,timevar,datevar)

	mycursor.execute(sqlquery)

	myresult = mycursor.fetchone()
	print("Myresult = {}".format(myresult))
	mydb.commit()

	for row in myresult:
		return row


#--- opening time slot from rname from tsid table
def RFetchOpeningTimeSlot(restroname):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()
	sqlquery='SELECT openingtime FROM timeslots WHERE tsid LIKE "{}";'.format(restroname)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchone()
	mydb.commit()

	for row in myresult:
		return row

#---closing time slot from rname from timeslots table
def RFetchClosingTimeSlot(restroname):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	mycursor = mydb.cursor()

	sqlquery='SELECT closingtime FROM timeslots WHERE tsid LIKE "{}";'.format(restroname)

	mycursor.execute(sqlquery)

	myresult = mycursor.fetchone()
	
	mydb.commit()

	for row in myresult:
		return row

#------------
def RFetchCuisine(restroname):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database="restaurant"
	)

	rid=RFetchId(restroname)

	mycursor = mydb.cursor()
	sqlquery='SELECT cname FROM restaurantcuisine  INNER JOIN cuisine ON restaurantcuisine.cid =cuisine.cid WHERE rid = "{}";'.format(rid)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchall()
	mydb.commit()

	count=0
	cuisinenames=" "
	for row in myresult:
		print("row[0] : {}".format(row[0]))
		count=count+1
		if count == 1 :
			cuisinenames = cuisinenames  + row[0]
		else :
			cuisinenames = cuisinenames + " , " + row[0]

	print("count={}".format(count))
	print(cuisinenames)
	return cuisinenames
	# cuisinenames =""
	# for i in range(count) :
	# 	sqlquery='SELECT cname FROM cuisine WHERE cid = "{}";'.format(list_cid[i])
	# 	mycursor.execute(sqlquery)
	# 	myresult = mycursor.fetchone()
	# 	for row in myresult:
	# 		if i == 1 :
	# 			cuisinenames = cuisinenames  + row[0]
	# 		else :
	# 			cuisinenames = cuisinenames + " , " + row[0]
