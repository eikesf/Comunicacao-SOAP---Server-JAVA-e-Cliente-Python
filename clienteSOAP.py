#!/usr/bin/env python
# coding: utf-8

# In[1]:


from zeep import Client
import time


# In[2]:


class Recurso:
    pass

client = Client("http://localhost:8080/trabalho2/soap?wsdl")
    
#método responsável por chamar o método registrarInteresse presente no servidor JAVA
def registrarInteresse (recurso, idCliente):
    client.service.registrarInteresse(recurso,idCliente)

#método responsável por chamar o método sairSC presente no servidor JAVA
def sairSC(recurso,idCliente):
    client.service.sairSC(recurso,idCliente)
    

def notificar(recurso, idCliente):
    ########## RECURSO 1 ##########
    if(recurso == "Recurso1"):
       
        if("Released" == client.service.verEstadoRecurso("Recurso1")):
            print("*****************************************************************")
            print("O Recurso1 está sendo utlizado pelo cliente ",idCliente)
            print("*****************************************************************")

            #Verifica se o estado está como Held
        elif("Held" == client.service.verEstadoRecurso("Recurso1")):
           
            if( idCliente == client.service.verUtilizadorRecurso("Recurso1")):
                print("**************************************************************")
                print("O ",idCliente," está saindo da seção crítica e liberando o Recurso1")
                print("**************************************************************")
            else:
                print("**************************************************************")
                print("O ",idCliente," foi adicionado a fila para consumir o Recurso1 ")
                print("**************************************************************")
            
    ########## RECURSO 2 ########## 
    elif(recurso == "Recurso2"):
        
        if("Released" == client.service.verEstadoRecurso("Recurso2")):
            print("*****************************************************************")
            print("O Recurso2 está sendo utlizado pelo cliente ",idCliente)
            print("*****************************************************************")
            #Verifica se o estado está como Held
        
        elif("Held" == client.service.verEstadoRecurso("Recurso2")):
            
            if( idCliente == client.service.verUtilizadorRecurso("Recurso2")):
                print("**************************************************************")
                print("O ",idCliente," está saindo da seção crítica e liberando o Recurso2")
                print("**************************************************************")
            else:
                print("**************************************************************")
                print("O ",idCliente," foi adicionado a fila para consumir o Recurso2 ")
                print("**************************************************************")
                
                
#responsável por permitir ao cliente com que saia da fila caso não queira aguardar para utilizar o recurso

#Espera para utilizar o recurso
def waitR(recurso,idCliente):
    if("Held" == client.service.verEstadoRecurso("Recurso1") and idCliente != client.service.verUtilizadorRecurso("Recurso1")):
        print("**************************************************************")
        print("O ",idCliente," está aguardando para utilização do Recurso1")
        print("**************************************************************")
    
    elif("Held" == client.service.verEstadoRecurso("Recurso2") and idCliente != client.service.verUtilizadorRecurso("Recurso2")):
        print("**************************************************************")
        print("O ",idCliente," está aguardando para utilização do Recurso2")
        print("**************************************************************")


# In[3]:


def main():
    client = Client("http://localhost:8080/trabalho2/soap?wsdl")
 
    print("## SOAP INICIADO ##")
    #Cadastrar cliente através de um ID
    print("Digite o seu ID: ")
    idCliente = input("> ")
    
    
    while True:

        #Realizar verificação do estado dos recursos
        # Caso os dois recursos estejam livres
        if(("Released" == client.service.verEstadoRecurso("Recurso1")) and 
           ("Released" == client.service.verEstadoRecurso("Recurso2"))):

            print("\nDigite o número correspondente ao recurso desejado e tecle ENTER: ")
            print("1, para solicitar acesso ao Recurso1")
            print("2, para solicitar acesso ao Recurso2")
            print("3, para parar execução")
            print("_______________________")
            print("Recurso desejado: ")
            op = input("> ")

            
            if op == "1":
                notificar("Recurso1",idCliente)
                registrarInteresse("Recurso1",idCliente)
                
            elif op == "2":
                notificar("Recurso2",idCliente)
                registrarInteresse("Recurso2",idCliente)
                
             
            elif op == "3":
                print("Saindo do programa")
                break
            else:
                print("Opcao inválida!")
    
        #Caso recurso1 esteja ocupado e recurso2 esteja livre
        elif(("Held" == client.service.verEstadoRecurso("Recurso1")) and 
             ("Released" == client.service.verEstadoRecurso("Recurso2"))):
            
            if(idCliente != client.service.verUtilizadorRecurso("Recurso1")):
                print("\nDigite o número correspondente ao recurso desejado e tecle ENTER: ")
                print("1, para solicitar acesso ao Recurso1")
                print("2, para solicitar acesso ao Recurso2")
                print("3, para parar execução")
                print("_______________________")
                print("Recurso desejado: ")
                op = input("> ")

                if op == "1":
                    notificar("Recurso1",idCliente)
                    registrarInteresse("Recurso1",idCliente)

                elif op == "2":
                    notificar("Recurso2",idCliente)
                    registrarInteresse("Recurso2",idCliente)   

                elif op == "3":
                    print("Saindo do programa")
                    break

                else:
                    print("Opcao inválida!")
            
            else:
                print("\nDigite o número correspondente ao recurso desejado e tecle ENTER: ")
                print("1, para liberar acesso ao Recurso1")
                print("2, para solicitar acesso ao Recurso2")
                print("3, para parar execução")
                print("_______________________")
                print("Recurso desejado: ")
                op = input("> ")

                if op == "1":
                    notificar("Recurso1",idCliente)
                    sairSC("Recurso1",idCliente)

                elif op == "2":
                    notificar("Recurso2",idCliente)
                    registrarInteresse("Recurso2",idCliente)   

                elif op == "3":
                    print("Saindo do programa")
                    break

                else:
                    print("Opcao inválida!")
        
        #Caso recurso1 esteja livre e o recurso2 esteja ocupado
        elif(("Released" == client.service.verEstadoRecurso("Recurso1")) and 
             ("Held" == client.service.verEstadoRecurso("Recurso2"))):
            
            if(idCliente != client.service.verUtilizadorRecurso("Recurso2")):
                print("\nDigite o número correspondente ao recurso desejado e tecle ENTER: ")
                print("1, para solicitar acesso ao Recurso1")
                print("2, para solicitar acesso ao Recurso2")
                print("3, para parar execução")
                print("_______________________")
                print("Recurso desejado: ")
                op = input("> ")

                if op == "1":
                    notificar("Recurso1",idCliente)
                    registrarInteresse("Recurso1",idCliente)

                elif op == "2":
                    notificar("Recurso2",idCliente)
                    registrarInteresse("Recurso2",idCliente)

                elif op == "3":
                    print("Saindo do programa")
                    break
                else:
                    print("Opcao inválida!")
            
            else:
                print("\nDigite o número correspondente ao recurso desejado e tecle ENTER: ")
                print("1, para solicitar acesso ao Recurso1")
                print("2, para liberar acesso ao Recurso2")
                print("3, para parar execução")
                print("_______________________")
                print("Recurso desejado: ")
                op = input("> ")

                if op == "1":
                    notificar("Recurso1",idCliente)
                    registrarInteresse("Recurso1",idCliente)

                elif op == "2":
                    notificar("Recurso2",idCliente)
                    sairSC("Recurso2",idCliente)

                elif op == "3":
                    print("Saindo do programa")
                    break
                else:
                    print("Opcao inválida!")
                
        #Caso ambos os recursos estejam ocupados
        elif(("Held" == client.service.verEstadoRecurso("Recurso1")) and 
             ("Held" == client.service.verEstadoRecurso("Recurso2"))):
            
            if(idCliente != client.service.verUtilizadorRecurso("Recurso1") and 
               idCliente != client.service.verUtilizadorRecurso("Recurso2")):
                print("\nDigite o número correspondente ao recurso desejado e tecle ENTER: ")
                print("1, para aguardar acesso ao Recurso1")
                print("2, para aguardar acesso ao Recurso2")
                print("3, para parar execução")
                print("_______________________")
                print("Recurso desejado: ")
                op = input("> ")

                if op == "1":
                    notificar("Recurso1",idCliente)
                    registrarInteresse("Recurso1",idCliente)

                elif op == "2":
                    notificar("Recurso2",idCliente)
                    registrarInteresse("Recurso2",idCliente)

                elif op == "3":
                    print("Saindo do programa")
                    break
                else:
                    print("Opcao inválida!")
                    
                    
            elif(idCliente != client.service.verUtilizadorRecurso("Recurso1") and 
               idCliente == client.service.verUtilizadorRecurso("Recurso2")):
                print("\nDigite o número correspondente ao recurso desejado e tecle ENTER: ")
                print("1, para aguardar acesso ao Recurso1")
                print("2, para liberar acesso ao Recurso2")
                print("3, para parar execução")
                print("_______________________")
                print("Recurso desejado: ")
                op = input("> ")

                if op == "1":
                    notificar("Recurso1",idCliente)
                    registrarInteresse("Recurso1",idCliente)

                elif op == "2":
                    notificar("Recurso2",idCliente)
                    sairSC("Recurso2",idCliente)

                elif op == "3":
                    print("Saindo do programa")
                    break
                else:
                    print("Opcao inválida!")
                    
            elif(idCliente == client.service.verUtilizadorRecurso("Recurso1") and 
               idCliente != client.service.verUtilizadorRecurso("Recurso2")):
                print("\nDigite o número correspondente ao recurso desejado e tecle ENTER: ")
                print("1, para liberar acesso ao Recurso1")
                print("2, para aguardar acesso ao Recurso2")
                print("3, para parar execução")
                print("_______________________")
                print("Recurso desejado: ")
                op = input("> ")

                if op == "1":
                    notificar("Recurso1",idCliente)
                    sairSC("Recurso1",idCliente)

                elif op == "2":
                    notificar("Recurso2",idCliente)
                    registrarInteresse("Recurso2",idCliente)

                elif op == "3":
                    print("Saindo do programa")
                    break
                else:
                    print("Opcao inválida!")
                
            else:
                print("\nDigite o número correspondente ao recurso desejado e tecle ENTER: ")
                print("1, para liberar acesso ao Recurso1")
                print("2, para liberar acesso ao Recurso2")
                print("3, para parar execução")
                print("_______________________")
                print("Recurso desejado: ")
                op = input("> ")

                if op == "1":
                    notificar("Recurso1",idCliente)
                    sairSC("Recurso1",idCliente)

                elif op == "2":
                    notificar("Recurso2",idCliente)
                    sairSC("Recurso2",idCliente)

                elif op == "3":
                    print("Saindo do programa")
                    break
                else:
                    print("Opcao inválida!")
                
        

        #caso ambos os recursos estejam como wanted
        else:
            print("Aguardando liberação do Recurso1 e do Recurso2")
            time.sleep(3)

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




