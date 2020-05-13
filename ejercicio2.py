#!/usr/bin/python
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import sqlite3
from tkinter.filedialog import askopenfilename
##############################################
#B. DORTMUND 2 vs. 2 REAL MADRID 1
#SP. PORTUGAL 1 vs. 2 B. DORMUND 2

db_name = 'ERUBIANO1140882562-01.db'

def run_query(query,parametros=()):
    with sqlite3.connect(db_name) as conn:
        cursor=conn.cursor()
        resultado=cursor.execute(query, parametros)
        conn.commit()
    return resultado
    

def registrar():
    name = askopenfilename(title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")) )
    contador=0
    vector_liga=[]
    with open(name) as f:
        for line in f.readlines():
            print(line)
            codigos=line.upper()
            lista=codigos.split(" ")
            print(lista)
            if 'VS.' in lista:
                pos_vs=lista.index('VS.')
                pos_gole1=pos_vs-1
                pos_gole2=pos_vs+1
                #gol equipo 1
                golequipo1=lista[pos_gole1]
                #gol equipo 2
                golequipo2=lista[pos_gole2]  
                nom_e1=lista[:pos_gole1]
                nom_e1 = "".join(nom_e1)
                nom_e2=lista[pos_gole2+1:pos_gole2+3] 
                nom_e2 = "".join(nom_e2)
                print(nom_e1)
                print(nom_e2)
                print(golequipo1)
                print(golequipo2)
                fecha=lista[len(lista)-2]
                print(fecha)
            else:
                # ES una liga
                liga=lista[0]
                vector_liga.append( liga )

                print('Es una liga')
                print(liga)
    
            if "REAL" in line:
                print ("Encontrada")
                print (contador)

            if contador>=1:
                #ID le ponemos NULL (ID, equipo1,goles1,equipo2,goles2,fecha,liga)
                query= 'INSERT INTO EMRT_partidos VALUES (NULL,?,?,?,?,?,?)'
                parametros=(nom_e1,golequipo1,nom_e2,golequipo2,fecha,liga)
                run_query(query,parametros)
            #contador
            contador=contador+1
    #print ("Read Line: %s" % (r))
    f.close() #cerramos el archivo



    
    

        
        
    """
    # Limpiamos la pantalla
    tree.delete(*tree.get_children()) """



def calcular():
    #Garantizamos que la tabla este vacia
    records= tree.get_children()
    for elemento in records:
        tree.delete(elemento)

    
    #consultar datos
    query= 'SELECT * FROM EMRT_partidos ORDER BY equipo1 DESC'
    
    db_filas= run_query(query)
    print(db_filas)
    lis_nombre=[]
    lis_puntos=[]
    lis_liga=[]
    #insertamos el pedido en la tabla
    #tree.insert('',0, text= i[:], values=(p_base[:], p_total[:]))
    
    for row in db_filas:
        #tree.insert('', 0, text = row[1]+':  '+str(row[2])+'     vs.     '+row[3]+':  '+str(row[4]), values = row[6])
        #print(row[1])# nombre equipo
        #print(row[2])#goles
        #print(row[3])# nombre equipo
        #print(row[4])#goles
        #Hacemos un post
        
        
        #2  la poscion de puntos su nombre de equipo esta en la misma posicion de nombres
        i=0
        if row[2]> row[4]: #GANADORES
            if row[1] in lis_nombre:
                pos_nom=lis_nombre.index(row[1])
                lis_puntos[pos_nom] = lis_puntos[pos_nom] + 3
                #se agrega [nombre,liga]
                lis_liga.append( row[1] ) #nombre
                lis_liga.append( row[6] ) #liga
                
            else: 
                lis_nombre.append(row[1]) #lista de ganadores
                lis_puntos.append(3) #3 puntos

                #se agrega [nombre,liga]
                lis_liga.append( row[1] ) #nombre
                lis_liga.append( row[6] ) #liga

        elif row[2]< row[4]: #GANADORES
            if row[4] in lis_nombre:
                pos_nom=lis_nombre.index(row[4])
                lis_puntos[pos_nom] = lis_puntos[pos_nom] + 3
                #se agrega [nombre,liga]
                lis_liga.append( row[3] ) #nombre
                lis_liga.append( row[6] ) #liga
                
            else: 
                lis_nombre.append(row[3]) #lista de ganadores
                lis_puntos.append(3) #3 puntos

                lis_liga.append( row[3] ) #nombre
                lis_liga.append( row[6] ) #liga

        elif row[2]== row[4]: #EMPATE    
            if row[1] in lis_nombre :
                pos_nom=lis_nombre.index(row[1])
                lis_puntos[pos_nom] = lis_puntos[pos_nom] + 1
                lis_liga.append( row[1] )
                lis_liga.append( row[6] )
            else:
                lis_nombre.append(row[1]) #lista de ganadores
                lis_puntos.append(1) #3 puntos
                lis_liga.append( row[1] )
                lis_liga.append( row[6] )

            if row[3] in lis_nombre: 
                pos_nom=lis_nombre.index(row[3])
                lis_puntos[pos_nom] = lis_puntos[pos_nom] + 1
                lis_liga.append( row[3] )
                lis_liga.append( row[6] )
            else:
                lis_nombre.append(row[3]) #lista de ganadores
                lis_puntos.append(1) #3 puntos
                lis_liga.append( row[3] )
                lis_liga.append( row[6] )

        #print(lis_nombre)
        #print(lis_puntos)
        #print(lis_liga)
        print(type(lis_nombre[i]))
        print(lis_nombre[i])

        nombreEquipo=lis_nombre[i]
        puntosEquipo= lis_puntos[i]
        print(type(puntosEquipo))
        #puntosEquipo= ''.join(puntosEquipo)
        #puntosEquipo= int(puntosEquipo) # converting list into string
        ligaEquipo=lis_liga[i+1]
        print(type(ligaEquipo))
        print(ligaEquipo)


        #ID le ponemos NULL (ID, pedido,precio base,precio total,fecha)
        #query= 'INSERT INTO EMRT_puntos VALUES (NULL,?,?,?)'
        #parametros=(nombreEquipo,puntosEquipo,ligaEquipo)
        #run_query(query,parametros)
        # Contador del ciclo
        i=i+1 





def buscar():

    #Garantizamos que la tabla este vacia
    records= tree.get_children()
    for elemento in records:
        tree.delete(elemento)

    print(entrada.get())
    if entrada.get() == '*':
        #consultar datos
        query= 'SELECT * FROM EMRT_partidos ORDER BY equipo1 DESC'
        
        db_filas= run_query(query)
        print(db_filas)
        #insertamos el pedido en la tabla
        #tree.insert('',0, text= i[:], values=(p_base[:], p_total[:]))
       
        for row in db_filas:
            tree.insert('', 0, text = row[1]+':  '+str(row[2])+'     vs.     '+row[3]+':  '+str(row[4]), values = row[6])


#########################################################
# Construyendo la ventana
ventana = Tk()
ventana.title("Registro de partidos de futbol") #Titulo de la ventana
# Dimencion de la ventana
ventana.geometry("620x450+0+0")

# CREAMOS LOS OBJECTOS


# TABLA


tree = ttk.Treeview(height =14,columns = ("#0","#1"))
tree.column("#0", width = 300) 
tree.column("#1", width = 300)
tree.place(x=7, y=90)
tree.heading('#0', text = 'Equipo(s)', anchor = CENTER)
tree.heading('#1', text = 'Liga', anchor = CENTER)

 #minwidth=270, stretch=tk.NO
# scrollbars
vsb = Scrollbar( orient="vertical", command=tree.yview)
vsb.place(relx=0.978, rely=0.175, relheight=0.713, relwidth=0.020)
tree.configure(yscrollcommand=vsb.set)

""" frame1 = tk.Frame(root)
frame1.place(x=7, y=140)
tree = ttk.Treeview(frame1) """

#leftframe = ttk.Frame(ventana, width=100, height=300, pad=10)
#leftframe = ttk.Frame(ventana)

""" tree = ttk.Treeview(ttk.Frame(ventana))
tree.place(x=7, y=180)
tree.heading('#0', text = 'Pedido', anchor = CENTER)
tree.heading('#1', text = 'Precio Base', anchor = CENTER) """
#tree.heading('#2', text = 'Precio Total', anchor = CENTER)

# attach a scrollbar to the frame
""" treeScroll = ttk.Scrollbar(leftframe)
treeScroll.configure(command=tree.yview)
tree.configure(yscrollcommand=treeScroll.set) """

""" frame1 = ttk.Frame(ventana)
frame1.place(x=7, y=140)

tree = ttk.Treeview(frame1)


tree.heading("#0", text="Name", anchor=CENTER)
tree.heading("C1", text="Type", anchor=CENTER)
tree.heading("C2", text="Index", anchor=CENTER)
print(tree["columns"]) """

# BOTONES
B_registrar=Button(ventana, text=" Registrar partidos",command=registrar).place(x=490, y=410)
B_buscar=Button(ventana, text=" Buscar ", command=buscar).place(x=510, y=45)
B_calcular=Button(ventana, text=" Calcular Posicion", command=calcular ).place(x=360, y=410)

# ENTRIYS

entrada = StringVar()
codigo= Entry(ventana, textvariable=entrada,  width= 58).place(x=10, y=45)
#codigo.focus_set()  # cursor parpadeando
entrada.set("Nombre de Equipo,Nombre Liga, Resultados Liga, Fecha Liga, todas *")


# LABELS
l_code=Label(ventana, text="Ingresa solo un parametro para filtrar la busqueda:").place(x=10, y=10)






#########################################################
ventana.resizable(False, False)
ventana.mainloop()
