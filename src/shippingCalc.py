import wx

class Calc(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title='Shipping Calculator', pos=wx.DefaultPosition, size=wx.DefaultSize):

        super(Calc, self).__init__(parent, id, title, pos, size=(600, 600))

        self.panel = wx.Panel(self)

        self.txt_input0 = wx.TextCtrl(self.panel, pos=(100, 20), size=(220, 22))

        self.txt_input1 = wx.TextCtrl(self.panel, pos=(100, 60), size=(330, 22))

        self.txt_input2 = wx.TextCtrl(self.panel, pos=(100, 100), size=(280, 22))

        self.lbl0 = wx.StaticText(self.panel, label="Name", pos=(330, 24))

        self.lbl1 = wx.StaticText(self.panel, label="Address", pos=(440, 66))

        self.lbl2 = wx.StaticText(self.panel, label="City, State, Zip Code", pos=(390, 100))

        self.lbl3 = wx.StaticText(self.panel, label="Weight",pos=(40, 150))

        self.lbl4 = wx.StaticText(self.panel, label="Speed", pos=(200, 150))

        self.lbl5 = wx.StaticText(self.panel, label="Options", pos=(345, 150))

        self.Radio0 = wx.RadioButton(self.panel, label="0 - 1.9 lbs. $5",style = wx.RB_GROUP, pos=(40, 180))

        self.Radio1 = wx.RadioButton(self.panel, label="2 - 4.9 lbs. $8", pos=(40, 200))

        self.Radio2 = wx.RadioButton(self.panel, label="5 - 10 lbs. $12.25", pos=(40, 220))

        self.Radio3 = wx.RadioButton(self.panel, label="overland $2.75", style = wx.RB_GROUP, pos=(200, 180))

        self.Radio4 = wx.RadioButton(self.panel, label="3-day air $6.15", pos=(200, 200))

        self.Radio5 = wx.RadioButton(self.panel, label="2-day air $10.80", pos=(200, 220))

        self.Radio6 = wx.RadioButton(self.panel, label="overnight $15.25", pos=(200, 240))

        self.cb0 = wx.CheckBox(self.panel, label="Extra padding. $5", pos=(350, 180))

        self.cb1 = wx.CheckBox(self.panel, label="Gift wrapping. $8", pos=(350, 200))

        self.btn_enter = wx.Button(self.panel, label="Calculate Total", pos=(160, 320))

        self.btn_clear = wx.Button(self.panel, label="Clear Form", pos=(300, 320))

        self.lbl5 = wx.StaticText(self.panel, label="Shipping Summary", pos=(220, 380))

        self.btn_enter.Bind(wx.EVT_BUTTON, self.calcTotal)

        self.btn_clear.Bind(wx.EVT_BUTTON, self.clearForm)

        self.Line0 = wx.StaticText(self.panel, id = -1, pos=(220, 430), label="", )

        self.Line1 = wx.StaticText(self.panel, id = -1, pos=(220, 450), label="")

        self.Line2 = wx.StaticText(self.panel, id = -1, pos=(220, 470), label="")

        self.Line3 = wx.StaticText(self.panel, id = -1, pos=(220, 490), label="")



    def calcTotal(self, event):

        cost = 0

        if self.Radio0.GetValue() and self.Radio3.GetValue():

            cost = "$7.75"

            if self.cb0.GetValue():

                cost = "$12.75"

            if self.cb1.GetValue():

                cost = "$15.75"

            if self.cb0.GetValue() and self.cb1.GetValue():

                cost = "$20.75"

        if self.Radio0.GetValue() and self.Radio4.GetValue():

            cost = "$11.15"

            if self.cb0.GetValue():

                cost = "$16.15"

            if self.cb1.GetValue():

                cost = "$19.15"

            if self.cb0.GetValue() and self.cb1.GetValue():

                cost = "$24.15"

        if self.Radio0.GetValue() and self.Radio5.GetValue():

            cost = "$15.80"

            if self.cb0.GetValue():

                cost = "$20.80"

            if self.cb1.GetValue():

                cost = "$23.80"

            if self.cb0.GetValue() and self.cb1.GetValue():

                cost = "$28.80"


        if self.Radio0.GetValue() and self.Radio6.GetValue():

            cost = "$20.25"

            if self.cb0.GetValue():

                cost = "$25.25"

            if self.cb1.GetValue():

                cost = "$28.25"

            if self.cb0.GetValue() and self.cb1.GetValue():

                cost = "$33.25"

        if self.Radio1.GetValue() and self.Radio3.GetValue():

            cost = "$10.75"

            if self.cb0.GetValue():

                cost = "$15.75"

            if self.cb1.GetValue():

                cost = "$18.75"

            if self.cb0.GetValue() and self.cb1.GetValue():

                cost = "$23.75"

        if self.Radio1.GetValue() and self.Radio4.GetValue():

            cost = "$14.15"

            if self.cb0.GetValue():

                cost = "$19.15"

            if self.cb1.GetValue():

                cost = "$22.15"

            if self.cb0.GetValue() and self.cb1.GetValue():

                cost = "$27.15"

        if self.Radio1.GetValue() and self.Radio5.GetValue():

            cost = "$18.80"

            if self.cb0.GetValue():

                cost = "$23.80"

            if self.cb1.GetValue():

                cost = "$26.80"

            if self.cb0.GetValue() and self.cb1.GetValue():

                cost = "$31.80"


        if self.Radio1.GetValue() and self.Radio6.GetValue():

            cost = "$23.25"

            if self.cb0.GetValue():

                cost = "$28.25"

            if self.cb1.GetValue():

                cost = "$31.25"

            if self.cb0.GetValue() and self.cb1.GetValue():

                cost = "$36.25"

        if self.Radio2.GetValue() and self.Radio3.GetValue():

            cost = "$15.00"

            if self.cb0.GetValue():

                cost = "$18.00"

            if self.cb1.GetValue():

               cost = "$21.00"

            if self.cb0.GetValue() and self.cb1.GetValue():

                cost = "$26.00"

        if self.Radio2.GetValue() and self.Radio4.GetValue():

            cost = "$18.40"

            if self.cb0.GetValue():

                cost = "$23.40"

            if self.cb1.GetValue():

                cost = "$26.40"

            if self.cb0.GetValue() and self.cb1.GetValue():

                cost = "$31.40"


        if self.Radio2.GetValue() and self.Radio5.GetValue():

            cost = "$23.05"

            if self.cb0.GetValue():

                cost = "$28.05"

            if self.cb1.GetValue():

               cost = "$31.05"

            if self.cb0.GetValue() and self.cb1.GetValue():

                cost = "$36.05"

        if self.Radio2.GetValue() and self.Radio6.GetValue():

            cost = "$27.50"

            if self.cb0.GetValue():

                cost = "$32.50"

            if self.cb1.GetValue():

                cost = "$35.50"

            if self.cb0.GetValue() and self.cb1.GetValue():

                cost = "$40.50"

        data0 = self.txt_input0.GetValue()

        data1 = self.txt_input1.GetValue()

        data2 = self.txt_input2.GetValue()

        data3 = cost

        self.Line0.SetLabel(data0)

        self.Line1.SetLabel(data1)

        self.Line2.SetLabel(data2)

        self.Line3.SetLabel(data3)

    def clearForm(self, event):

        self.txt_input0.SetValue("")

        self.txt_input1.SetValue("")

        self.txt_input2.SetValue("")

        self.Radio0.SetValue(1)

        self.Radio1.SetValue(0)

        self.Radio2.SetValue(0)

        self.Radio3.SetValue(1)

        self.Radio4.SetValue(0)

        self.Radio5.SetValue(0)

        self.Radio6.SetValue(0)

        self.cb0.SetValue(0)

        self.cb1.SetValue(0)

        clsData = ""

        self.Line0.SetLabel(clsData)

        self.Line1.SetLabel(clsData)

        self.Line2.SetLabel(clsData)

        self.Line3.SetLabel(clsData)

if __name__ == "__main__":

    app = wx.App()

    fr = Calc(None, -1)

    fr.Show()

    app.MainLoop()
