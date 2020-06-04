import sys
import requests

print("[1] python version: {}".format(sys.version))
print("[2] python executable: {}".format(sys.executable))


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("world"))
print(greet("cwb4"))
r = requests.get("https://coreyms.com")
print("[3] status code: {}".format(r.status_code))

# name = input("Enter Name: ")
# print("Output: ", name)
