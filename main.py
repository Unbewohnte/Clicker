import pynput,sys,random,time,pyautogui
from pynput import mouse,keyboard ### keyboard Listener ###Number of clicks (0 - infinite)
import tkinter as tk

def main():
    mouse_c = mouse.Controller()
    keyboard_c = keyboard.Controller()


    def GUI():
        global BACK_CLR
        BACK_CLR = '#e3e1e8'

        global window
        window = tk.Tk()
        window.title('Clicker')
        window.geometry(("700x300"))
        window.minsize(700,320)
        window.maxsize(700,320)
        canvas = tk.Canvas(window,width = 700,height = 320, bg = BACK_CLR)
        canvas.pack()
        #
        #listener = keyboard.Listener(on_press= switch_to_start)
        #listener.start()
        #
        global mouse_pos_label
        mouse_pos_label = tk.Label(window,text = mouse_c.position,font = 24,bg = BACK_CLR)
        mouse_pos_label.after(100,update_mouse_pos)
        mouse_pos_label.place(x = 400,y = 300, width = 100, height = 20)
        #
        global time_btwn_clcks
        time_btwn_clcks = tk.Scale(window, orient = "horizontal", resolution = -1,length = 10000,
                                   from_ = 0.05, to = 500 ,bg = BACK_CLR, font = 20,
                                   label = "Click interval (seconds)")
        time_btwn_clcks.place(x = 5,y = 0,width = 200)
        #
        global start_bttn
        start_bttn = tk.Button(window,text = "Start",bg = BACK_CLR, font = 20, command = start) #, command = switch_to_stop
        start_bttn.place(x = 5, y = 268, width = 100, height = 50)

        global stop_bttn
        stop_bttn = tk.Button(window, text = "Stop" , bg = BACK_CLR, font = 20, state = "disabled", command = stop) #, command = switch_to_start
        stop_bttn.place(x = 110, y = 268, width = 100, height = 50)
        #

        location_choose = tk.Label(window, text = "Mouse location", font = 20, bg = BACK_CLR)
        location_choose.place(x = 360,y =5, width = 160, height = 30)

        global location_x
        location_x_label = tk.Label(window, text = "X",bg = BACK_CLR)
        location_x_label.place(x = 380, y = 40,height = 18)
        location_x = tk.Entry(window,justify = "right")
        location_x.insert(0,0)
        location_x.place(x = 395,y = 40, width = 50)

        global location_y
        location_y_label = tk.Label(window, text = "Y",bg = BACK_CLR)
        location_y_label.place(x = 450, y = 40,height = 18)
        location_y = tk.Entry(window, justify = "right")
        location_y.insert(0,0)
        location_y.place(x = 465,y = 40, width = 50)

        entry_cleaner = tk.Button(window,text = "Clear",font = 14, command = clean_entries)
        entry_cleaner.place(x = 520, y = 40 , width = 100, height = 20)
        #
        #pretender = tk.Checkbutton(window,text = "Pretend to be online",bg = BACK_CLR)
        #pretender.place(x = 350, y = 5)
        #
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

    def stop():
        print("Stopped \n")
        start_bttn["state"] = "normal"
        stop_bttn["state"] = "disabled"
        pass

    def start():
        print("Started")
        start_bttn["state"] = "disabled"
        stop_bttn["state"] = "normal"

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
            print("Error ! ",e)
            clean_entries()
            stop()

        pass

    ###

    GUI()
    pass




if __name__ == "__main__":
    main()
