#ALGORITMO PARA RESERVA DE LOCAL
#NÃO TEM INTERFACE GRAFICA
import pyodbc



def CadastrarHorario():  #função em que o adm cadastra o horario no local
    conexaodb = pyodbc.connect("Driver={SQLite3 ODBC Driver};Server=localhost;Database=TabelaHorario.db")

    cursor = conexaodb.cursor()

    print("Insira seu nome:")
    newnome = input()

    print("Insira seu CPF:")
    newcpf = input()

    print("Insira Data:(formato: DD/MM/AAAA)")
    newdata = input()
    
    try:
        #verificando formato da data
        dia, mes, ano = map(int, newdata.split('/'))
    except ValueError:
        print("digite em formato valido")
    
    
    print("Insira Hora Inicial:(formato: 00:00)")
    newhora_inicial = input()
    print("Insira Hora Final:(formato: 00:00)")
    newhora_final = input()
    
    try:
        #verificando formato da hora
        horas, minutos = map(int, newhora_inicial.split(':'))
        horas2, minutos2 = map(int, newhora_final.split(':'))
    
    # checa se o tempo esta entre 9 e 23(os dois horarios digitados)
        if 9 <= horas <= 23 and 0 <= minutos <= 59:
            if 9 <= horas2 <= 23 and 0 <= minutos2 <= 59:
                #caso esteja dentro do intervalo, verificando se o horario esta disponivel:
                cursor.execute("SELECT * FROM HorariosReserva WHERE data = ? and (hora_inicial >= ? and hora_inicial <= ?) or (hora_inicial <= ? and hora_final >= ?)", (newdata,newhora_inicial,newhora_final, newhora_inicial,newhora_inicial))
                dataantiga = cursor.fetchall() 
                if dataantiga:
                    print("estes horarios ja estao reservados")
            
                else:
                    cursor.execute("INSERT INTO HorariosReserva (data,hora_inicial,hora_final,nome,cpf) VALUES (?,?,?,?,?)", (newdata,newhora_inicial,newhora_final,newnome,newcpf))
                    conexaodb.commit()
                    print("Horario Registrado com sucesso")
                    
            else:
                print("Digite um horário entre 09:00 e 23:00.")

        else:
            print("Digite um horário entre 09:00 e 23:00.")
    except ValueError:
        print("Formato inválido. Digite no formato 00:00.")
   
   



def MostrarHorarios(): #função mostra todos os horarios cadastrados e filtrando por dia ou nome
    conexaodb = pyodbc.connect("Driver={SQLite3 ODBC Driver};Server=localhost;Database=TabelaHorario.db")
    cursor = conexaodb.cursor()


    print("1 - Localizar por Nome\n2 - Localizar por Data\n3 - Localizar por CPF")
    number2 = int(input())
   

    if number2 == 1:

        print("Insira o Nome:")
        Name = input()
        cursor.execute("SELECT * FROM HorariosReserva WHERE nome = ?", (Name))
        AgendaLocal = cursor.fetchall()
        
        for i in AgendaLocal:#separar linha a linha
            print(f"{i}\n")
    
    
    elif number2 == 2:

        print("Insira a Data(formato DD/MM/AAAA):")
        Date = input()
        try:
        #verificando formato da data
            dia1, mes2, ano2 = map(int, Date.split('/'))
        
        #Procurando no banco:
            cursor.execute("SELECT * FROM HorariosReserva WHERE data = ?", (Date))
            AgendaLocal = cursor.fetchall()
        
            for i in AgendaLocal:#separar linha a linha
                print(f"{i}\n")
    
        except ValueError:
            print("digite em formato valido")
        
    elif number2 == 3:
        print("Insira o CPF:")
        cpf = int(input())
        
        cursor.execute("SELECT * FROM HorariosReserva WHERE cpf = ?", (cpf))
        AgendaLocal = cursor.fetchall()
        
        for i in AgendaLocal:#separar linha a linha
             print(f"{i}\n")




while True:  #menu
    print("SISTEMA DE RESERVA DO LOCAL XXXXX")
    print("1 - Para Cadastrar um Horario\n2 - Para Verificar Horarios Cadastrados\n3 - Para Encerrar o Programa")
    number1 = int(input())
    
    if number1 == 1:
        CadastrarHorario()
        break
    elif number1 == 2:
        MostrarHorarios()
        break
    elif number1 == 3:
        print("Programa Finalizado")
        break
    else:
        print("digite um numero válido")


    