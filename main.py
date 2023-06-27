import os
import json

# init function
def get_json_data(file_name):
    with open(file_name) as file:
        data = json.load(file)
        return data
# end function
#
# init function
def save_workers_json_data():
    with open('workers.json', 'w') as file:
        json.dump(worker_list, file)
# end function
#
# init function
def main_menu():
    os.system('clear')
    option = input(''' MENU PRINCIPAL ingrese un número:
                        [1] Gestion de trabajadores
                        [2] Reportes
                        [3] Salir
                        
                        Ingrese numero:''')

    if option == "1":
        management_workers_menu()
    elif option == "2":
        reports_workers_menu()
    else:
        print("Usted salio del sistema")
# end function
#
# init function
def management_workers_menu():
    os.system('clear')
    option = input(''' MENU TRABAJADORES
                        [1] Ingrese nuevo trabajador
                        [2] Modificar dato de trabajador
                        [3] Eliminar trabajador
                        [4] Volver

                        Ingrese numero:''')
    if option == "1":
        save_worker()
    elif option == "2": 
        set_worker_document("modificar")
    elif option == "3":
        delete_worker()
    elif option == "4":
        main_menu()
    else:
        print("Usted salio del sistema")
# end function
#
# init function
def reports_workers_menu():
    os.system('clear')
    option = input(''' MENU REPORTES
                        [1] Ver informacion de un trabajador segun DNI
                        [2] Mostrar trabajadores inactivos
                        [3] Mostrar trabajadores activos
                        [4] Mostrar trabajador segun profesion
                        [5] Lista de trabajadores
                        [6] Menu principal

                        Ingrese numero:''')
    if option == "1":
        set_worker_document("ver")
    elif option == "2": 
        worker_list_by_status("inactivos")
    elif option == "3": 
        worker_list_by_status("activos")
    elif option == "4":
        choose_profession_menu()
    elif option == "5":
        get_worker_list()
    elif option == "6":
        main_menu()
    else:
        print("Usted salio del sistema")
# end function
#
# init function
def save_worker():
    os.system('clear')
    document = input("ingrese DNI:")
    nombre = input("ingrese Nombre y Apellido:")
    edad = input("ingrese edad:")

    profesion = show_professions_and_get_one_menu()

    status = input('''ingrese estado:
                        [0] Inactivo
                        [1] Activo

                        Ingrese opcion:''')

    worker_list[document] = [nombre, edad, profesion, status]
    save_workers_json_data()
    management_workers_menu()
# end function
#
# init function
def set_worker_document(accion):
    os.system('clear')
    document = input("Ingrese DNI trabajador:")

    if document in worker_list:
        if accion == "modificar":
            modify_worker_menu(document)
        elif accion == "ver":
            show_worker_data(document)
    else:
        print(f"El trabajador con DNI {document} no existe.")
        show_sub_menu()

# end function
#
# init function
def modify_worker_menu(worker_document):
    os.system('clear')
    option = input(''' MENU MODIFICAR DATOS TRABAJADOR
                        [1] Modificar nombre y aplellido
                        [2] Modificar edad
                        [3] Modificar profesion
                        [4] Modificar estado (activo / inactivo)

                        Ingrese numero:''')
    if option == "1":
        nombre = input("Ingrese Nombre y apellido:")
        worker_list[worker_document][0] = nombre
    elif option == "2":
        edad = input("Ingrese Edad:")
        worker_list[worker_document][1] = edad
    elif option == "3":
        profession = show_professions_and_get_one_menu()
        worker_list[worker_document][2] = profession
    elif option == "4":
        status = input('''ingrese estado:
                            [0] Inactivo
                            [1] Activo

                            Ingrese opcion:''')
        worker_list[worker_document][3] = status
    
    save_workers_json_data()
    main_menu()
# end function
#
# init function
def get_worker_list():
    os.system('clear')
    for document, worker in worker_list.items():
        print_worker(document, worker)
        print("_____________________________________")

    show_sub_menu()
# end function
#
# init function
def show_worker_data(document):
    os.system('clear')
    worker = worker_list[document]
    print_worker(document, worker)

    show_sub_menu()
# end function
#
# init function
def worker_list_by_status(status):
    os.system('clear')
    if status == "inactivos":
        for document, worker in worker_list.items():
            if worker[3] == "0":
                print_worker(document, worker)
                print("_______________________")

    elif status == "activos":
        for document, worker in worker_list.items():
            if worker[3] == "1":
                print_worker(document, worker)
                print("_______________________")

    show_sub_menu()
# end function
#
# init function
def choose_profession_menu():

    os.system('clear')

    profession = show_professions_and_get_one_menu()
    if profession == "0":
        main_menu()
    else:
        for document, worker in worker_list.items():
            if worker[2] == profession:
                print_worker(document, worker)
                print("_______________________")

    show_sub_menu()
# end function
#
# init function
def delete_worker():

    document = input("Ingrese numero DNI:")

    if document in worker_list:
        del worker_list[document]
        save_workers_json_data()

    else:
        print(f"El trabajador con DNI {document} no existe.")
    show_sub_menu()
# end function
#
# init function
def show_sub_menu():

    option = input(''' ELIJA OPCIOM
                        [1] Menu principal
                        [2] Gestion de trabajadores
                        [3] Reportes
                        [4] Salir
                        Ingrese numero:''')

    if option == "1":
        main_menu()
    elif option == "2": 
        management_workers_menu()
    elif option == "3":
        reports_workers_menu()
    else:
        print("Usted salio del sistema")
# end function
#
# init function
def show_professions_and_get_one_menu():

    for index, profession in professions.items():
        print(f"[{index}] {profession}")
    profession = input("Ingrese numero de profesion:")
    return profession
# end function
#
# init function
def print_worker(document, worker):
        print("DNI: ", document)
        print("Nombre: ", worker[0])
        print("Edad: ", worker[1])
        print("Profesion: ", professions[worker[2]])
        if worker[3] == "1":
            print("Estado: Activo")
        else:
            print("Estado: Inactivo")
# end function
professions = get_json_data("professions.json")
worker_list = get_json_data("workers.json")
main_menu()