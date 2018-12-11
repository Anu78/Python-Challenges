import wx

#import the newly created GUI file
import noname


class CalcFrame(noname.MyFrame1):
    numString = ""
    def __init__(self,parent):
        noname.MyFrame1.__init__(self,parent)

    def updateText():
        noname.numone.setLabel(numString)

    def zero(self,event):
        numString = ""
        numString = numString + "0"
        CalcFrame.updateText()




app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)
#start the applications
app.MainLoop()
