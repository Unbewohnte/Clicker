import pynput,sys,time
from pynput import mouse
import tkinter as tk

def main():
    mouse_c = mouse.Controller()


    def GUI():
        global BACK_CLR
        BACK_CLR = '#e3e1e8'

        global window
        window = tk.Tk()
        window.title('Clicker')
        window.geometry(("500x200"))
        window.minsize(500,200)
        window.maxsize(500,200)
        try:
            img = tk.PhotoImage(file = 'icon.png')
            window.tk.call('wm','iconphoto', window._w, img)
        except Exception as e:
            pass

        canvas = tk.Canvas(window,width = 700,height = 320, bg = BACK_CLR)
        canvas.pack()
        #
        global mouse_pos_label
        mouse_pos_label = tk.Label(window,text = mouse_c.position,font = 24,bg = BACK_CLR)
        mouse_pos_label.after(100,update_mouse_pos)
        mouse_pos_label.place(x = 380,y = 180, width = 100, height = 20)
        #
        global time_btwn_clcks
        time_btwn_clcks = tk.Scale(window, orient = "horizontal", resolution = -1,length = 9999999,
                                   from_ = 0.001, to = 1 ,bg = BACK_CLR, font = 20,
                                   label = "Click interval (seconds)")
        time_btwn_clcks.place(x = 5,y = 0,width = 200)
        #
        global start_bttn
        start_bttn = tk.Button(window,text = "Start", font = 20, command = start)
        start_bttn.place(x = 5, y = 147, width = 135, height = 50)

        location_choose = tk.Label(window, text = "Mouse location", font = 20, bg = BACK_CLR)
        location_choose.place(x = 220,y =5, width = 160, height = 30)

        warning_label = tk.Label(window,text = "Move the cursor away to stop", bg = BACK_CLR)
        warning_label.place(x = 150, y = 180)

        global location_x
        location_x_label = tk.Label(window, text = "X",bg = BACK_CLR)
        location_x_label.place(x = 230, y = 40,height = 18)
        location_x = tk.Entry(window,justify = "right")
        location_x.insert(0,0)
        location_x.bind("<Return>",select_y)
        location_x.place(x = 250,y = 40, width = 50)

        global location_y
        location_y_label = tk.Label(window, text = "Y",bg = BACK_CLR)
        location_y_label.place(x = 305, y = 40,height = 18)
        location_y = tk.Entry(window, justify = "right")
        location_y.insert(0,0)
        location_y.bind("<Return>",select_x)
        location_y.place(x = 320,y = 40, width = 50)

        entry_cleaner = tk.Button(window,text = "Clear",font = 14, command = clean_entries)
        entry_cleaner.place(x = 380, y = 40 , width = 100, height = 20)
        #

        location_x.focus_set()

        window.mainloop()


    ### FUNC

    def update_mouse_pos():
        mouse_pos_label.config(text = mouse_c.position)
        mouse_pos_label.after(100,update_mouse_pos)
        pass

    def clean_entries():
        location_x.delete(0,"end")
        location_y.delete(0,"end")
        location_x.insert(0,0)
        location_y.insert(0,0)

    def select_x(key):
        location_x.focus_set()
        pass

    def select_y(key):
        location_y.focus_set()
        pass

    def stop():
        start_bttn["state"] = "normal"
        pass

    def start():
        start_bttn["state"] = "disabled"

        time_btwn_clcks_value = float(time_btwn_clcks.get())
        try:
            if float(location_x.get()) != None and float(location_y.get()) != None:
                location_x_value = float(location_x.get())
                location_y_value = float(location_y.get())

                mouse_c.position = (location_x_value,location_y_value)
                while mouse_c.position == (location_x_value,location_y_value):
                    mouse_c.click(mouse.Button.left)
                    time.sleep(time_btwn_clcks_value)
                    pass
                stop()

        except Exception as e:
            clean_entries()
            stop()

        pass

    ###

    GUI()
    pass




if __name__ == "__main__":
    main()
