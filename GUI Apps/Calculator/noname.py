# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 537,356 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer1 = wx.FlexGridSizer( 7, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )

		self.button0 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.button0, 0, wx.ALL, 5 )

		self.button1 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.button1, 0, wx.ALL, 5 )

		self.button2 = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.button2, 0, wx.ALL, 5 )

		self.button3 = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.button3, 0, wx.ALL, 5 )

		self.button4 = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.button4, 0, wx.ALL, 5 )

		self.button5 = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.button5, 0, wx.ALL, 5 )

		self.button6 = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.button6, 0, wx.ALL, 5 )

		self.button7 = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.button7, 0, wx.ALL, 5 )

		self.button8 = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.button8, 0, wx.ALL, 5 )


		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.button9 = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.button9, 0, wx.ALL, 5 )


		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.operationtxt = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.operationtxt.Wrap( -1 )

		fgSizer1.Add( self.operationtxt, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button0.Bind( wx.EVT_BUTTON, self.zero )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def zero( self, event ):
		event.Skip()


