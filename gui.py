import wx
import os

class MainWindow(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainWindow, self).__init__(*args, **kw)

        self.makeMenuBar()
        self.CreateStatusBar()
                
    
    def makeMenuBar(self):
        # Make a file menu
        fileMenu = wx.Menu()
        openItem = fileMenu.Append(-1, "&Open File...\tCtrl-O",
                    "Open a file from existing file system.")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)
        
        # Make a help menu
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)
        
        # Make the menu bar and set to frame
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)
        
        # Associate hander to each menu items
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.OnOpen, openItem)


    def OnExit(self, _event):
        self.Close(True)


    def OnAbout(self, _event):
        wx.MessageBox("This is a application for extracting characteristic parameters from Sonnet simulation result.",
                      "About EPX", wx.OK | wx.ICON_INFORMATION)

    def OnOpen(self, _event):
        file_wildcard = "CSV files(*.csv)|*.csv|All files(*.*)|*.*"
        dlg = wx.FileDialog(self, "Open CSV file...",
                            os.getcwd(),
                            wildcard=file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            self.importFile(filename)
        dlg.Destroy()
    
    
    def importFile(self, filename):
        print(filename)


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainWindow(None, title="Extraction")
        self.frame.Show(show=True)
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
