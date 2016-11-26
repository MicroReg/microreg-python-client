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

    def get_service_details(self, name):
        '''
        Get information about service
        '''

        return self.__client.get_service_details(name)

    def get_all_service_details(self):
        '''
        Get information about all the services
        '''

        return self.__client.get_all_service_details()

    def get_reg_count(self):
        '''
        Get the registration count of services currently registered with the
        server
        '''

        return self.__client.get_reg_count()

    def unregister(self, name):
        '''
        Unregister an existing service
        '''

        return self.__client.unregister(name)
