# Librerias a utilizar
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.font import Font
from instalacion import createView

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# -----------------------> FUNCIONES <-----------------------


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def installLMS():
    createView(root)
    print("INSTALACION")


def confDRP():
    print("DRP")


def resetLMS():
    print("RESET LMS")


# -----------------------> VENTANA PRINCIPAL <-----------------------
# Declaracion de la ventana
root = Tk()
# Medidas y color de la ventana
alto = 700
ancho = 980

x_ventana = root.winfo_screenwidth() // 2 - ancho // 2
y_ventana = root.winfo_screenheight() // 2 - alto // 2
posicion = str(ancho) + "x" + str(alto) + \
    "+" + str(x_ventana) + "+" + str(y_ventana)
root.geometry(posicion)
root.configure(bg="#FFFFFF")

# Fuente a utilizar
f_font = "Arial Nova"
btn_font = Font(family=f_font, size=14)

# Fondo blanco de la ventana en general
canvas = Canvas(
    root,
    bg="#FFFFFF",
    height=alto,
    width=ancho,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)


# Imagen superior de LEAR
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    526.0,
    90.0,
    image=image_image_1
)

# Titulo CONFIGURACION LMS de la ventana
canvas.create_text(
    550.0,
    190.0,
    anchor="nw",
    text="CONFIGURACION LMS",
    fill="#000000",
    font=(f_font, 36 * -1)
)


# Boton de INSTALACION
btn_install = Button(
    text="INSTALACION",
    borderwidth=0,
    highlightthickness=0,
    command=installLMS,
    relief="flat",
    font=btn_font,
    bg="#C13737",
    fg='#FFFFFF'
)
btn_install.place(
    x=ancho-390,
    y=300.0,
    width=300.0,
    height=43.0
)


# Boton de RESET LMS
btn_reset = Button(
    text="RESET LMS",
    borderwidth=0,
    highlightthickness=0,
    command=resetLMS,
    relief="flat",
    font=btn_font,
    background="#C13737",
    fg='#FFFFFF'
)
btn_reset.place(
    x=ancho-390,
    y=400,
    width=300.0,
    height=43.0
)

# Boton de CONFIGURACION DRP
btn_drp = Button(
    text="CONFIGURACION DRP",
    borderwidth=0,
    highlightthickness=0,
    command=confDRP,
    relief="flat",
    font=btn_font,
    background="#C13737",
    fg='#FFFFFF'
)
btn_drp.place(
    x=ancho-390,
    y=500.0,
    width=300.0,
    height=43.0
)

# LADO ROJO DE LA VENTANA PRINCIPAL
canvas.create_rectangle(
    0.0,
    0.0,
    ancho/2,
    alto,
    fill="#B70000",
    outline="")
# Texto dentro del rectangulo rojo
canvas.create_text(
    50.0,
    alto/2.2,
    anchor="nw",
    text="Instalacion, configuracion y administracion\n"
        +"de servidor, software y re-establecimiento \n"
        +"del software LMS 12.2",
    fill="white",
    font=(f_font, 20 * -1)
)

# Se desactiva el ajuste del tamaño de la ventana
root.resizable(False, False)

# Se ejecuta y abre la ventana
root.mainloop()
