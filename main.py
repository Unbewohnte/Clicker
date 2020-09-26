import pynput,sys,random,time,pyautogui
from pynput import mouse,keyboard
import tkinter as tk

def main():
    mouse_c = mouse.Controller()
    keyboard_c = keyboard.Controller()


    ######### GUI
    def GUI():
        window = tk.Tk()
        window.title('Clicker')
        window.geometry(("700x300"))
        window.minsize(700,320)
        window.maxsize(700,320)
        canvas = tk.Canvas(window,width = 700,height = 320, bg = '#e3e1e8')
        canvas.pack()
        #
        global mouse_pos_label
        mouse_pos_label = tk.Label(window,text = mouse_c.position)
        mouse_pos_label.after(100,update_mouse_pos)
        mouse_pos_label.place(x = 400,y = 300, width = 100, height = 20)
        #
        window.mainloop()


    ### FUNC
    def update_mouse_pos():
        mouse_pos_label.config(text = mouse_c.position)
        mouse_pos_label.after(100,update_mouse_pos)
        pass

    ###

    GUI()
    pass
    #########



if __name__ == "__main__":
    main()
