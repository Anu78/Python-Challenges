import wx

#import the newly created GUI file
import noname

numString = ""
class CalcFrame(noname.MyFrame1):
   def __init__(self,parent):
      noname.MyFrame1.__init__(self,parent)

   def button0(self,event):
       numString = numString+"0"

app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)
#start the applications
app.MainLoop()
