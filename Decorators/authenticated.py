# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  # code here
    def wrap_func(user):
        if user['valid']:
           fn(user)
        else: print('User is not authenticated, message not sent!')
 
    return wrap_func

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)