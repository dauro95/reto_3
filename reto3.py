cinco = diez= veinte= cinq= cien= dosc= quin = 0

menu_num_plato =[1,2,3]
menu_des_plato =["macarrones","cocido","judias"]
menu_precio_plato =[555,1005,350]

menu_dic_platos= {}
menu_dic_precios = {}
# menu_dic = dict(macarrones= 500,cocido= 1000,judias= 5000)

#funcion para carga de diccionario con menu y precio
def carga_dic(list_a, list_b):
  dic= {}
  i = 0
  for a in list_a:
    dic[a] = list_b[i]
    i = i + 1
  return dic

#visualiza el menu
def mostrar_menu (dic_a,dic_b):
  print ('el menu de hoy es /n')
  for clave in dic_a.keys():
    print (str(clave)  + " plato:" + str(dic_a[clave])+ " precio:" + str(dic_b[clave]))


#selección de menu
def selecionar_menu():
  cargar_menu = 1
  lista_menu = []

  print ("vamos a cargar menu")

  while cargar_menu == 1 :
    
    num=int(input("introduce un numero de plato: "))
    
    if num>=1 and num<=3:  
      lista_menu.append (num)
    else:
      print("el numero selecionado no es valio")
    
    cargar_menu = int(input("quieres otro plato?: (1 si 0 no)"))
  
  return(lista_menu)

# calculo billetes
def caclulo_billete (coste,cinco,diez,veinte,cinq,cien,dosc,quin):
  while coste >= 5:
    if coste >= 500:
        quin = int(coste // 500)
        coste = coste % 500 
    elif coste >= 200:
      dosc = int(coste // 200)
      coste = int(coste % 200 )
    elif coste >= 100:
        cien=int(coste//100)
        coste=coste % 100
    elif coste >= 50:
        cinq=int(coste//50)
        coste=coste % 50
    elif coste >= 20:
        veinte=int(coste//20)
        coste=coste % 20
    elif coste >= 10:
        diez=int(coste//10)
        coste=coste % 10
    elif coste >= 5:
        cinco=int(coste//5)
        coste=coste % 5

  print (" billentes 500: "+ str(quin)+ "\n billentes 200: " + str(dosc) + "\n billentes de cien: " + str(cien) + "\n billenetes 50" + str(cinq)+ "\n billentes veinte: " +str(veinte)+"\n billetes 10: " +str(diez) + "\n billetes cinco: " +str (cinco))


menu_dic_platos =carga_dic(menu_num_plato,menu_des_plato)
menu_dic_precios=carga_dic(menu_num_plato,menu_precio_plato)

mostrar_menu(menu_dic_platos,menu_dic_precios)
lista_menu = selecionar_menu()

coste = 0

for item in lista_menu:
  coste=coste + menu_dic_precios[item]

print("tu cuenta asciende a: " + str(coste))

caclulo_billete(coste,cinco,diez,veinte,cinq,cien,dosc,quin)








