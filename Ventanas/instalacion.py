import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.font import Font
from tkinter.ttk import Progressbar

from pathlib import Path
import rutines
import version
import ctypes
import os
from sys import exit
import json
import shutil


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
disabled = False
admin = False

flag_wClient = True
flag_lmsp = True
flag_gzip = True
flag_fecha = True
flag_fnumber = True
flag_lenguaje = True
flag_wrap = True
flag_installWClient = True
flag_installLMS = True
flag_installWinSCP = True
flag_pathWinSCP = True


def test():
    print("hola mundo")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def createView(app):
    newWindow = tk.Toplevel(app)
    newWindow.grab_set()
    newWindow.focus_set()
    newWindow.configure(bg="white")
    ancho_ventana = 1000
    alto_ventana = 1000
    x_ventana = newWindow.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = newWindow.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
        "+" + str(x_ventana) + "+" + str(y_ventana)
    newWindow.geometry(posicion)

    # Configuraciones de botones a utilizar
    ajuste_x_btn = 400

    # Fuente a utilizar
    f_font = "Arial Nova"
    title_font = Font(family=f_font, size=18)
    sbtl_font = Font(family=f_font, size=14)
    gnrl_font = Font(family=f_font, size=10)

    on = PhotoImage(file="assets/on-24.png")
    off = PhotoImage(file="assets/off-24.png")
    config = PhotoImage(file="assets/config.png")

    canvas = Canvas(
        newWindow,
        bg="white",
        height=alto_ventana,
        width=ancho_ventana,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    canvas.create_text(
        400.0,
        57.0,
        anchor="nw",
        text="INSTALACION LMS",
        fill="#000000",
        font=(title_font)
    )

    canvas.create_text(
        36.0,
        117.0,
        anchor="nw",
        text="VERIFICACION DE PERMISOS",
        fill="#000000",
        font=(sbtl_font)
    )

    checkframe = tk.Frame(newWindow, bg="white")
    checkframe.place(x=60, y=158)
    def changeVersion():
        x = version.my_treeview(newWindow)
        print(x)
        
    def is_disabled():
        global disabled
        if disabled != True:
            try:
                rutines.editHost()
                c2.select()
                disabled = True
            except:
                disabled = False
                c2.deselect()
        else:
            c2.select()
            disabled = True

    def is_admin():
        global admin
        try:
            admin = os.getuid() == 0
        except AttributeError:
            admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if(admin):
            c1.select()
        else:
            c1.deselect()

    def check():
        is_disabled()
        is_admin()
        if disabled and admin != True:
            changeState(0)
        else:
            changeState(1)

    vc1 = tk.IntVar(checkframe)
    vc2 = tk.IntVar(checkframe)

    c1 = tk.Checkbutton(checkframe, text='El usuario es administrador', font=gnrl_font,
                        variable=vc1, state="disabled",  bg="white")
    c1.grid(column=1, row=2)

    c2 = tk.Checkbutton(checkframe, text='User Account Control: Run all administrators \nin Admin Approval Mode: [Disable]', font=gnrl_font,
                        variable=vc2, state="disabled", bg="white")

    c2.grid(column=2, row=2)

    button_1 = Button(
        newWindow,
        text="Verificacion",
        borderwidth=0,
        highlightthickness=0,
        command=check,
        relief="flat",
        bg="#C13737",
        fg='#FFFFFF'
    )

    button_1.place(
        x=560,
        y=170,
        width=150,
        height=20
    )

    button_2 = Button(
        newWindow,
        text="Instalacion",
        borderwidth=0,
        highlightthickness=0,
        # command=installLMS,
        relief="flat",
        bg="#C13737",
        fg='#FFFFFF'
    )

    button_2.place(
        x=720,
        y=170,
        width=150,
        height=20
    )

    canvas.create_text(
        36.0,
        258.0,
        anchor="nw",
        text="OBTENCION DE ARCHIVOS A UTILIZAR",
        fill="#000000",
        font=(sbtl_font)
    )

 
    def changeState(mode):
        if mode == 0:
            btn_wClient.config(state='disabled')
            btn_lmsp.config(state='disabled')
            btn_gzip.config(state='disabled')
            btn_fecha.config(state='disabled')
            btn_fnumber.config(state='disabled')
            btn_lenguaje.config(state='disabled')
            btn_wrap.config(state='disabled')
            btn_installWClient.config(state='disabled')
            btn_installWinSCP.config(state='disabled')
            btn_installLMS.config(state='disabled')
            btn_pathWinSCP.config(state='disabled')
        else:
            btn_wClient.config(state='active')
            btn_lmsp.config(state='active')
            btn_gzip.config(state='active')
            btn_fecha.config(state='active')
            btn_fnumber.config(state='active')
            btn_lenguaje.config(state='active')
            btn_wrap.config(state='active')
            btn_installWClient.config(state='active')
            btn_installWinSCP.config(state='active')
            btn_installLMS.config(state='active')
            btn_pathWinSCP.config(state='active')

    def Switch(btn):
        global flag_wClient
        global flag_lmsp
        global flag_gzip
        global flag_fecha
        global flag_fnumber
        global flag_lenguaje
        global flag_wrap
        global flag_installWClient
        global flag_installLMS
        global flag_installWinSCP
        global flag_pathWinSCP
        if btn == "wClient":
            if flag_wClient:
                btn_wClient.config(image=off)
                flag_wClient = False
            else:
                btn_wClient.config(image=on)
                flag_wClient = True
        if btn == "lmsp":
            if flag_lmsp:
                btn_lmsp.config(image=off)
                flag_lmsp = False
            else:
                btn_lmsp.config(image=on)
                flag_lmsp = True
        if btn == "gzip":
            if flag_gzip:
                btn_gzip.config(image=off)
                flag_gzip = False
            else:
                btn_gzip.config(image=on)
                flag_gzip = True
        if btn == "fecha":
            if flag_fecha:
                btn_fecha.config(image=off)
                flag_fecha = False
            else:
                btn_fecha.config(image=on)
                flag_fecha = True
        if btn == "fnumber":
            if flag_fnumber:
                btn_fnumber.config(image=off)
                flag_fnumber = False
            else:
                btn_fnumber.config(image=on)
                flag_fnumber = True
        if btn == "lenguaje":
            if flag_lenguaje:
                btn_lenguaje.config(image=off)
                flag_lenguaje = False
            else:
                btn_lenguaje.config(image=on)
                flag_lenguaje = True
        if btn == "wrap":
            if flag_wrap:
                btn_wrap.config(image=off)
                flag_wrap = False
            else:
                btn_wrap.config(image=on)
                flag_wrap = True
        if btn == "installWClient":
            if flag_installWClient:
                btn_installWClient.config(image=off)
                flag_installWClient = False
            else:
                btn_installWClient.config(image=on)
                flag_installWClient = True
        if btn == "installLMS":
            if flag_installLMS:
                btn_installLMS.config(image=off)
                flag_installLMS = False
            else:
                btn_installLMS.config(image=on)
                flag_installLMS = True
        if btn == "installWinSCP":
            if flag_installWinSCP:
                btn_installWinSCP.config(image=off)
                flag_installWinSCP = False
            else:
                btn_installWinSCP.config(image=on)
                flag_installWinSCP = True
        if btn == "pathWinSCP":
            if flag_pathWinSCP:
                btn_pathWinSCP.config(image=off)
                flag_pathWinSCP = False
            else:
                btn_pathWinSCP.config(image=on)
                flag_pathWinSCP = True


    canvas.create_text(
        114.0,
        291.0,
        anchor="nw",
        text="WebClient",
        fill="#000000",
        font=(gnrl_font)
    )
    btn_wClient = Button(
        newWindow,
        image=on,
        bd=0,
        command=lambda: Switch("wClient"),
        bg="#FFFFFF",
        fg='#FFFFFF',
        width=22,
        height=12
    )
    btn_wClient.place(
        x=ajuste_x_btn,
        y=291
    )

    canvas.create_text(
        114.0,
        327.0,
        anchor="nw",
        text="LMS 12.2.prowcapc",
        fill="#000000",
        font=(gnrl_font)
    )
    btn_lmsp = Button(
        newWindow,
        image=on,
        bd=0,
        command=lambda: Switch("lmsp"),
        bg="#FFFFFF",
        fg='#FFFFFF',
        width=22,
        height=12
    )
    btn_lmsp.place(
        x=ajuste_x_btn,
        y=327
    )
    
    btn_version = Button(
        newWindow,
        image=config,
        borderwidth=0,
        command=changeVersion,
        highlightthickness=0,
        relief="flat",
        bg="#FFFFFF",
    )

    btn_version.place(
        x=ajuste_x_btn + 35,
        y=327,
    )

    
    
    
    button_1 = Button(
        newWindow,
        text="Verificacion",
        borderwidth=0,
        highlightthickness=0,
        command=check,
        relief="flat",
        bg="#C13737",
        fg='#FFFFFF'
    )

    canvas.create_text(
        115.0,
        359.0,
        anchor="nw",
        text="Gunzip",
        fill="#000000",
        font=(gnrl_font)
    )

    btn_gzip = Button(
        newWindow,
        image=on,
        bd=0,
        command=lambda: Switch("gzip"),
        bg="#FFFFFF",
        fg='#FFFFFF',
        width=22,
        height=12
    )
    btn_gzip.place(
        x=ajuste_x_btn,
        y=359
    )

    canvas.create_text(
        32.0,
        407.0,
        anchor="nw",
        text="CONFIGURACIONES DE SISTEMA",
        fill="#000000",
        font=(sbtl_font)
    )

    canvas.create_text(
        114.0,
        441.0,
        anchor="nw",
        text="Ajuste en Formato de fecha",
        fill="#000000",
        font=(gnrl_font)
    )

    btn_fecha = Button(
        newWindow,
        image=on,
        bd=0,
        command=lambda: Switch("fecha"),
        bg="#FFFFFF",
        fg='#FFFFFF',
        width=22,
        height=12
    )
    btn_fecha.place(
        x=ajuste_x_btn,
        y=441
    )

    canvas.create_text(
        115.0,
        472.0,
        anchor="nw",
        text="Ajuste en Formato de numero",
        fill="#000000",
        font=(gnrl_font)
    )
    btn_fnumber = Button(
        newWindow,
        image=on,
        bd=0,
        command=lambda: Switch("fnumber"),
        bg="#FFFFFF",
        fg='#FFFFFF',
        width=22,
        height=12
    )
    btn_fnumber.place(
        x=ajuste_x_btn,
        y=472
    )

    canvas.create_text(
        114.0,
        508.0,
        anchor="nw",
        text="Ajuste en Lenguaje",
        fill="#000000",
        font=(gnrl_font)
    )

    btn_lenguaje = Button(
        newWindow,
        image=on,
        bd=0,
        command=lambda: Switch("lenguaje"),
        bg="#FFFFFF",
        fg='#FFFFFF',
        width=22,
        height=12
    )
    btn_lenguaje.place(
        x=ajuste_x_btn,
        y=508.0
    )

    canvas.create_text(
        114.0,
        542.0,
        anchor="nw",
        text="Ajuste en Formato No Wrap en WordPad",
        fill="#000000",
        font=(gnrl_font)
    )

    btn_wrap = Button(
        newWindow,
        image=on,
        bd=0,
        command=lambda: Switch("wrap"),
        bg="#FFFFFF",
        fg='#FFFFFF',
        width=22,
        height=12
    )
    btn_wrap.place(
        x=ajuste_x_btn,
        y=542
    )

    canvas.create_text(
        36.0,
        590.0,
        anchor="nw",
        text="ARCHIVOS A INSTALAR",
        fill="#000000",
        font=(sbtl_font)
    )

    canvas.create_text(
        114.0,
        624.0,
        anchor="nw",
        text="Instalar Web Client",
        fill="#000000",
        font=(gnrl_font)
    )

    btn_installWClient = Button(
        newWindow,
        image=on,
        bd=0,
        command=lambda: Switch("installWClient"),
        bg="#FFFFFF",
        fg='#FFFFFF',
        width=22,
        height=12
    )

    btn_installWClient.place(
        x=ajuste_x_btn,
        y=624
    )
    canvas.create_text(
        114.0,
        658.0,
        anchor="nw",
        text="Instalar LMS 12.2.prowcapc",
        fill="#000000",
        font=(gnrl_font)
    )

    btn_installLMS = Button(
        newWindow,
        image=on,
        bd=0,
        command=lambda: Switch("installLMS"),
        bg="#FFFFFF",
        fg='#FFFFFF',
        width=22,
        height=12
    )
    btn_installLMS.place(
        x=ajuste_x_btn,
        y=658
    )

    canvas.create_text(
        114.0,
        692.0,
        anchor="nw",
        text="Instalar WinSCP (Desde software center)",
        fill="#000000",
        font=(gnrl_font)
    )

    btn_installWinSCP = Button(
        newWindow,
        image=on,
        bd=0,
        command=lambda: Switch("installWinSCP"),
        bg="#FFFFFF",
        fg='#FFFFFF',
        width=22,
        height=12
    )

    btn_installWinSCP.place(
        x=ajuste_x_btn,
        y=692
    )
    
    
    canvas.create_text(
        114.0,
        726.0,
        anchor="nw",
        text="Agregar variable de entorno WinSCP",
        fill="#000000",
        font=(gnrl_font)
    )

    btn_pathWinSCP = Button(
        newWindow,
        image=on,
        bd=0,
        command=lambda: Switch("pathWinSCP"),
        bg="#FFFFFF",
        fg='#FFFFFF',
        width=22,
        height=12
    )

    btn_pathWinSCP.place(
        x=ajuste_x_btn,
        y=726
    )
    
    changeState(0)
    newWindow.mainloop()

# newWindow.resizable(False, False)
# newWindow.mainloop()
