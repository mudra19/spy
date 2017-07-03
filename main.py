#to print in different colors

from colorama import Fore


from spy_details import spy,Spy,ChatMessage,friends

#import library for encoding and decoding data

from steganography.steganography import Steganography

#import library to get information about time and period

from datetime import datetime

#store status messages for  the user in the list
STATUS_MESSAGES=['sharing is caring','less is more','ability without honor is useless','be courageous to act and leave the talking to others']

print "hello"

#backlash or escaping character

print 'let\'s get started'

#function to send encrypted message to friend


def send_message():
    #call the fuction select_friend which returns the position of friend whom we want to send the message
    #store it in a variable friend_choise

    friend_choise=select_friend()
    #input original image upon which text will be encoded

    original_img=raw_input('What is the name of the image')

    #save the path of the ouput image which will carry our message in output_path variable
    output_path='output.jpg'

    #input and store secret message in variable text

    text=raw_input('What do you want to say?')

    #original img is the carrier and output path has hidden text in it


    Steganography.encode(original_img,output_path,text)
    #save the secret message alongwith the time at which it was send using class ChatMessage


    new_chat=ChatMessage(text,True)

    #append the message to the friend's chat instance

    friends[friend_choise].chats.append(new_chat)

    print 'you secret message image is ready'

#read encrypted message from a friend

def read_message():

    #call function select_friend to get index of the friend whose message is to be read

    sender=select_friend()

    #output_path has the image which is to be decoded

    output_path=raw_input('what is the name of the file')

    #decode and save secret message in a variable secret_text

    secret_text=Steganography.decode(output_path)
    #save the secret message that we decoded using class ChatMessage alongwith current timestamp


    new_chat=ChatMessage(secret_text,False)

    #append the message recieved from the friend in chat instance

    friends[sender].chats.append(new_chat)

    print 'your message has been saved'


#function to read chat history


def read_chat_history():


    #get index of a friend whose chat history is to be read
    read_for=select_friend()




    #find the index of selected friend in the list

    for chat in friends[read_for].chats:
        # check if the message is send

        if chat.sent_by_me:
            print(Fore.BLUE + chat.time.strftime('%d %B %Y') +'you said'+ Fore.BLACK + chat.message)

        else:

            print(Fore.BLUE + chat.time.strftime('%d %B %Y') + Fore.RED + friends[read_for].name + Fore.BLACK + chat.message)




        #or the message is recieved













#make a function for adding status message


def add_status(current_status_message):

    #initially no status is updated
    updated_status_message=None

    #check if status is updated

    if spy.current_status_message !=None:


        print'your current status message is '+spy.current_status_message+'\n'

    else:

        print 'you dont have any status message currently \n'


    status=raw_input('Do you want to select from the older status (y/n)? ')

    #if answer is no
    if status.upper()=='N':

        new_status_message=raw_input('what status message do you want to set?')

        #check if the status message is valid one

        if len(new_status_message)>0:

            updated_status_message=new_status_message

            STATUS_MESSAGES.append(new_status_message)
     #if answer is yes

    elif status.upper()=='Y':

        pos=1
        #print all the status messages

        for message in STATUS_MESSAGES:
            print str(pos)+ '.'+ str(message)
            pos=pos+1
        #ask the user to select from the displayed status message


        message_selection=int(raw_input('choose from the above messages' ))

        #if the user has entered the choise from within the list
        if len(STATUS_MESSAGES)>=message_selection:

            #update the status message
            updated_status_message=STATUS_MESSAGES[message_selection-1]

    else:

        print' The option you choosed is not valid.press y or n'


    if updated_status_message:


        print 'your updated status message is %s'%(updated_status_message)
    else:

        print 'you did not update your status message'
        #return the updated message
    return updated_status_message

#make a function to add spy's friend
def add_friend():

    # class object new friend is initialised

    new_friend=Spy('','',0,0.0)
    #get details of friend and save them in class variables

    new_friend.name=raw_input("please add your friend's name: ")

    new_friend.salutation=raw_input('Mr or Ms? :')

    new_friend.name=new_friend.salutation+' '+new_friend.name

    new_friend.age=int(raw_input('Age?:'))

    new_friend.rating=float(raw_input('Rating of spy?:'))

    if len(new_friend.name)>0 and new_friend.age>12 and  new_friend.rating>=spy.rating:


        friends.append(new_friend)

        print 'friend added!!'

    else:

        print 'sorry we can\'t add spy with the details you provided'

    return len(friends)

#function to select friend to whom message is to be send
def select_friend():

    num=0
#Print out all the friends of the user

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (num + 1, friend.salutation, friend.name,friend.age,friend.rating)



        num = num +1
        #Ask the user to select from one of the friends

    friends_choise=raw_input('Choose from your friends')

    friend_choise_pos=int(friends_choise)-1

    # Return the index of the selected friend in the friends list
    return friend_choise_pos



#make a fuction for chat menu

def start_chat(spy):

    current_status_message= None

    spy.name=spy.salutation+ ' '+spy.name


    if spy.age>12 and spy.age<50:

        print'Authentication complete.welcome ' + str(spy.name) + ' age: ' + str(spy.age) + ' and rating of:'+ str(spy.rating) +' proud to have you on board'

    #now we will create a list called show menu which will give user different options to work on
        show_menu=True

        #run the loop untill the showmenu is false ie the user chooses to exit application
        while(show_menu):

            choise='what do you want to do? \n 1.Add a status update\n 2.Add a friend\n 3.read a secret message \n4.send a secret message\n  5.read chats from a user\n 6.close application '

            menu_choise=raw_input(choise)

            if len(menu_choise)>0:

                menu_choise=int(menu_choise)

                if menu_choise==1:

                    print 'you choose to update the status'
                    #call the function add_status
                    current_status_message=add_status(current_status_message)

                elif menu_choise==2:
                    #call the function add_friend
                    num_of_friends=add_friend()

                    print 'you have %d friends'%(num_of_friends)

                elif menu_choise==3:
                    #call function read_message

                    read_message()

                elif menu_choise==4:
                    #call function send_message

                    send_message()

                elif menu_choise==5:
                    #call function read_chat_history

                    read_chat_history()

                else:
                    show_menu=False

    else:
        print 'sorry you are not of correct age to be a spy'

    #ask user if he wants to add new identity or continue with the default one

existing = raw_input('Do you want to continue as ' + str(spy.salutation) + ' ' + str(spy.name) + ' (Y/N)? ')
#if the user wants to continue with default values then directly call start chat function

if existing.upper()=='Y':

    start_chat(spy)

else:

    #create class object spy

    spy=Spy('','',0,0.0)

#taking input from user
#ask user details

    spy.name=raw_input("welcome to spy chat.let me know your good name?")

    #check if the user has entered a valid name

    if len(spy.name)<0 and spy.name.isspace():

        print "A spy needs to have a valid name.try again please...."

    else:

        spy.salutation=raw_input("what should we call you(Mr or Ms?)")

        spy.name=spy.salutation + " " +spy.name

        print "Alright " + spy.name + ". I'd like to know a little bit more about you before we proceed..."

#get information regarding age,rating and online status from the user




        spy.age=int(raw_input('enter your age: '))

#check if the age is appropriate

        if spy.age>12 and spy.age<50:

#take spy rating as an input from user otherwise print else statement

            spy.rating=float(raw_input('Enter your rating: '))

#according to spy rating analyse the nature of spy

            if spy.rating>=4.5:
                print 'You are an ace!'

            elif  spy.rating<4.5 and spy.rating>=3.5:
                print 'You are one of the good ones'

            elif spy.rating>=2.5 and spy.rating<3.5:
                print 'you can always do better'

            else:
                print 'we can always use somebody to help in the office'

         # let's make this spy come online

            spy.is_online = True



            #calling fuction start chat
            start_chat(spy)


        else:
            print 'you are not of correct age to be a spy'



