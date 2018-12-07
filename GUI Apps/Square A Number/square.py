import wx

#import the newly created GUI file
import noname
class Calculator(noname.MyFrame1):
   def __init__(self,parent):
      noname.MyFrame1.__init__(self,parent)

   def button0(self,event):
       print("ha")

app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)
#start the applications
app.MainLoop()
