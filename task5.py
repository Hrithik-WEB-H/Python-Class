class Student:
  _id = 69
  _name = "Rittik"
  
  def _show(self):
   print("ID:", self._id)
  
class Jafri(Student):
 def ShowDetails(self):
   print("Name:", self._name)
   self._show()
   
obj = Jafri()
obj.ShowDetails()
