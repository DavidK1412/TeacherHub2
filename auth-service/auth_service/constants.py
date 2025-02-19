from enum import Enum

API_VERSION = 'v1'
BASE_API_URL = f'api/{API_VERSION}'

class UserRoles(Enum):
    ADMIN = 'admin'
    USER = 'user'

class RoleDetails(Enum):
    ADMIN = 'Administrator'
    USER = 'Regular User'

class ErrorMessages(Enum):
    INVALID_CREDENTIALS = 'Invalid credentials'
    USER_NOT_FOUND = 'User not found'
    USER_ALREADY_EXISTS = 'User already exists'
    EMAIL_ALREADY_EXISTS = 'Email already exists'
    EMAIL_MUST_BE_SET = 'The Email field must be set'

class ViewsUrls(Enum):
    REGISTER = '/register'
    LOGIN = '/login'
    VERIFY_TOKEN = '/verify-token'

class ViewsNames(Enum):
    REGISTER = 'register'
    LOGIN = 'login'
    VERIFY_TOKEN = 'verify-token'
