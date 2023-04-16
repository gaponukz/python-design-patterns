import abc
import typing

Request: typing.TypeAlias = dict[str, typing.Any]

class IHandler(abc.ABC):
    @abc.abstractmethod
    def handle_request(self, request: Request) -> bool: ...

class AuthHandlerBase(IHandler):
    def __init__(self, successor: IHandler | None = None):
        self._successor = successor

class UsernamePasswordAuthHandler(AuthHandlerBase):
    def handle_request(self, request: Request) -> bool:
        if 'username' in request and 'password' in request:
            return request['username'] == 'admin' and request['password'] == 'password123'
            
        if self._successor:
            return self._successor.handle_request(request)
        
        return False

class TokenAuthHandler(AuthHandlerBase):
    def handle_request(self, request: Request) -> bool:
        if 'token' in request:
            return request['token'] == 'abcdef1234567890'
            
        if self._successor:
            return self._successor.handle_request(request)
        
        return False

class EmailPasswordAuthHandler(AuthHandlerBase):
    def handle_request(self, request: Request) -> bool:
        if 'email' in request and 'password' in request:
            return request['email'] == 'admin@example.com' and request['password'] == 'password123'
        
        if self._successor:
            return self._successor.handle_request(request)
        
        return False

class AuthSystem:
    def __init__(self):
        self._handler_chain = EmailPasswordAuthHandler(UsernamePasswordAuthHandler(TokenAuthHandler()))

    def authenticate(self, request: Request) -> bool:
        return self._handler_chain.handle_request(request)

if __name__ == '__main__':
    auth_system = AuthSystem()

    request = {'username': 'admin', 'password': 'password123'}
    result = auth_system.authenticate(request)
    print(result)  # Output: True

    request = {'token': 'abcdef1234567890'}
    result = auth_system.authenticate(request)
    print(result)  # Output: True

    request = {'username': 'invalid', 'password': 'password123'}
    result = auth_system.authenticate(request)
    print(result)  # Output: False

    request = {'email': 'admin@example.com', 'password': 'password123'}
    result = auth_system.authenticate(request)
    print(result)  # Output: True
