# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from decimal import Decimal
from rasa_sdk import Action, Tracker , FormValidationAction
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import CollectingDispatcher
from database_connectivity import DataUpdateUser
from database_connectivity import DataFetchUsername
from database_connectivity import DataFetchUserId
from restrodetails import RFetchImage
from restrodetails import RFetchStreet
from restrodetails import RFetchArea
from restrodetails import RFetchRating
from restrodetails import RFetchRType
from restrodetails import RFetchFoodType
from restrodetails import RFetchCapacity
from restrodetails import RFetchOpeningTime
from restrodetails import RFetchClosingTime
from restrodetails import RCheckName
from restrodetails import RFetchCapacitySlot
from restrodetails import RFetchOpeningTimeSlot
from restrodetails import RFetchClosingTimeSlot
from restrodetails import  RFetchCuisine
from database_connectivity import BookTable
from database_connectivity import getCount
from database_connectivity import UpdateBookingTable
from bookings import getBookings
from bookings import BcheckBid
from bookings import cancelBooking
from bookings import getAllBookings
from bookings import BCheckDate
from bookings import BCheckDateInterval
from bookings import BCheckTime

# User details form for first sign in and ask for both uname and number
class ValidateSignUpForm(Action):

    def name(self) -> Text:
        return "userdetails_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict) -> List[EventType]:

        print("1")
        required_slots = ["number","uname"]

        print("2")
        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                #for an empty slot, request user to fill it
                return [SlotSet("requested_slot", slot_name)]

        print("3")    
        #when all required slots are filled
        return [SlotSet("requested_slot", None)]

##Validating SIGNUP FORM
class ValidateUserdetailsForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_userdetails_form"

    def validate_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate number value."""

        # If the name is super short, it might be wrong.
        print(f"Contact number given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) != 10:
            dispatcher.utter_message(text="Not a 10 digit number")
            return {"number": None}
        else:
            return {"number": slot_value}

    def validate_uname(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate uname value."""

        # If the name is super short, it might be wrong.
        print(f"Name = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name.")
            return {"uname": None}
        else:
            return {"uname": slot_value}

# submit form for details uname and number and update details
class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher,
            tracker: Tracker,
            domain: "DomainDict",) -> List[Dict[Text, Any]]:

        print("4")
        username=tracker.get_slot("uname")
        usernumber=tracker.get_slot("number")

        print("5")
        DataUpdateUser(username,usernumber)
        dispatcher.utter_message(text=" Hey {} !".format(username))


# User details form for login and ask for number
class ValidateSignInForm(Action):

    def name(self) -> Text:
        return "usernumber_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict) -> List[EventType]:

        required_slots = ["number"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                #for an empty slot, request user to fill it
                return [SlotSet("requested_slot", slot_name)]

        #when all required slots are filled
        return [SlotSet("requested_slot", None)]

# Validate user number for sign in
class ValidateUsernumberForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_usernumber_form"

    def validate_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate number value."""

        # If the name is super short, it might be wrong.
        print(f"Contact number given = {slot_value} length = {len(slot_value)}")
        # usernumber=tracker.get_slot("number")
        name=DataFetchUsername(slot_value)
        print(f"name = {name}")
        print(f"name={name}")

        if len(slot_value) != 10:
            dispatcher.utter_message(text="Not a 10 digit number")
            return {"number": None}

        elif DataFetchUsername(slot_value) == "nodata":
            dispatcher.utter_message(text="Not seen this number before")
            return {"number": None}

        else:
            return {"number": slot_value}

# submit form for number and fetch name from database
class ActionSubmitNumber(Action):

    def name(self) -> Text:
        return "action_submitnumber"

    def run(self, dispatcher,
            tracker: Tracker,
            domain: "DomainDict",) -> List[Dict[Text, Any]]:

        usernumber=tracker.get_slot("number")
        name=DataFetchUsername(usernumber)
        SlotSet("uname",name)
        output="Welcome back {} !".format(name)
        dispatcher.utter_message(text=output)

        return


# book table form
class ValidateBookTableDemoForm(Action):

    def name(self) -> Text:
        return "booktable_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict) -> List[EventType]:

        required_slots = ["rname","btdate","bttime","noofpeople"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                #for an empty slot, request user to fill it
                return [SlotSet("requested_slot", slot_name)]

        print("3")    
        #when all required slots are filled
        return [SlotSet("requested_slot", None)]


# validate book a table form
class ValidateBookTableForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_booktable_form"

    def validate_rname(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate rname value."""

        # If restaurant name could not be found in database.
        if RCheckName(slot_value) == "nodata":
            dispatcher.utter_message(text="Could not find a restaurant with that name")
            return {"rname": None}
        else:
            return {"rname": slot_value}

    def validate_btdate(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate btdate value."""

        if BCheckDate(slot_value) == "invalid":
            dispatcher.utter_message(text="You cannot enter a past date")
            return {"btdate": None}
        elif BCheckDateInterval(slot_value) == "invalid":
            dispatcher.utter_message(text="Date is not within 7 day interval")
            return {"btdate": None}
        else:
            return {"btdate": slot_value}

    def validate_bttime(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate bttime value."""

        userdate=tracker.get_slot("btdate")
        if BCheckTime(slot_value,userdate) == "invalid":
            dispatcher.utter_message(text="You cannot select that time slot")
            return {"bttime": None}
        else:
            return {"bttime": slot_value}

    def validate_noofpeople(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate noofpeople value."""

        timevar=tracker.get_slot("bttime")
        datevar=tracker.get_slot("btdate")
        restrovar=tracker.get_slot("rname")
        usernumber=tracker.get_slot("numbers")
        seats=slot_value

        ddict={
            "time":timevar,
            "restro":restrovar,
            "usernum":usernumber,
            "date":datevar,
            "nop":seats
        }
        avcap=RFetchCapacitySlot(ddict)
        # If the requested seats is greater than available, than ask again .
        seats=Decimal(seats)
        avcap=Decimal(avcap)
        if seats > avcap:
            dispatcher.utter_message(text=f"Table of {slot_value} not available")
            return {"noofpeople": "0"}
        else:
            return {"noofpeople": slot_value}


# submit form for book a table
class ActionSubmitBtForm(Action):

    def name(self) -> Text:
        return "action_submit_btform"

    def run(self, dispatcher,
            tracker: Tracker,
            domain: "DomainDict",) -> List[Dict[Text, Any]]:
        if tracker.get_slot("noofpeople") == "0":
            dispatcher.utter_message(text="Cannot book a table")
        else:
            usernumber=tracker.get_slot("number")
            name=DataFetchUsername(usernumber)
            timevar=tracker.get_slot("bttime")
            optime=RFetchOpeningTimeSlot(timevar)
            clstime=RFetchClosingTimeSlot(timevar)
            datevar=tracker.get_slot("btdate")
            restrovar=tracker.get_slot("rname")
            seats=tracker.get_slot("noofpeople")

            ddict={
                "time":timevar,
                "restro":restrovar,
                "usernum":usernumber,
                "date":datevar,
                "nop":seats
            }
          
            BookTable(ddict)
            dispatcher.utter_message(text="{0},I have booked a table for {1} people at {2} restaurant on {3} from {4} - {5} ".format(name,seats,restrovar,datevar,optime,clstime)) 

            UpdateBookingTable(ddict)
        return

# ---------inquire---------------
class ActionRestrodetails(Action):

    def name(self) -> Text:
        return "action_restrodetails"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    	
        restro=tracker.get_slot("rname")
        # # new code
        # testname = RFetchName(restro)
        
        # if testname == None:
        #     dispatcher.utter_message(text="Could not find a restaurant with that name")    
        
        # else:
        # #
        imageurl=RFetchImage(restro)
        dispatcher.utter_message(image=imageurl)

        street=RFetchStreet(restro)
        area=RFetchArea(restro)
        rating=RFetchRating(restro)
        rtype=RFetchRType(restro)
        foodtype=RFetchFoodType(restro)
        cuisines=RFetchCuisine(restro)
        capacity=RFetchCapacity(restro)
        openingtime=RFetchOpeningTime(restro)
        closingtime=RFetchClosingTime(restro)
        
        output="Address : {0},{1} \nRating : {2} \nType : {3} \nFood-type : {4} \nCuisines : {5}\nCapacity : {6} \nOpen From : {7} to {8}\n".format(street,area,rating,rtype,foodtype,cuisines,capacity,openingtime,closingtime) 
        dispatcher.utter_message(text=output)
        return []

########-----CANCEL BOOKING ACTIONS---------------################

#--Show all bookings for a customer
class ActionShowBookimgs(Action):

    def name(self) -> Text:
        return "action_show_bookings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        usernumber=tracker.get_slot("number")
        uid=DataFetchUserId(usernumber)
        
        count=getCount(uid)
        if count == 0:
            dispatcher.utter_message(text="You have no bookings")
            SlotSet("zerobooking","0")
    
        elif count == 1:
            ddict=getBookings(uid)
            bid=ddict["bid"]
            restro=ddict["rname"]
            date=ddict["date"]
            numofpeople=ddict["numofpeople"]
            dispatcher.utter_message(text="You have one booking at {0} restaurant on {1} for {2} people\nBOOKING ID: {3}".format(restro,date,numofpeople,bid))
        else:
            ddict={
                "count":count,
                "userid":uid
            }
            Allbid=getAllBookings(ddict)
            dispatcher.utter_message(text="You have {} bookings".format(count))
            
            for x in range(count) :
                    bookid=Allbid[x][0]
                    restroname =Allbid[x][1]
                    date=Allbid[x][2]
                    dispatcher.utter_message(text="{} restaurant on {}\nBOOKING ID: {}".format(restroname,date,bookid))

#-- bid form
class ValidateBid(Action):

    def name(self) -> Text:
        return "bid_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict) -> List[EventType]:

        if tracker.get_slot("zerobooking") == "0" :
            return [SlotSet("requested_slot", -1)]

        if tracker.slots.get(bid) is None:
            #for an empty slot, request user to fill it
            return [SlotSet("requested_slot", bid)]
 
        #when all required slots are filled
        return [SlotSet("requested_slot", None)]

# -- validate bid
class ValidateBidForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_bid_form"

    def validate_bid(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate bid value."""

        usernumber=tracker.get_slot("number")
        uid=DataFetchUserId(usernumber)
        bid=slot_value
        ddict={
            "uid":uid,
            "bid":bid
        }
        
        count=getCount(uid)
        if count == 0:
            return {"bid": -1}
        # If bid doesnot belong to the given user 
        if BcheckBid(ddict) is None :
            dispatcher.utter_message(text="Enter a valid booking id from those shown above to cancel a booking")
            return {"bid": None}

        else:
            return {"bid": slot_value}

#--Submit form and cancel a booking
class ActionSubmitBidForm(Action):

    def name(self) -> Text:
        return "action_submit_bidform"

    def run(self, dispatcher,
            tracker: Tracker,
            domain: "DomainDict",) -> List[Dict[Text, Any]]:

        bookid=tracker.get_slot("bid")
        print("print from action_submit_bidform")
        if bookid == -1 :
            return
        cancelBooking(bookid)
        dispatcher.utter_message(text="Your booking has been cancelled")
        return

# class ActionUpdateData(Action):

#     def name(self) -> Text:
#         return "action_update_data"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         username=tracker.get_slot("uname")
#         usernumber=tracker.get_slot("number")

#         DataUpdateUser(username,usernumber)
        
#         return[]

# class ActionCheckNumber(Action):

#     def name(self) -> Text:
#         return "action_check_number"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         usernumber=tracker.get_slot("number")

#         name=DataFetchUsername(usernumber)

#         output="Welcome back {} !".format(name)

#         dispatcher.utter_message(text=output)

#         return[]
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#