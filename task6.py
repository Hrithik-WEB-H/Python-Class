class Student:
  _id = 69
  _name = "Rittik"
  
  def __show(self):
   print("ID:", self._id)
  
class Jafri(Student):
 def ShowDetails(self):
   print("Name:", self._name)
   self.__show()
   
obj = Jafri()
obj.ShowDetails()
