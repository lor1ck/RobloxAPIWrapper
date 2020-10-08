import requests


def getUserFollowers(id): return requests.get("https://friends.roblox.com/v1/users/" + str(id) + "/followers").text
def getUserFriends(id): return requests.get("https://friends.roblox.com/v1/users/" + str(id) + "/friends").text
def getUserFriendsCount(id): return requests.get("https://friends.roblox.com/v1/users/" + str(id) + "/friends/count").text
def getUserFriendsOnline(id): return requests.get("https://friends.roblox.com/v1/users/" + str(id) + "/friends/online").text



def friendRequestsDeclineAll(): return requests.post("https://friends.roblox.com/v1/user/friend-requests/decline-all")
def friendRequestAccept(id): return requests.post("https://friends.roblox.com/v1/users/" + str(id) + "/friend-requests/accept-friend-request")
def friendRequestDecline(id): return requests.post("https://friends.roblox.com/v1/users/" + str(id) + "/friend-requests/decline-friend-request")
def friendUserUnfriend(id): return requests.post("https://friends.roblox.com/v1/users/" + str(id) + "/unfriend")

def userFollow(id): return requests.post("https://friends.roblox.com/v1/users/" + str(id) + "/follow")
def userUnFollow(id): return requests.post("https://friends.roblox.com/v1/users/" + str(id) + "/unfollow")
