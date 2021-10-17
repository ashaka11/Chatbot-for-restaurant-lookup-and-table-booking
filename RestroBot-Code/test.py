import mysql.connector
from decimal import Decimal

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

    #bid rid rname date 
    Allbid = []
  
	sqlquery='SELECT bid,rid,bookingdate FROM booking WHERE userid = "{}";'.format(userid)
	mycursor.execute(sqlquery)
	myresult = mycursor.fetchall()
	mydb.commit()

    i=0
	for row in myresult:
        print(row)
        data=Decimal(row[0])
        Allbid[0]=data
        Allbid[1]=row[1]
        Allbid[1]=row[2]
        print(Allbid)
 
