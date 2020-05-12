#  Author:          Your Name
#  ULID/Section:    Your ULID & Section
#  lab12.py 

class Clock:

   def __init__(self, hrsIn, minsIn, secsIn):
      self.__hours = hrsIn
      self.__minutes = minsIn
      self.__seconds = secsIn


   def SetTime(self, newHrsIn, newMinsIn, newSecsIn):
      # write this class method
      self.__hours = newHrsIn
      self.__minutes = newMinsIn
      self.__seconds = newSecsIn

   def GetHours(self):
      return self.__hours

   def GetMinutes(self):
      # write this class method
      return self.__minutes

   def GetSeconds(self):
      # write this class method
      return self.__seconds


   def DisplayTime24(self):
      print("The time is",format(self.__hours,"2d"),":",end="")
      if (self.__minutes < 10):
         print("0",end="")
         # finish the rest of this class method
         print(self.__minutes,":",end="")
      if (self.__minutes >= 10):
         print(format(self.__minutes,"2d"),":",end="")
      if (self.__seconds < 10):
         print("0",end="")
         print(self.__seconds)
      if (self.__seconds >= 10):
         print(format(self.__seconds,"2d"))
      

   def DisplayTime12(self):
      print("The time is ",end="")

      if (self.__hours < 12) and (self.__hours >= 0):
         # finish the rest of this class method
         if (self.__hours == 0):
            self.__hours = self.__hours + 12
            print(format(self.__hours,"2d"),":",end="")
            self.__hours = self.__hours - 12
         else:
            print(format(self.__hours,"2d"),":",end="")
            
         if (self.__minutes < 10):
            print("0",end="")
            print(self.__minutes,":",end="")
         if (self.__minutes >= 10):
            print(format(self.__minutes,"2d"),":",end="")
         if (self.__seconds < 10):
            print("0",end="")
            print(self.__seconds," AM")
         if (self.__seconds >= 10):
            print(format(self.__seconds,"2d")," AM")
      else:
         if (self.__hours == 12):
            print(format(self.__hours,"2d"),":",end="")
         else:
            self.__hours = self.__hours - 12
            print(format(self.__hours,"2d"),":",end="")
            self.__hours = self.__hours + 12

         if (self.__minutes < 10):
            print("0",end="")
            print(self.__minutes,":",end="")
         if (self.__minutes >= 10):
            print(format(self.__minutes,"2d"),":",end="")
         if (self.__seconds < 10):
            print("0",end="")
            print(self.__seconds," PM")
         if (self.__seconds >= 10):
            print(format(self.__seconds,"2d")," PM")
         

   def IncrementClock(self):
      self.__seconds = self.__seconds + 1
      if (self.__seconds == 60):
         self.__seconds = 0
         self.__minutes = self.__minutes + 1
         # finish the rest of this class method
      if (self.__minutes == 60):
         self.__minutes = 0
         self.__seconds = 0
         self.__hours = self.__hours + 1



def main():
   myClock = Clock(0,0,0)     # create a clock with a time of midnight
   myClock.DisplayTime12()    # display it with a 12-hour format
   myClock.DisplayTime24()    # display it with a 24-hour format
   print()

   myClock.SetTime(22,30,5)   # change the time to 10:30:05 PM
   myClock.DisplayTime12()    # display it with a 12-hour format
   myClock.DisplayTime24()    # display it with a 24-hour format
   print()

   myClock.SetTime(11,59,59)  # change the time to 11:59:59 AM
   myClock.DisplayTime12()    # display it with a 12-hour format
   myClock.DisplayTime24()    # display it with a 24-hour format
   print()

   myClock.IncrementClock()   # increment the clock (make time pass) by 1 second
   myClock.DisplayTime12()    # display new/current time in 12-hour format
   myClock.DisplayTime24()    # display new/current time in 24-hour format
   print()


main()
