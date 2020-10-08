import wrapper

UID = input("Enter UID: ")  # getting user id

getFriends = wrapper.getUserFriends(UID)  # calling getUserFriends function


getFriendsCount = wrapper.getUserFriendsCount(UID) # calling getUserFriendsCount function

print(getFriends + "\n" + getFriendsCount)  # printing friends and friends count