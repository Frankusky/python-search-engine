#coding: utf-8
import time #impor time nos dara un timeo o una pausa
import urllib2 # urllib2 para la interacción con URLs
import re #reemplazo múltiple de cadenas
import os
class conexion(object): #clase conexion
	print """
 ______  _                             _     _            
(____  \(_)                           (_)   | |           
 ____)  )_  ____ ____ _   _ ____ ____  _  _ | | ___   ___ 
|  __  (| |/ _  )  _ \ | | / _  )  _ \| |/ || |/ _ \ /___)
| |__)  ) ( (/ /| | | \ V ( (/ /| | | | ( (_| | |_| |___ |
|______/|_|\____)_| |_|\_/ \____)_| |_|_|\____|\___/(___/ 
                                                          

"""
	time.sleep(2)
	print """
                                                 _        
                                                | |       
  _ __  _ __ ___ _ __   __ _ _ __ __ _ _ __   __| | ___   
 | '_ \| '__/ _ \ '_ \ / _` | '__/ _` | '_ \ / _` |/ _ \  
 | |_) | | |  __/ |_) | (_| | | | (_| | | | | (_| | (_) | 
 | .__/|_|  \___| .__/ \__,_|_|  \__,_|_| |_|\__,_|\___/  
 | |   | |      | |                                       
 |_|___| |      |_|                                       
   / _ \ |          _                   _                 
  |  __/ |         | |                 | |                
   \___|_|__   ___ | |_ ___  _ __    __| | ___            
   | '_ ` _ \ / _ \| __/ _ \| '__|  / _` |/ _ \           
   | | | | | | (_) | || (_) | |    | (_| |  __/           
   |_| |_| |_|\___/ \__\___/|_|     \__,_|\___|           
    | |                                  | |              
    | |__  _   _ ___  __ _ _   _  ___  __| | __ _         
    | '_ \| | | / __|/ _` | | | |/ _ \/ _` |/ _` |        
    | |_) | |_| \__ \ (_| | |_| |  __/ (_| | (_| |        
    |_.__/ \__,_|___/\__, |\__,_|\___|\__,_|\__,_|        
                        | |                               
                        |_|                               


"""
	time.sleep(1) #me dara una pequena pausa 
	print "Listo para comenzar......."
	time.sleep(2)
	os.system("clear") #me limpiara mi pantalla la funcin cls camabiara segun el ordenador si es ubutu sera clear en ves de cls esto le concierne a windows
	def contar(self):#mi funcion que correra y buscara lo que desea el usuario
		self.link = raw_input("Ingrese pagina: \n")
		self.link2 = raw_input("Ingrese  la segunda pagina: \n")
		os.system("clear") 
		self.palabra = str(raw_input("Palabra que desea buscar: \n" ))
	
		if self.link[0:4] != 'http' or self.link2[0:4] != 'http': #verificara si es diferente para ayudar al usario un poco al ingreso de las url
			self.link = 'http://' + self.link #aqui si nuestra url no tiene http se la agregara 
			self.link2 = 'http://' + self.link2
		try:# intentra verificar si la url es valida
			f = urllib2.urlopen(self.link)      #abrira nuestro url      
			myfile = f.read()  #aqui leera nuestra url 
			f2 = urllib2.urlopen(self.link2)           
			myfile2 = f2.read()
			if len(re.findall(self.palabra, myfile)) == 0:# verificara y buacara la palabra y si esta basia 
				print "La palabra que desea buscar no esta en la pagina que ingreso"
			else:
				print "\nLa palabra que se encontraron en la primera pagina  son de: ", len(re.findall(self.palabra, myfile))
				print "\nLa palabra que se encontraron en la segunda pagina son de:", len(re.findall(self.palabra, myfile2))
				print  "Gracis por usar nuestro motor de Busqueda"
		except urllib2.URLError as e:
			print e.reason
			print "Verifique sus urls no es una url Valida"
			self.contar() #si no es vlaida nos regrera de nuevo a comenzar a nuesta funcion 

busca1 = conexion()
busca1.contar()


