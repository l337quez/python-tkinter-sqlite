#!/usr/bin/python
#PA400x400(O3M3S4R1B1)
from tkinter import ttk
from tkinter import *
import sqlite3
import time
##############################################


db_name = 'ERUBIANO1140882562-01.db'

# FUNCIONES

def get_productos(lis_cant_inmuebles,area):

    #Garantizamos que la tabla este vacia
    """     records= tree.get_children()
    for elemento in records:
        tree.delete(elemento) """

    #consultar datos
    query= 'SELECT * FROM EMRT_precios ORDER BY nombre DESC'
    db_filas= run_query(query)
    
    #rellenar datos
    for fila in db_filas:
        #tree.insert('',0, text= fila[1], values=fila[2])
        if fila[1]== 'proyecto':
            proyecto=fila[2] #precio de proyecto
        elif fila[1]== 'mesa': 
            mesa=fila[2]
        elif fila[1]== 'silla': 
            silla=fila[2]
        elif fila[1]== 'repisa': 
            repisa=fila[2]
        elif fila[1]== 'tapete': 
            tapete=fila[2]
        elif fila[1]== 'archivador': 
            archivador=fila[2]
        elif fila[1]== 'biblioteca': 
            biblioteca=fila[2]
        elif fila[1]== 'papelera': 
            papelera=fila[2]
        elif fila[1]== 'oficina': 
            oficina=fila[2]
            print('oficinaaaaaaaaa')
            print(oficina)

    #  lis_cant_inmuebles  [O,M,S,R,T,P,A,B]
    MESA= float(lis_cant_inmuebles[1])*mesa
    SILLA= float(lis_cant_inmuebles[2])*silla
    REPISA=float(lis_cant_inmuebles[3])*repisa
    TAPETE=float(lis_cant_inmuebles[4])*tapete
    PAPELERA=float(lis_cant_inmuebles[5])*papelera
    ARCHIVADOR=float(lis_cant_inmuebles[6])*archivador
    BIBLIOTECAS=float(lis_cant_inmuebles[7])*biblioteca

    valor_inmuebles= MESA+SILLA+REPISA+TAPETE+PAPELERA+ARCHIVADOR+BIBLIOTECAS


    print(type(area))
    print(type(proyecto))
    print(type(oficina))
    print(type(lis_cant_inmuebles[0]))

    Precio_base= float(area)*proyecto+oficina*float(lis_cant_inmuebles[0])
    print(Precio_base)
    Precio_base=str(Precio_base)
    #insertamos el pedido en la tabla
    #tree.insert( values= Precio_base)
    return Precio_base,valor_inmuebles  
    

 

def run_query(query,parametros=()):
    with sqlite3.connect(db_name) as conn:
        cursor=conn.cursor()
        resultado=cursor.execute(query, parametros)
        conn.commit()
    return resultado

# Funcion para guardar los resultados
def post():
    for Parent in tree.get_children():
        print(tree.item(Parent)["values"])
        print(tree.item(Parent)["text"])
        ## representacion de fecha y hora
        print (time.strftime("%c"))
    #ID le ponemos NULL (ID, pedido,precio base,precio total,fecha)
    query= 'INSERT INTO EMRT_guardarProductos VALUES (NULL,?,?,?,?)'
    parametros=(tree.item(Parent)["text"],tree.item(Parent)["values"][0],tree.item(Parent)["values"][1],time.strftime("%c"))
    run_query(query,parametros)
    """ for child in tree.get_children(Parent):
        data = tree.item(child)["text"]
        print(data) """
    # Limpiamos la pantalla
    tree.delete(*tree.get_children())

def clear ():
    # Limpiamos la pantalla
    tree.delete(*tree.get_children())


#Funcion de inicio de botones, labels etc.. deshabilitados
def calcular ():
    #self.B_guardar.configure(state=NORMAL)
    #B_guardar.configure(state="normal")
    #B_guardar.configure(['active'])  
    #B_guardar["state"] = NORMAL
    #B_guardar.set(state='enable')
    #B_guardar["text"] = "enable"
    #B_guardar.configure(state='enable')
    ban=False #bandera
    codigos= code.get()
    codigos=codigos.upper()
    concurrencias=codigos.count(';')
    lista_codigos=codigos.split(';')
    n_pedidos=concurrencias+1
    
    #isdigit()
    print(len(codigos))
    print(codigos[1])
    print(list(codigos))
    
    #[O,M,S,R,T,P,A,B] 
    lis_cant_inmuebles= [0,0,0,0,0,0,0,0]
    for i in lista_codigos:
        print("TIPOOOOOOOOOOOO")
        print(type(i))
        pos_a=i.index('A')
        pos_x=i.index('X')
        pos_pa=i.index('(')
        ancho=i[pos_a+1:pos_x]
        alto=i[pos_x+1:pos_pa]      
        area=int(ancho)*int(alto)


        ban=False
        ban_letra=False
        for j in list(i):
            print(j)
            digit=j.isdigit()
            if j=='(' or ban==True:
                ban=True
                if digit==False: #no es numero
                    print('es false')
                    print(j)
                    #print(i.index(j))
                    print('el check ofisinaaaaa')
                    print(oficina.get())
                    if j == 'O' :
                        k=0
                        ban_letra=True
                    elif j == 'M' and mesa.get()==True:
                        k=1
                        ban_letra=True
                    elif j == 'S' and silla.get()==True:
                        k=2
                        ban_letra=True
                    elif j == 'R' and repisa.get()==True:
                        k=3
                        ban_letra=True
                    elif j == 'T' and tapete.get()==True:
                        k=4
                        ban_letra=True
                    elif j == 'P' and papelera.get()==True:
                        k=5
                        ban_letra=True
                    elif j == 'A' and archivador.get()==True:
                        k=6
                        ban_letra=True
                    elif j == 'B' and biblioteca.get()==True:
                        k=7
                        ban_letra=True

                elif j != ')' and digit==True:
                    #lis_cant_inmuebles.append(j)
                    if ban_letra==True:
                        lis_cant_inmuebles[k]=j
                        ban_letra=False
        #llamamos la funcion get para mostrar el valor BASE
        p_base,valor_inmuebles =get_productos(lis_cant_inmuebles,area)
        p_total=str(float(p_base) + valor_inmuebles)
        print('totaaaaaal')
        print(p_total)
        print('baseeeee')
        print(p_base)
        #insertamos el pedido en la tabla
        tree.insert('',0, text= i[:], values=(p_base[:], p_total[:]))
    #tree.insert( '',0, text= i[:])

            
"""     print('la listaaa')
    print(lis_cant_inmuebles)
    get_productos(lis_cant_inmuebles,area) """
    
#






   
    

""" 
list_tc=Listbox(pestana0,width= 14, height=2)
list_tc.insert(0,"Ceramic")
list_tc.insert(1,"Polyester")
list_tc.insert(2,"Tamtalio")
list_tc.insert(3,"Electrolityc")
list_tc.insert(4,"Mica")
list_tc.insert(4,"Polypropylene")
list_tc.place(x=10, y=62.5)
#barra de scroll para el listbox
scrollbar_list_tc= Scrollbar(pestana0, width= 12.5, orient="vertical")
scrollbar_list_tc.config(command=list_tc.yview)
scrollbar_list_tc.place(x=110.3, y=64.9)
list_tc.config(yscrollcommand=scrollbar_list_tc.set)
list_tc.select_set(0)
 """

"""     for i in lista_codigos:
        for j in list(codigos):
            print(j)
            digit=j.isdigit()
            if j=='(' or ban==True:
                ban=True
                if digit==False:
                    print(i.index(j))
                 """
    
#     for i in lista_codigos:
#         print(i)
    
#     pos_p=codigos.index('P')
#     pos_p=codigos.index('A')
#     pos_p=codigos.rindex('M')
#     pos_p=codigos.rindex('S')
#     pos_p=codigos.rindex('R')
#     pos_p=codigos.rindex('T')
#     pos_p=codigos.rindex('P')
#     pos_p=codigos.rindex('A')
#     pos_p=codigos.rindex('B')
#     pos_p=codigos.rindex('(')
#     pos_p=codigos.rindex(')')
#     pos_p=codigos.rindex('x')

    
    #print(lista_codigos)
"""     print(concurrencias)
    print(codigos)"""
    



#########################################################
# Construyendo la ventana
ventana = Tk()
ventana.title("Cotizador de Construcion de Oficinas") #Titulo de la ventana
# style = Style(ventana)
# style.theme_use("clam")
# Dimencion de la ventana
ventana.geometry("620x450+0+0")


# CREAMOS LOS OBJECTOS

tree = ttk.Treeview(height =7, columns = ("#0","#1"))
tree.place(x=7, y=180)
tree.heading('#0', text = 'Pedido', anchor = CENTER)
tree.heading('#1', text = 'Precio Base', anchor = CENTER)
tree.heading('#2', text = 'Precio Total', anchor = CENTER)

# scrollbars
vsb = Scrollbar( orient="vertical", command=tree.yview)
vsb.place(relx=0.978, rely=0.175, relheight=0.713, relwidth=0.020)
tree.configure(yscrollcommand=vsb.set)


# BOTONES
#Boton_Conectar= Button(ventana, text= "Conectar",command=port).place(x=10, y=60)
#Boton_buscar_HEX=Button(ventana, text = "Buscar .HEX",command=buscar_HEX, state='disabled').place(x=97, y=132)
# frame_programar = tk.Frame(ventana)
B_calcular=Button(ventana, text=" Calcular ",command=calcular).place(x=460, y=410)
B_guardar=Button(ventana, text=" Guardar ", command=post).place(x=540, y=410)
B_clear=Button(ventana, text=" Limpiar ", command=clear).place(x=380, y=410)


# ENTRIYS
code = StringVar()
codigo= Entry(ventana, textvariable=code,  width= 99).place(x=10, y=45)
#codigo.focus_set()  # cursor parpadeando
code.set("Ingrese el codigo")

# Tabla de entry
""" pedido = StringVar()
entry_pedido=Entry(ventana, textvariable=pedido, width= 25, background='blue', state='disabled').place(x=10, y=180)
pedido.set("Pedido")

p_base = StringVar()
entry_p_base=Entry(ventana, textvariable=p_base, width= 25, state='disabled').place(x=170, y=180)
p_base.set("Precio Base")

total = StringVar()
entry_total=Entry(ventana, textvariable=total, width= 25, state='disabled').place(x=330, y=180)
total.set("Total") """

# CHECKBUTTON

#Checkbutton(root, text="Con leche", variable=leche, 
            #onvalue=1, offvalue=0).place(x=10, y=39)

oficina=BooleanVar()
mesa=BooleanVar()
silla=BooleanVar()
repisa=BooleanVar()
tapete=BooleanVar()
archivador=BooleanVar()
papelera=BooleanVar()
biblioteca=BooleanVar()

""" Checkbutton(ventana, text="oficinas",  
            onvalue=1, offvalue=0, variable=oficina).place(x=40, y=100) """
Checkbutton(ventana, text="mesas",  
            onvalue=1, offvalue=0, variable=mesa).place(x=40, y=100)
Checkbutton(ventana, text="sillas",  
            onvalue=1, offvalue=0, variable=silla).place(x=40, y=120)
Checkbutton(ventana, text="repisas",  
            onvalue=1, offvalue=0, variable=repisa).place(x=40, y=140)
Checkbutton(ventana, text="tapetes",  
            onvalue=1, offvalue=0, variable=tapete).place(x=270, y=100)
Checkbutton(ventana, text="papeleras",  
            onvalue=1, offvalue=0, variable=papelera).place(x=270, y=120)
Checkbutton(ventana, text="archivadores",  
            onvalue=1, offvalue=0, variable=archivador).place(x=270, y=140)
Checkbutton(ventana, text="bibliotecas",  
            onvalue=1, offvalue=0, variable=biblioteca).place(x=480, y=100)


# LABELS

l_code=Label(ventana, text="Codigo de cotizacion:").place(x=10, y=20)
#l_cbase=Label(ventana, text="Costo base:").place(x=10, y=180)
#l_total=Label(ventana, text="Total:").place(x=10, y=200)
#l_error=Label(ventana, text="Advertencia:", fg='red').place(x=10, y=350)
#label=Label(ventana, text="   nn    ").place(x=590, y=155)





#########################################################
ventana.resizable(False, False)
ventana.mainloop()
