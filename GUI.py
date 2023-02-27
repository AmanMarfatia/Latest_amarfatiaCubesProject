import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Wufoo Form")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GListBox_649=tk.Listbox(root)
        GListBox_649["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_649["font"] = ft
        GListBox_649["fg"] = "#333333"
        GListBox_649["justify"] = "center"
        GListBox_649.place(x=20,y=30,width=80,height=25)

        GLabel_852=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_852["font"] = ft
        GLabel_852["fg"] = "#333333"
        GLabel_852["justify"] = "center"
        GLabel_852["text"] = "EntryID"
        GLabel_852.place(x=300,y=30,width=70,height=25)

        GLabel_115=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_115["font"] = ft
        GLabel_115["fg"] = "#333333"
        GLabel_115["justify"] = "center"
        GLabel_115["text"] = "Prefix"
        GLabel_115.place(x=440,y=30,width=70,height=25)

        GLabel_897=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_897["font"] = ft
        GLabel_897["fg"] = "#333333"
        GLabel_897["justify"] = "center"
        GLabel_897["text"] = "First Name"
        GLabel_897.place(x=300,y=70,width=70,height=25)

        GLabel_879=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_879["font"] = ft
        GLabel_879["fg"] = "#333333"
        GLabel_879["justify"] = "center"
        GLabel_879["text"] = "Last Name"
        GLabel_879.place(x=450,y=70,width=70,height=25)

        GLabel_765=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_765["font"] = ft
        GLabel_765["fg"] = "#333333"
        GLabel_765["justify"] = "center"
        GLabel_765["text"] = "Logo"
        GLabel_765.place(x=300,y=110,width=70,height=25)

        GLabel_350=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_350["font"] = ft
        GLabel_350["fg"] = "#333333"
        GLabel_350["justify"] = "center"
        GLabel_350["text"] = "Team Name"
        GLabel_350.place(x=310,y=160,width=70,height=25)

        GLabel_982=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_982["font"] = ft
        GLabel_982["fg"] = "#333333"
        GLabel_982["justify"] = "center"
        GLabel_982["text"] = "Email"
        GLabel_982.place(x=300,y=200,width=70,height=25)

        GLabel_663=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_663["font"] = ft
        GLabel_663["fg"] = "#333333"
        GLabel_663["justify"] = "center"
        GLabel_663["text"] = "Jersey Color"
        GLabel_663.place(x=310,y=250,width=70,height=25)

        GLabel_981=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_981["font"] = ft
        GLabel_981["fg"] = "#333333"
        GLabel_981["justify"] = "center"
        GLabel_981["text"] = "Phone Number"
        GLabel_981.place(x=300,y=300,width=94,height=30)

        GCheckBox_511=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_511["font"] = ft
        GCheckBox_511["fg"] = "#333333"
        GCheckBox_511["justify"] = "center"
        GCheckBox_511["text"] = "Coach"
        GCheckBox_511.place(x=450,y=120,width=70,height=25)
        GCheckBox_511["offvalue"] = "0"
        GCheckBox_511["onvalue"] = "1"
        GCheckBox_511["command"] = self.GCheckBox_511_command

        GCheckBox_431=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_431["font"] = ft
        GCheckBox_431["fg"] = "#333333"
        GCheckBox_431["justify"] = "center"
        GCheckBox_431["text"] = "Head Coach"
        GCheckBox_431.place(x=450,y=160,width=85,height=39)
        GCheckBox_431["offvalue"] = "0"
        GCheckBox_431["onvalue"] = "1"
        GCheckBox_431["command"] = self.GCheckBox_431_command

        GCheckBox_29=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_29["font"] = ft
        GCheckBox_29["fg"] = "#333333"
        GCheckBox_29["justify"] = "center"
        GCheckBox_29["text"] = "Waterboys"
        GCheckBox_29.place(x=460,y=200,width=70,height=25)
        GCheckBox_29["offvalue"] = "0"
        GCheckBox_29["onvalue"] = "1"
        GCheckBox_29["command"] = self.GCheckBox_29_command

        GCheckBox_730=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_730["font"] = ft
        GCheckBox_730["fg"] = "#333333"
        GCheckBox_730["justify"] = "center"
        GCheckBox_730["text"] = "Doctor"
        GCheckBox_730.place(x=450,y=240,width=70,height=25)
        GCheckBox_730["offvalue"] = "0"
        GCheckBox_730["onvalue"] = "1"
        GCheckBox_730["command"] = self.GCheckBox_730_command

        GCheckBox_778=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_778["font"] = ft
        GCheckBox_778["fg"] = "#333333"
        GCheckBox_778["justify"] = "center"
        GCheckBox_778["text"] = "18-25"
        GCheckBox_778.place(x=450,y=280,width=70,height=25)
        GCheckBox_778["offvalue"] = "0"
        GCheckBox_778["onvalue"] = "1"
        GCheckBox_778["command"] = self.GCheckBox_778_command

        GCheckBox_295=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_295["font"] = ft
        GCheckBox_295["fg"] = "#333333"
        GCheckBox_295["justify"] = "center"
        GCheckBox_295["text"] = "25-30"
        GCheckBox_295.place(x=450,y=320,width=70,height=25)
        GCheckBox_295["offvalue"] = "0"
        GCheckBox_295["onvalue"] = "1"
        GCheckBox_295["command"] = self.GCheckBox_295_command

        GCheckBox_10=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_10["font"] = ft
        GCheckBox_10["fg"] = "#333333"
        GCheckBox_10["justify"] = "center"
        GCheckBox_10["text"] = "30-40"
        GCheckBox_10.place(x=450,y=360,width=70,height=25)
        GCheckBox_10["offvalue"] = "0"
        GCheckBox_10["onvalue"] = "1"
        GCheckBox_10["command"] = self.GCheckBox_10_command

        GListBox_182=tk.Listbox(root)
        GListBox_182["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_182["font"] = ft
        GListBox_182["fg"] = "#333333"
        GListBox_182["justify"] = "center"
        GListBox_182.place(x=20,y=90,width=80,height=25)

        GCheckBox_554=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_554["font"] = ft
        GCheckBox_554["fg"] = "#333333"
        GCheckBox_554["justify"] = "center"
        GCheckBox_554["text"] = "40-50"
        GCheckBox_554.place(x=450,y=390,width=70,height=25)
        GCheckBox_554["offvalue"] = "0"
        GCheckBox_554["onvalue"] = "1"
        GCheckBox_554["command"] = self.GCheckBox_554_command

    def GCheckBox_511_command(self):
        print("command")


    def GCheckBox_431_command(self):
        print("command")


    def GCheckBox_29_command(self):
        print("command")


    def GCheckBox_730_command(self):
        print("command")


    def GCheckBox_778_command(self):
        print("command")


    def GCheckBox_295_command(self):
        print("command")


    def GCheckBox_10_command(self):
        print("command")


    def GCheckBox_554_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()