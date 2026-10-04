def get_input():
    userName = input("Name: ")
    return userName

def validate_input(value):
    print(value, " is validated")    

def save_to_db(value):
    print(value ," is Saved to Db!!")


def register_user():
   name =  get_input()
   validate_input(name)
   save_to_db(name)        

register_user()