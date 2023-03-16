# === PROBLEM 2 ===
# ~ Scenario ~
# You are a software engineer at the Pentagon, and your task
# is to write a script for the president that will verify their
# username and password. Below is an incomplete attempt at the
# task, left behind by an intern that was fired. You may use it
# as a starting point or choose to start from scratch.
#
# ~ Success Criteria ~
# The script will prompt the user for their username and password.
# Determine if the username and password combination is valid.
# If invalid, inform the user that they will be drone-striked.
# If valid, tell the user that they've been verified.
#
# Here are valid credentials (DO NOT ACCEPT ANYTHING ELSE):
#   obama  => bomb_Civilians1234
#   donald => MagaMagaMagaMaga
#   joeB   => cornball!
#   
#
# ~ Example ~
# Scenario 1
#   Inputs:
#     Username: obama
#     Password: bomb_Civilians1234
#   Output:
#     You have been verified.
# Scenario 2
#   Inputs:
#     Username: obama
#     Password: cornball!
#   Output:
#     Unable to verify credentials. You will be drone-stiked.

database = {
    "obama":"bomb_Civilians1234",
    "donald":"MagaMagaMagaMaga",
    "joeB":"cornball!"
}

username = input("Username: ")
password = input("Password: ")

if database.get(username) == password:
    print("You have been verified")
else:
    print("Unable to verify credentials. You will be drone-stiked.")
