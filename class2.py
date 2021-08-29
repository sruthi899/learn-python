class justcount:
    __secretcount = 0
    def count(self):
        self.__secretcount += 1
        print(self.__secretcount)
counter = justcount()
counter.count()
print (counter.__justcount__.__secretcount)

class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print (counter.__secretCount)