import wx

#import the newly created GUI file
import noname
class CalcFrame(noname.MyFrame1):
   def __init__(self,parent):
      noname.MyFrame1.__init__(self,parent)

   def findSquare(self,event):
       self.notanint.SetLabel("")
       try:
           num = int(self.inputbox.GetValue())
       except:
           self.notanint.SetLabel("What you typed is not an integer")
       self.resultbox.SetValue(str(num*num))

app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)
#start the applications
app.MainLoop()
