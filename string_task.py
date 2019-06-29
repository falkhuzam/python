Number=input("Number: ")
time= "It was " + Number + " o'clock when I hears a knock at the door.\n"
Item= input("Item:")
Name=input("Name:")
ItemName="I opened the door and there was a box full of %s with a note saying \"From Mr.%s\" \n"%(Item, Name.title())
Scream= input("Scream Something:")
ScreamScene= "Just as I closed the door I heard a scream \"" + Scream.upper() + ".\".\n"
Action=input("Action:")
ActionDecision= "I froze in place and all I could do was" + Action + "."


print ("%s%s%s%s" % (time,ItemName,ScreamScene,ActionDecision))

