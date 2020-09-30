import pynput,sys,random,time,pyautogui
from pynput import mouse,keyboard ### keyboard Listener ###Number of clicks (0 - infinite)
import tkinter as tk

def main():
    mouse_c = mouse.Controller()
    keyboard_c = keyboard.Controller()

    def LOGIC():
        global STARTED
        STARTED = False



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
        start_bttn = tk.Button(window,text = "Start",bg = BACK_CLR, font = 20) #, command = switch_to_stop
        start_bttn.place(x = 5, y = 268, width = 100, height = 50)

        global stop_bttn
        stop_bttn = tk.Button(window, text = "Stop" , bg = BACK_CLR, font = 20, state = "disabled") #, command = switch_to_start
        stop_bttn.place(x = 110, y = 268, width = 100, height = 50)
        #
        location_choose = tk.Label(window, text = "Mouse location", font = 20, bg = BACK_CLR)
        location_choose.place(x = 360,y =5, width = 160, height = 30)

        global location_x
        location_x_label = tk.Label(window, text = "X",bg = BACK_CLR)
        location_x_label.place(x = 380, y = 40,height = 18)
        location_x = tk.Entry(window)
        location_x.place(x = 395,y = 40, width = 50)

        global location_y
        location_y_label = tk.Label(window, text = "Y",bg = BACK_CLR)
        location_y_label.place(x = 450, y = 40,height = 18)
        location_y = tk.Entry(window)
        location_y.place(x = 465,y = 40, width = 50)
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

    # def switch_to_stop():
    #     STARTED = True
    #     #
    #     start_bttn.destroy()
    #     global stop_bttn
    #     stop_bttn = tk.Button(window,text = "Stop", command = switch_to_start, bg = BACK_CLR, font = 20)
    #     stop_bttn.place(x = 0, y = 270, width = 60, height = 50)
    #     #
    #     time_btwn_clcks_value = float(time_btwn_clcks.get())
    #     if location_x == '' and location_y == '':
    #         location_x_value = float(location_x.get())
    #         location_y_value = float(location_y.get())
    #     else:
    #         print("No values for mouse mos")
    #
    #     print("Starded : ",STARTED)
    #     print("Got value from time_btwn_clcks : {} \n".format(time_btwn_clcks_value))
    #     pass
    #
    # def switch_to_start():
    #     STARTED = False
    #     stop_bttn.destroy()
    #     start_bttn = tk.Button(window,text = "Start", command = switch_to_stop,bg = BACK_CLR, font = 20)
    #     start_bttn.place(x = 0, y = 270, width = 60, height = 50)
    #     print("Starded : ",STARTED)
    #     pass

    ###

    LOGIC()
    GUI()
    pass




if __name__ == "__main__":
    main()
