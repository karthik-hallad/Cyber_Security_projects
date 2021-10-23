class Authentication(object):
  def __init__(self,passw=" "):
    self.passw=passw
  
  def __lower(self):
    lower = any(i.islower() for i in self.passw)
    return lower

  def __upper(self):
    upper = any(i.isupper() for i in self.passw)
    return upper
  
  def __digit(self):
    digit = any(i.isdigit() for i in self.passw)
    return digit
  
  def validate(self):
    lower = self.__lower()
    upper = self.__upper()
    digit = self.__digit()
    length=len(self.passw) 

    report= lower and upper and digit and length >=6

    if report:
      print("Password is Strong")
      return True

    elif not lower:
      print("Please use at least one lower case character")

    elif not upper:
      print("Please use at least one UPPER case character")
      
    elif length<6:
      print("Please use at least  6 characters")

    elif not digit:
      print("Please use at least one digit")
      
str=input("Enter your password: ")
Authentication(str).validate()