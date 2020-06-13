#!/usr/bin/env python3

import wx


class CalcExample(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id,
                          'wxWidget Calculator Example',  # Window title
                          size=(400, 400))  # original size of window.
        panel = wx.Panel(self)
        grid_bag = wx.GridBagSizer()

        self.calc_display = wx.StaticText(panel, label='')
        grid_bag.Add(self.calc_display, pos=(0, 0), span=(1, 3),
                     flag=wx.ALIGN_LEFT | wx.EXPAND | wx.ALL, border=5)
        digit_start = 1
        one = wx.Button(self, label='1')
        grid_bag.Add(one, pos=(digit_start+0, 0), flag=wx.ALL, border=2)
        two = wx.Button(self, label='2')
        grid_bag.Add(two, pos=(digit_start+0, 1), flag=wx.ALL, border=2)
        three = wx.Button(self, label='3')
        grid_bag.Add(three, pos=(digit_start+0, 2), flag=wx.ALL, border=2)
        four = wx.Button(self, label='4')
        grid_bag.Add(four, pos=(digit_start+1, 0), flag=wx.ALL, border=2)
        five = wx.Button(self, label='5')
        grid_bag.Add(five, pos=(digit_start+1, 1), flag=wx.ALL, border=2)
        six = wx.Button(self, label='6')
        grid_bag.Add(six, pos=(digit_start+1, 2), flag=wx.ALL, border=2)
        seven = wx.Button(self, label='7')
        grid_bag.Add(seven, pos=(digit_start+2, 0), flag=wx.ALL, border=2)
        eight = wx.Button(self, label='8')
        grid_bag.Add(eight, pos=(digit_start+2, 1), flag=wx.ALL, border=2)
        nine = wx.Button(self, label='9')
        grid_bag.Add(nine, pos=(digit_start+2, 2), flag=wx.ALL, border=2)

        zero = wx.Button(self, label='0')
        grid_bag.Add(zero, pos=(digit_start+3, 1), flag=wx.ALL, border=2)

        digit_btns = [one, two, three, four, five, six,
                      seven, eight, nine, zero]
        for btn in digit_btns:
            btn.Bind(wx.EVT_BUTTON, self.digit_click)

        add = wx.Button(self, label='+')
        grid_bag.Add(add, pos=(digit_start+0, 3), flag=wx.ALL, border=2)
        sub = wx.Button(self, label='-')
        grid_bag.Add(sub, pos=(digit_start+1, 3), flag=wx.ALL, border=2)
        mul = wx.Button(self, label='*')
        grid_bag.Add(mul, pos=(digit_start+2, 3), flag=wx.ALL, border=2)
        div = wx.Button(self, label='/')
        grid_bag.Add(div, pos=(digit_start+3, 3), flag=wx.ALL, border=2)
        equal = wx.Button(self, label='=')
        grid_bag.Add(equal, pos=(digit_start+4, 3), flag=wx.ALL, border=2)

        op_btns = [add, sub, mul, div, equal]
        for btn in op_btns:
            btn.Bind(wx.EVT_BUTTON, self.op_click)

        clear = wx.Button(self, label='Clear')
        grid_bag.Add(clear, pos=(digit_start+3, 2), flag=wx.ALL, border=2)
        clear.Bind(wx.EVT_BUTTON, self.clear_click)

        status_bar = self.CreateStatusBar()
        self.Bind(wx.EVT_CLOSE, self.close_window)
        panel.SetSizerAndFit(grid_bag)

    def append_display(self, txt):
        orig = self.calc_display.GetLabel()
        new = orig + txt
        self.calc_display.SetLabel(new)
    
    def solve_problem(self):
        eq = self.calc_display.GetLabel()
        ans = eval(eq)
        self.calc_display.SetLabel(f'{ans}')
    
    def clear_click(self, e):
        self.calc_display.SetLabel('')

    def op_click(self, e):
        lbl = e.GetEventObject().GetLabel()
        if (lbl == '='):
            self.solve_problem()
        else:
            self.append_display(lbl)

    def digit_click(self, e):
        lbl = e.GetEventObject().GetLabel()
        self.append_display(lbl)

    def close_window(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = CalcExample(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
