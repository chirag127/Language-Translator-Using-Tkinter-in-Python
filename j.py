import tkinter as tk
import sys

class PrintLogger(): # create file like object
    def __init__(self, textbox): # pass reference to text widget
        self.textbox = textbox # keep ref

    def write(self, text):
        self.textbox.insert(tk.END, text) # write text to textbox
            # could also scroll to end of textbox here to make sure always visible

    def flush(self): # needed for file like object
        pass

if __name__ == '__main__':

    while True:
        try:
            
            def do_something():
                print('i did something')
                # root.after(1000, do_something)

            print("qiaulfskhdnliukf")

            root = tk.Tk()
            t = tk.Text()
            t.pack()
            # create instance of file like object
            pl = PrintLogger(t)

            # replace sys.stdout with our object
            sys.stdout = pl

            # now we can print to stdout or file
            print('hello world')
            print('hello world')


            root.mainloop()

        except:
            print("exception")
