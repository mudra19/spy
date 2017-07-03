from datetime import datetime
#create a class spy to store the details of spy

class Spy:

    #The function__init__() is a constructor to build the class


    def __init__(self,name,salutation,age,rating):
        # self plays the role of a pronoun for a class object name,salutation,age and rating
        self.name=name
        self.salutation=salutation
        self.age=age
        self.rating=rating
        self.is_online=True
        self.chats=[]
        self.current_status_message=None


#create class ChatMessage to save send and recieved messages seperately
class ChatMessage:
    def __init__(self,message,sent_by_me):
        #print appropriate message if these words are there included in message

        words=['sos','save me','help','danger']

        self.message=message



        #if message is send then the value of sent_by_me will be true otherwise false if it is recieved

        self.sent_by_me=sent_by_me

        #The datetime module provides classes for manipulating dates and times.
        self.time=datetime.now()
        if any(i in message for i in words):
            print "It's urgent!!!!"

#create class object spy to store default values of spy
spy=Spy('Mudra','Ms',21,3.0)


#create class objects of friends to store the details of friends

friend1=Spy('Harman','Ms',21,3.2)
friend2=Spy('Surbhi','Ms',20,3.5)
friend3=Spy('ankita','Ms',20,3.7)
friend4=Spy('jammy','Mr',21,2.5)

#create a list of friends
friends=[friend1,friend2,friend3,friend4]


