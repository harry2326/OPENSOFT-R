import ttkbootstrap as ttb
from ttkbootstrap.constants import *
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import serial


from ikpy.chain import Chain
from ikpy.link import URDFLink
import ikpy.utils.plot as plot_utils
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

import numpy as np
import cv2
from screeninfo import get_monitors

video = cv2.VideoCapture('intro.mp4')
monitors = get_monitors()
if monitors:
    screen_width = monitors[0].width
    screen_height = monitors[0].height
else:
    screen_width, screen_height = 1920, 1080

window_size = (screen_width, screen_height)
cv2.namedWindow('LOADING')
desired_fps=62
while True:
    ret, frame = video.read()
    if not ret:
        break
    frame = cv2.resize(frame, window_size)
    cv2.imshow('LOADING',frame)
     # Convert to milliseconds
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()



def mainwindow():
    # q
     # ser2= serial.Serial("COM4",9200)
    root = ttb.Window(themename="cyborg")
    root.title("EvoboTs")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=8)
    root.grid_rowconfigure(2, weight=5)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    partition1 = ttb.Frame(root, padding=10, borderwidth=2, relief="ridge")
    partition2 = ttb.Frame(root, padding=10, borderwidth=2, relief="ridge")
    partition3 = ttb.Frame(root, padding=10, borderwidth=2, relief="ridge")
    partition4 = ttb.Frame(root, padding=10, borderwidth=2, relief="ridge")
    partition5 = ttb.Frame(root, padding=10, borderwidth=2, relief="ridge")
    partition1.grid(row=0, column=0, padx=5, pady=5, columnspan=2, sticky="nsew")
    partition2.grid(row=1, column=0, padx=5, pady=5, columnspan=1, sticky="nsew")
    partition3.grid(row=2, column=0, padx=5, pady=5, columnspan=1, sticky="nsew")
    partition4.grid(row=1, column=1, padx=5, pady=5, columnspan=1, sticky="nsew")
    partition5.grid(row=2, column=1, padx=5, pady=5, columnspan=1, sticky="nsew")
    partition1.grid_propagate(False)
    partition2.grid_propagate(False)
    partition3.grid_propagate(False)
    partition4.grid_propagate(False)
    partition5.grid_propagate(False)
    partition4.grid_rowconfigure(0, weight=1)
    partition4.grid_columnconfigure(0, weight=1)


    # 11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

    def save_file():
        file = filedialog.asksaveasfilename(defaultextension=".txt")
        if file:
            with open(file, "w") as f:
                f.write(terminal.get("1.0", "end"))

    def open_file():
        file = filedialog.askopenfilename()
        if file:
            with open(file, "r") as f:
                terminal.delete("1.0", "end")
                terminal.insert("end", f.read())

    def new_file():
        terminal.delete("1.0", "end")

    partition1.grid_rowconfigure(0, weight=1)
    file_menu = ttk.Menubutton(partition1, text="File", style="dark")
    file_menu.grid(row=0, column=0, columnspan=1, sticky="nsew")
    file_menu.menu = tk.Menu(file_menu, tearoff=0)
    file_menu["menu"] = file_menu.menu
    file_menu.menu.add_command(label="Open", command=open_file)
    file_menu.menu.add_command(label="New", command=new_file)
    file_menu.menu.add_command(label="Save", command=save_file)

    sim_menu = ttk.Menubutton(partition1, text="Simulation", style="dark")
    sim_menu.grid(row=0, column=1, columnspan=1, sticky="nsew")
    sim_menu.menu = tk.Menu(sim_menu, tearoff=0)
    sim_menu["menu"] = sim_menu.menu
    sim_menu.menu.add_checkbutton(label="On")
    sim_menu.menu.add_checkbutton(label="Off")

    terminal_menu = ttk.Menubutton(partition1, text="Terminal", style="dark")
    terminal_menu.grid(row=0, column=2, columnspan=1, sticky="nsew")
    terminal_menu.menu = tk.Menu(terminal_menu, tearoff=0)
    terminal_menu["menu"] = terminal_menu.menu
    terminal_menu.menu.add_checkbutton(label="On")
    terminal_menu.menu.add_checkbutton(label="Off")

    def code_to_arduino():
        initialcommand = "coding"
        initialcommand = initialcommand + '\r'
        ser.write(initialcommand.encode())
        lines = terminal.get("1.0", "end").split("\n")
        for line in lines:
            for cmd in line.split(","):
                if "=" in cmd:
                    name, value = cmd.split("=")
                    name = name.strip()
                    value = value.strip()
                    if name == "speed":
                        val1 = "s1" + '\r'
                        ser.write(val1.encode())
                        val2 = value + '\r'
                        ser.write(val2.encode())
                    elif name == "acc":
                        val1 = "a1" + '\r'
                        ser.write(val1.encode())
                        val2 = value + '\r'
                        ser.write(val2.encode())
                    elif name == "st":
                        val1 = "start" + '\r'
                        ser.write(val1.encode())
                    elif name == "joint1":
                        val1 = "j1" + '\r'
                        ser.write(val1.encode())
                        val2 = value + '\r'
                        ser.write(val2.encode())
                    elif name == "joint2":
                        val1 = "j2" + '\r'
                        ser.write(val1.encode())
                        val2 = value + '\r'
                        ser.write(val2.encode())
                    elif name == "joint3":
                        val1 = "j3" + '\r'
                        ser.write(val1.encode())
                        val2 = value + '\r'
                        ser.write(val2.encode())
                    elif name == "joint4":
                        val1 = "j4" + '\r'
                        ser.write(val1.encode())
                        val2 = value + '\r'
                        ser.write(val2.encode())
                    elif name == "joint5":
                        val1 = "j5" + '\r'
                        ser.write(val1.encode())
                        val2 = value + '\r'
                        ser.write(val2.encode())
                    elif name == "join6":
                        val1 = "j6" + '\r'
                        ser.write(val1.encode())
                        val2 = value + '\r'
                        ser.write(val2.encode())
                    elif name == "end":
                        val1 = "end" + '\r'
                        print(val1)
                        ser.write(val1.encode())
                    elif name == "delay":
                        val1 = "d1" + '\r'
                        ser.write(val1.encode())
                        val2 = value + '\r'
                        ser.write(val2.encode())

    execute_code_button = ttb.Button(partition1, text="EXECUTE THE CODE", command=code_to_arduino, style="dark")
    execute_code_button.grid(row=0, column=3, columnspan=1, sticky="nsew")
    execute_code_button.grid_propagate(False)

    def pausecode():
        pausecode = pause_code_button.cget('text')
        if (pausecode == 'PAUSE'):
            pause_code_button.config(text='CONTINUE')
        if (pausecode == 'CONTINUE'):
            pause_code_button.config(text='PAUSE')
        pausecode = pausecode + '\r'
        ser.write(pausecode.encode())
        ser2.write(pausecode.encode())

    pause_code_button = ttb.Button(partition1, text="PAUSE", command=pausecode, style="dark")
    pause_code_button.grid(row=0, column=4, columnspan=1, sticky="nsew")
    pause_code_button.grid_propagate(False)

    def stopcode():
        stopcode = 'STOP'
        stopcode = stopcode + '\r'
        print(stopcode)
        ser.write(stopcode.encode())

    stop_code_button = ttb.Button(partition1, text="STOP", command=stopcode, style="dark")
    stop_code_button.grid(row=0, column=5, columnspan=1, sticky="nsew")
    stop_code_button.grid_propagate(False)

    def homecode():
        homecode = "HOME"
        homecode = homecode + '\r'
        ser.write(homecode.encode())
        speed = str(speedmeter.amountusedvar.get())
        speed = speed + '\r'
        acc = str(accmeter.amountusedvar.get())
        acc = acc + '\r'
        ser.write(speed.encode())
        ser.write(acc.encode())
        joint_1 = str(0)
        joint_1 = joint_1 + '\r'
        joint_2 = str(0)
        joint_2 = joint_2 + '\r'
        joint_3 = str(0)
        joint_3 = joint_3 + '\r'
        joint_4 = str(0)
        joint_4 = joint_4 + '\r'
        joint_5 = str(0)
        joint_5 = joint_5 + '\r'
        ser.write(joint_1.encode())
        ser.write(joint_2.encode())
        ser.write(joint_3.encode())
        # ser2.write(homecode.encode())
        # ser2.write(speed.encode())
        # ser2.write(acc.encode())
        # ser2.write(joint_4.encode())
        # ser2.write(joint_5.encode())

    home_code_button = ttb.Button(partition1, text="HOME", command=homecode, style="dark")
    home_code_button.grid(row=0, column=6, columnspan=1, sticky="nsew")
    home_code_button.grid_propagate(False)

    ttk.Button(partition1, text="Exit", command=root.quit, style="dark").grid(row=0, column=7, columnspan=1,
                                                                              sticky="nsew")

    # 22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
    partition2.grid_rowconfigure(0, weight=3)
    partition2.grid_rowconfigure(1, weight=1)
    partition2.grid_rowconfigure(2, weight=1)
    partition2.grid_rowconfigure(3, weight=1)
    partition2.grid_rowconfigure(4, weight=1)
    partition2.grid_columnconfigure(0, weight=1)
    partition2.grid_columnconfigure(1, weight=1)

    speed_frame = ttk.Frame(partition2, padding=10)
    speed_frame.grid(row=0, column=0, columnspan=1, sticky="nsew")
    acc_frame = ttk.Frame(partition2, padding=10)
    acc_frame.grid(row=0, column=1, columnspan=1, sticky="nsew")
    speed_frame.grid_rowconfigure(0, weight=1)
    speed_frame.grid_columnconfigure(0, weight=1)
    acc_frame.grid_rowconfigure(0, weight=1)
    acc_frame.grid_columnconfigure(0, weight=1)
    speed_frame.grid_propagate(False)
    acc_frame.grid_propagate(False)
    speedmeter = ttb.Meter(speed_frame, stripethickness=4, bootstyle="light", metertype='semi', showtext=True,
                           textright="%", subtext="SPEED", arcrange=270, interactive=True, metersize=180)
    speedmeter.grid(row=0, column=0, sticky="ew")
    accmeter = ttb.Meter(acc_frame, bootstyle="light", stripethickness=4, metertype='semi', showtext=True,
                         textright="%", subtext="ACCELERATION", arcrange=270, interactive=True, metersize=180)
    accmeter.grid(row=0, column=0, sticky="ew")

    joint1_frame = ttk.Frame(partition2, padding=10)
    joint1_frame.grid(row=1, column=0, columnspan=1, sticky="nsew")
    joint2_frame = ttk.Frame(partition2, padding=10)
    joint2_frame.grid(row=1, column=1, columnspan=1, sticky="nsew")
    joint3_frame = ttk.Frame(partition2, padding=10)
    joint3_frame.grid(row=2, column=0, columnspan=1, sticky="nsew")
    joint4_frame = ttk.Frame(partition2, padding=10, )
    joint4_frame.grid(row=2, column=1, columnspan=1, sticky="nsew")
    joint5_frame = ttk.Frame(partition2, padding=10)
    joint5_frame.grid(row=3, column=0, columnspan=1, sticky="nsew")
    joint6_frame = ttk.Frame(partition2, padding=10)
    joint6_frame.grid(row=3, column=1, columnspan=1, sticky="nsew")
    executebutton_frame = ttk.Frame(partition2, padding=10, )
    executebutton_frame.grid(row=4, column=0, columnspan=2, sticky="nsew")
    joint1_frame.grid_propagate(False)
    joint2_frame.grid_propagate(False)
    joint3_frame.grid_propagate(False)
    joint4_frame.grid_propagate(False)
    joint5_frame.grid_propagate(False)
    joint6_frame.grid_propagate(False)
    executebutton_frame.grid_propagate(False)

    joint1_frame.grid_rowconfigure(0, weight=1)
    joint1_frame.grid_rowconfigure(1, weight=1)
    joint1_frame.grid_columnconfigure(0, weight=1)
    joint1_frame.grid_columnconfigure(1, weight=3)
    joint1lable = ttb.Label(joint1_frame, bootstyle="inverse-light", text="    JOINT1    ", font=("bold", 12))
    joint1lable.grid(row=0, column=0, sticky="nsew")
    joint1lable2 = ttb.Label(joint1_frame, bootstyle="inverse-light", text="0", font=("bold", 14), anchor="center")
    joint1lable2.grid(row=1, column=0, sticky="nsew")

    def joint1scaler(a):
        joint1lable2.config(text=f'{int(joint1scale.get())}')

    joint1scale = ttb.Scale(joint1_frame, bootstyle="secondary", length=300, orient="horizontal", from_=-180, to=180,
                            command=joint1scaler, )
    joint1scale.grid(row=0, rowspan=2, column=1, sticky="w", padx=(15, 0))

    joint2_frame.grid_rowconfigure(0, weight=1)
    joint2_frame.grid_rowconfigure(1, weight=1)
    joint2_frame.grid_columnconfigure(0, weight=1)
    joint2_frame.grid_columnconfigure(1, weight=3)
    joint2lable = ttb.Label(joint2_frame, bootstyle="inverse-light", text="    JOINT2    ", font=("bold", 12))
    joint2lable.grid(row=0, column=0, sticky="nsew")
    joint2lable2 = ttb.Label(joint2_frame, bootstyle="inverse-light", text="0", font=("bold", 14), anchor="center")
    joint2lable2.grid(row=1, column=0, sticky="nsew")

    def joint2scaler(b):
        joint2lable2.config(text=f'{int(joint2scale.get())}')

    joint2scale = ttb.Scale(joint2_frame, bootstyle="secondary", length=300, orient="horizontal", from_=-180, to=180,
                            command=joint2scaler)
    joint2scale.grid(row=0, rowspan=2, column=1, sticky="w", padx=(15, 0))

    joint3_frame.grid_rowconfigure(0, weight=1)
    joint3_frame.grid_rowconfigure(1, weight=1)
    joint3_frame.grid_columnconfigure(0, weight=1)
    joint3_frame.grid_columnconfigure(1, weight=3)
    joint3lable = ttb.Label(joint3_frame, bootstyle="inverse-light", text="    JOINT3    ", font=("bold", 12))
    joint3lable.grid(row=0, column=0, sticky="nsew")
    joint3lable2 = ttb.Label(joint3_frame, bootstyle="inverse-light", text="0", font=("bold", 14), anchor="center")
    joint3lable2.grid(row=1, column=0, sticky="nsew")

    def joint3scaler(c):
        joint3lable2.config(text=f'{int(joint3scale.get())}')

    joint3scale = ttb.Scale(joint3_frame, bootstyle="secondary", length=300, orient="horizontal", from_=-180, to=180,
                            command=joint3scaler)
    joint3scale.grid(row=0, rowspan=2, column=1, sticky="w", padx=(15, 0))

    joint4_frame.grid_rowconfigure(0, weight=1)
    joint4_frame.grid_rowconfigure(1, weight=1)
    joint4_frame.grid_columnconfigure(0, weight=1)
    joint4_frame.grid_columnconfigure(1, weight=3)
    joint4lable = ttb.Label(joint4_frame, bootstyle="inverse-light", text="    JOINT4    ", font=("bold", 12))
    joint4lable.grid(row=0, column=0, sticky="nsew")
    joint4lable2 = ttb.Label(joint4_frame, bootstyle="inverse-light", text="0", font=("bold", 14), anchor="center")
    joint4lable2.grid(row=1, column=0, sticky="nsew")

    def joint4scaler(a):
        joint4lable2.config(text=f'{int(joint4scale.get())}')

    joint4scale = ttb.Scale(joint4_frame, bootstyle="secondary", length=300, orient="horizontal", from_=-180, to=180,
                            command=joint4scaler)
    joint4scale.grid(row=0, rowspan=2, column=1, sticky="w", padx=(15, 0))

    joint5_frame.grid_rowconfigure(0, weight=1)
    joint5_frame.grid_rowconfigure(1, weight=1)
    joint5_frame.grid_columnconfigure(0, weight=1)
    joint5_frame.grid_columnconfigure(1, weight=3)
    joint5lable = ttb.Label(joint5_frame, bootstyle="inverse-light", text="    JOINT5    ", font=("bold", 12))
    joint5lable.grid(row=0, column=0, sticky="nsew")
    joint5lable2 = ttb.Label(joint5_frame, bootstyle="inverse-light", text="0", font=("bold", 14), anchor="center")
    joint5lable2.grid(row=1, column=0, sticky="nsew")

    def joint5scaler(a):
        joint5lable2.config(text=f'{int(joint5scale.get())}')

    joint5scale = ttb.Scale(joint5_frame, bootstyle="secondary", length=300, orient="horizontal", from_=-180, to=180,
                            command=joint5scaler)
    joint5scale.grid(row=0, rowspan=2, column=1, sticky="w", padx=(15, 0))

    joint6_frame.grid_rowconfigure(0, weight=1)
    joint6_frame.grid_rowconfigure(1, weight=1)
    joint6_frame.grid_columnconfigure(0, weight=1)
    joint6_frame.grid_columnconfigure(1, weight=3)
    joint6lable = ttb.Label(joint6_frame, bootstyle="inverse-light", text="    JOINT6    ", font=("bold", 12))
    joint6lable.grid(row=0, column=0, sticky="nsew")
    joint6lable2 = ttb.Label(joint6_frame, bootstyle="inverse-light", text="0", font=("bold", 14), anchor="center")
    joint6lable2.grid(row=1, column=0, sticky="nsew")

    def joint6scaler(a):
        joint6lable2.config(text=f'{int(joint6scale.get())}')

    joint6scale = ttb.Scale(joint6_frame, bootstyle="secondary", length=300, orient="horizontal", from_=-180, to=180,
                            command=joint6scaler)
    joint6scale.grid(row=0, rowspan=2, column=1, sticky="w", padx=(15, 0))

    executebutton_frame.grid_rowconfigure(0, weight=1)
    executebutton_frame.grid_columnconfigure(0, weight=1)
    executebutton_frame.grid_columnconfigure(1, weight=1)
    executebutton_frame.grid_columnconfigure(2, weight=1)

    def send_to_arduinoonce():
        print("send to arduino once")
        joint_1 = str(joint1scale.get())
        joint_1 = joint_1 + '\r'
        joint_2 = str(joint2scale.get())
        joint_2 = joint_2 + '\r'
        joint_3 = str(joint3scale.get())
        joint_3 = joint_3 + '\r'
        # joint_4 = str(joint4scale.get())
        # joint_4 = joint_4 + '\r'
        # joint_5 = str(joint5scale.get())
        # joint_5 = joint_5 + '\r'
        speed = str(speedmeter.amountusedvar.get())
        speed = speed + '\r'
        acc = str(accmeter.amountusedvar.get())
        acc = acc + '\r'
        cmd = "singlerun"
        cmd = cmd + '\r'
        ser.write(cmd.encode())
        ser.write(speed.encode())
        ser.write(acc.encode())
        ser.write(joint_1.encode())
        ser.write(joint_2.encode())
        ser.write(joint_3.encode())
        # ser2.write(cmd.encode())
        # ser2.write(speed.encode())
        # ser2.write(acc.encode())
        # ser2.write(joint_4.encode())
        # ser2.write(joint_5.encode())

    run_button = ttb.Button(executebutton_frame, bootstyle="warning-outline", text="RUN", command=send_to_arduinoonce)
    run_button.grid(row=0, column=0, sticky="nsew", columnspan=1, rowspan=1)

    def send_to_arduinoloop():
        print("send to arduino loop")
        joint_1 = str(joint1scale.get())
        joint_1 = joint_1 + '\r'
        joint_2 = str(joint2scale.get())
        joint_2 = joint_2 + '\r'
        joint_3 = str(joint3scale.get())
        joint_3 = joint_3 + '\r'
        joint_4 = str(joint4scale.get())
        joint_4 = joint_4 + '\r'
        joint_5 = str(joint5scale.get())
        joint_5 = joint_5 + '\r'
        speed = str(speedmeter.amountusedvar.get())
        speed = speed + '\r'
        acc = str(accmeter.amountusedvar.get())
        acc = acc + '\r'
        cmd = "looprun"
        cmd = cmd + '\r'
        ser.write(cmd.encode())
        ser.write(speed.encode())
        ser.write(acc.encode())
        ser.write(joint_1.encode())
        ser.write(joint_2.encode())
        ser.write(joint_3.encode())
        ser2.write(cmd.encode())
        ser2.write(speed.encode())
        ser2.write(joint_4.encode())
        # ser2.write(joint_5.encode())

    loop_button = ttb.Button(executebutton_frame, bootstyle="warning-outline", text="LOOP-RUN",
                             command=send_to_arduinoloop)
    loop_button.grid(row=0, column=1, sticky="nsew", columnspan=1)



    def send_to_simulate():
        print("simulate it")
        joint1 = joint1scale.get()
        joint2 = joint2scale.get()
        joint3 = joint3scale.get()
        joint4 = joint4scale.get()
        joint5 = joint5scale.get()
        joint1_rad = math.radians(joint1)
        joint2_rad = math.radians(joint2)
        joint3_rad = math.radians(joint3)
        joint4_rad = math.radians(joint4)
        joint5_rad = math.radians(joint5)
        ik_angles = [0, joint1_rad, joint2_rad, joint3_rad, joint4_rad, joint5_rad, 0]
        urdf_file_path = "C:/Users/harry/Downloads/topbot.urdf"  # Replace with your actual URDF file path
        chain = Chain.from_urdf_file(urdf_file_path, active_links_mask=[False, True, True, True, True, True, False])
        position_check = chain.forward_kinematics(ik_angles)
        x_final = position_check[0, 3]
        y_final = position_check[1, 3]
        z_final = position_check[2, 3]
        target_pose = [x_final, y_final, z_final]
        fig, ax = plot_utils.init_3d_figure()
        fig.set_figheight(9)
        fig.set_figwidth(15)
        chain.plot(ik_angles, ax, target=target_pose)
        plt.xlim(-0.5, 0.5)
        plt.ylim(-0.5, 0.5)
        ax.set_zlim(0, 0.8)
        plt.ion()
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=partition4)
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
        canvas.get_tk_widget().grid_propagate(False)


    simulate_button = ttb.Button(executebutton_frame, bootstyle="warning-outline", text="SIMULATE",
                                 command=send_to_simulate)
    simulate_button.grid(row=0, column=2, sticky="nsew", columnspan=1)

    # 33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    partition3.grid_rowconfigure(0, weight=8)
    partition3.grid_rowconfigure(1, weight=1)
    partition3.grid_columnconfigure(0, weight=1)
    terminal = tk.Text(partition3, font=('TkDefault', 15))
    terminal.grid(row=0, column=0, columnspan=1, sticky="nsew", rowspan=1)

    def execute_command(event=None):
        lines = terminal.get("1.0", "end").split("\n")
        for line in lines:
            for cmd in line.split(","):
                if "=" in cmd:
                    name, value = cmd.split("=")
                    name = name.strip()
                    value = value.strip()
                    if name == "speed":
                        speedmeter.configure(amountused=int(value))
                    elif name == "acc":
                        accmeter.configure(amountused=int(value))
                    elif name == "joint1":
                        joint1scale.set(value=int(value))
                    elif name == "joint2":
                        joint2scale.set(value=int(value))
                    elif name == "joint3":
                        joint3scale.set(value=int(value))
                    elif name == "joint4":
                        joint4scale.set(value=int(value))
                    elif name == "joint5":
                        joint5scale.set(value=int(value))
                    elif name == "join6":
                        joint6scale.set(value=int(value))

    terminal.bind("<Return>", execute_command)
    terminal.grid_propagate(False)

    # 555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
    partition5.grid_rowconfigure(0, weight=1)
    partition5.grid_rowconfigure(1, weight=2)
    partition5.grid_rowconfigure(2, weight=2)
    partition5.grid_rowconfigure(3, weight=2)
    partition5.grid_columnconfigure(0, weight=1)
    partition5.grid_columnconfigure(1, weight=2)
    partition5.grid_columnconfigure(2, weight=2)
    partition5.grid_columnconfigure(3, weight=2)
    partition5.grid_columnconfigure(4, weight=2)
    partition5.grid_columnconfigure(5, weight=2)
    partition5.grid_columnconfigure(6, weight=2)
    partition5.grid_columnconfigure(7, weight=2)
    currentposlabe = ttb.Label(partition5, bootstyle="inverse-light", text="CURRENT POS", anchor="center", font=(14))
    currentposlabe.grid(row=0, column=0, sticky="nswe", columnspan=4, rowspan=1)
    currentposlabe.grid_propagate(False)
    updateposlabe = ttb.Label(partition5, bootstyle="inverse-light", text="UPDATE POS", anchor="center", font=(14))
    updateposlabe.grid(row=0, column=4, sticky="nswe", columnspan=4, rowspan=1)
    updateposlabe.grid_propagate(False)
    x_lable = ttb.Label(partition5, text="X:", bootstyle="light", font=(15), anchor="center")
    x_lable.grid(row=1, column=0, columnspan=2)

    y_lable = ttb.Label(partition5, text="Y:", bootstyle="light", font=(15), anchor="center")
    y_lable.grid(row=1, column=2, columnspan=2)

    z_lable = ttb.Label(partition5, text="Z:", bootstyle="light", font=(15), anchor="center")
    z_lable.grid(row=2, column=0, columnspan=2)

    roll_lable = ttb.Label(partition5, text="ROLL:", bootstyle="light", font=(15), anchor="center")
    roll_lable.grid(row=2, column=2, columnspan=2)

    pitch_lable = ttb.Label(partition5, text="PITCH:", bootstyle="light", font=(15), anchor="center")
    pitch_lable.grid(row=3, column=0, columnspan=2)

    yaw_lable = ttb.Label(partition5, text="YAW:", bootstyle="light", font=(15), anchor="center")
    yaw_lable.grid(row=3, column=2, columnspan=2)

    def sendinverse():
        urdf_file_path = "C:/Users/harry/Downloads/topbot.urdf"
        chain = Chain.from_urdf_file(urdf_file_path, active_links_mask=[False, True, True, True, True, True, False])
        x_value = x_var.get()
        y_value = y_var.get()
        z_value = z_var.get()
        x_value = x_value / 1000
        y_value = y_value / 1000
        z_value = z_value / 1000
        target_pose = [x_value, y_value, z_value]
        ik_angles = chain.inverse_kinematics(target_pose)
        ik_angles_degrees = [math.degrees(angle) for angle in ik_angles]
        print(ik_angles_degrees)
        firstdegAng = (ik_angles_degrees[1])
        firstdegAng = round(firstdegAng, 5)
        seconddegAng = (ik_angles_degrees[2])
        seconddegAng = round(seconddegAng, 5)
        thirddegAng = (ik_angles_degrees[3])
        thirddegAng = round(thirddegAng, 5)
        firstdegAng = str(firstdegAng)
        seconddegAng = str(seconddegAng)
        thirddegAng = str(thirddegAng)
        firstdegAng = firstdegAng + '\r'
        seconddegAng = seconddegAng + '\r'
        thirddegAng = thirddegAng + '\r'
        ser.write(firstdegAng.encode())
        ser.write(seconddegAng.encode())
        ser.write(thirddegAng.encode())
        position_check = chain.forward_kinematics(ik_angles)
        x_final = position_check[0, 3]
        y_final = position_check[1, 3]
        z_final = position_check[2, 3]
        x_final = x_final * 1000
        y_final = y_final * 1000
        z_final = z_final * 1000
        x_final = round(x_final, 4)
        y_final = round(y_final, 4)
        z_final = round(z_final, 4)
        x_lable.config(text=f"X: {x_final}")
        y_lable.config(text=f"Y: {(y_final)}")
        z_lable.config(text=f"Z: {(z_final)}")

    x_var = IntVar(value=0)
    x_spinbox = Spinbox(partition5, from_=-600, to=600, textvariable=x_var, font=15, command=sendinverse)
    x_spinbox.grid(row=1, column=4, columnspan=2, sticky="nsew")

    y_var = IntVar(value=0)
    y_spinbox = Spinbox(partition5, from_=-600, to=600, textvariable=y_var, font=15, command=sendinverse)
    y_spinbox.grid(row=1, column=6, columnspan=2, sticky="nsew")

    z_var = IntVar(value=0)
    z_spinbox = Spinbox(partition5, from_=-600, to=600, textvariable=z_var, font=15, command=sendinverse)
    z_spinbox.grid(row=2, column=4, columnspan=2, sticky="nsew")

    def inversereceive():
        while (ser.inWaiting() == 0):
            pass

        datapack = ser.readline().strip()
        datapack = str(datapack, 'utf-8')

        datapack = int(datapack)
        datapack1 = ser.readline().strip()
        datapack1 = str(datapack1, 'utf-8')
        datapack1 = int(datapack1)
        datapack2 = ser.readline().strip()
        datapack2 = str(datapack2, 'utf-8')
        datapack2 = int(datapack2)
        urdf_file_path = "C:/Users/harry/Downloads/topbot.urdf"  # Replace with your actual URDF file path
        chain = Chain.from_urdf_file(urdf_file_path, active_links_mask=[False, True, True, True, True, True, False])
        ik_angles = [0, datapack, datapack1, datapack2, 0, 0, 0]
        ik_angles_degrees = [math.radians(angle) for angle in ik_angles]
        print(ik_angles_degrees)
        position_check = chain.forward_kinematics(ik_angles)
        x_final = position_check[0, 3]
        y_final = position_check[1, 3]
        z_final = position_check[2, 3]
        x_final = x_final * 1000
        y_final = y_final * 1000
        z_final = z_final * 1000
        x_final = round(x_final, 4)
        y_final = round(y_final, 4)
        z_final = round(z_final, 4)
        print("Final Position (x, y, z):", x_final, y_final, z_final)
        x_lable.config(text=f"X: {x_final}")
        y_lable.config(text=f"Y: {(y_final)}")
        z_lable.config(text=f"Z: {(z_final)}")
        x_var.set(x_final)
        y_var.set(y_final)
        z_var.set(z_final)

    var = StringVar()

    def on_check():
        if var.get() == "1":
            cmd = "inverse"
            cmd = cmd + '\r'
            ser.write(cmd.encode())
            inversereceive()

        else:
            print("Checkbutton is unchecked")

    ttk.Checkbutton(partition1, text='Live', bootstyle="success", variable=var, command=on_check).grid(row=0, column=8,
                                                                                                       columnspan=1,
                                                                                                       sticky="nsew")

    root.mainloop()

mainwindow()



