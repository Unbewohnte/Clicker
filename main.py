import pynput,sys,random,time,pyautogui
from pynput import mouse,keyboard
#import tkinter.font as font
import tkinter as tk

def main():
    mouse_c = mouse.Controller()
    keyboard_c = keyboard.Controller()

    def GUI():
        BACK_CLR = '#e3e1e8'

        window = tk.Tk()
        window.title('Clicker')
        window.geometry(("700x300"))
        window.minsize(700,320)
        window.maxsize(700,320)
        canvas = tk.Canvas(window,width = 700,height = 320, bg = BACK_CLR)
        canvas.pack()
        #
        global mouse_pos_label
        mouse_pos_label = tk.Label(window,text = mouse_c.position,font = 24)
        mouse_pos_label.after(100,update_mouse_pos)
        mouse_pos_label.place(x = 400,y = 300, width = 100, height = 20)
        #
        time_btwn_clcks = tk.Scale(window, orient = "horizontal", length = 30, from_ = 0.05, bg = BACK_CLR, font = 20)
        time_btwn_clcks.place(x = 370,y = 40,width = 160)
        #
        start_bttn = tk.Button(window,text = "Start", command = start_cmmnd,bg = BACK_CLR, font = 20)
        #start_bttn.config(command = start_cmmnd)
        start_bttn.place(x = 0, y = 270, width = 60, height = 50)
        #
        window.mainloop()


    ### FUNC
    def update_mouse_pos():
        mouse_pos_label.config(text = mouse_c.position)
        mouse_pos_label.after(100,update_mouse_pos)
        pass

    def start_cmmnd():
        pass

    ###

    GUI()
    pass




if __name__ == "__main__":
    main()
