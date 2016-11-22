'''
MicroReg Client library
Allows the python client services to connect with the Registry Server to allow
the registration and other facilities provided through Registry Server.
'''
import xmlrpclib

class MicroRegClient:
    '''
    MicroRegClient defines the methods facilitating the connection with the
    MicroReg Server.
    '''

    def __init__(self,host,port):
        '''
        Setup the connection with the MicroReg server.
        '''

        self.__connection_uri = str(host).rstrip('/') + ":" + str(port)
        self.__client = xmlrpclib.ServerProxy(self.__connection_uri)

    def register(self, name, host, port):
        '''
        Register a new service
        '''

        return self.__client.register(name, host, port)

    def unregister(self, name):
        '''
        Unregister an existing service
        '''

        return self.__client.unregister(name)
