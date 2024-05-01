import numpy as np

#entrada, geralmente vem de um arquivo texto
linhas = 1
registro = []
linhatoken = []
tokens = []
erro = False

with open("Testetokens3.txt", "r", encoding="utf-8") as arquivo: #define o arquivo que vai ser lido
        for line in arquivo:
            palavra = line
            #variavel para armazenar o lexema 
            lexema = ''
            palavraatual = ""
            iniPalavra = 0
            #variavel para armazenar a lista de token (que ira alimentar o sintatico)
            token = []
            lexemas = []
            linha = [] 
            
            for i in range(len(palavra)): #percorre a entrada
                
                
                if palavra[i] == '\n':
                    linhas =linhas + 1 
                    continue
                
                    
                elif palavra[i] != ' ':  #se nao for espaço... aqui tem q colocar outros caracters como pontuacao e parentização
                    lexema = lexema + palavra[i]
                    
                    
                else: 
                    lexema = ''
                    iniPalavra = i+1
                    
                print(lexema) #print opcional para ver o andamento 
                
                if lexema == ' ':
                    
                    lexema = ''
                elif lexema == 'write':
                    token.append(0)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                    
                elif lexema == 'while':
                    token.append(1)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'until':
                    token.append(2)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'to':
                    token.append(3)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'then':
                    token.append(4)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'string':
                    token.append(5)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'repeat':
                    token.append(6)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'real':
                    token.append(7)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'read':
                    token.append(8)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'program':
                    token.append(9)
                    lexemas.append(lexema)
                    linha.append(linhas)
                
                elif lexema == 'procedure':
                    token.append(10)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'or':
                    token.append(11)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'of':
                    token.append(12)
                    lexemas.append(lexema)
                    linha.append(linhas)

                elif palavra[iniPalavra] == '&' :   #literal
                    if palavra[i+1] == " " or palavra[i+1] == "\n":     
                        if palavra[i] == "&" and i != iniPalavra:    
                            token.append(13)
                            lexemas.append(lexema)
                            linha.append(linhas)
                        else:
                            token.append("=====Erro Lexico=====")
                            lexemas.append("=====Erro Lexico=====")
                            linha.append(linhas)
                elif lexema == 'integer':
                    token.append(14)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'if':
                    token.append(15)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'î':
                    token.append(17)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'for':
                    token.append(18)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'end':
                    token.append(19)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'else':
                    token.append(20)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'do':
                    token.append(21)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'declaravariaveis':
                    token.append(22)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'const':
                    token.append(23)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'char':
                    token.append(24)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'chamaprocedure':
                    token.append(25)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'begin':
                    token.append(26)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'array':
                    token.append(27)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == 'and':
                    token.append(28)
                    lexemas.append(lexema)
                    linha.append(linhas)

                elif lexema == '>=':
                    token.append(29)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == '>'and palavra[i+1] != '=':
                    token.append(30)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == '=':
                    token.append(31)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == '<>':
                    token.append(32)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == '<=':
                    token.append(33)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == '<'and palavra[i+1] != '>'and palavra[i+1] != '=':
                    token.append(34)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == '+':
                    token.append(35)
                    lexemas.append(lexema)
                    linha.append(linhas)
                
                elif lexema.isdigit() == True and palavra[i+1] == " " or lexema.isdigit() == True and palavra[i+1] == "\n" :
                    if int(lexema) <= 20000:
                        token.append(37)
                        lexemas.append(lexema)
                        linha.append(linhas)
                    else:
                        token.append("=====Erro Lexico=====")
                        lexemas.append("=====Erro Lexico=====")
                        linha.append(linhas)
                        
                elif lexema.isdigit() == True and palavra[i+1] == ".":
                    if int(lexema) <= 20000:
                        if palavra[i+2].isdigit():
                            lexema= lexema + palavra[i+1]+palavra[i+2]
                            if palavra[i+3].isdigit():
                                lexema= lexema + palavra[i+3]
                                if palavra[i+4].isdigit():
                                    token.append("=====Erro Lexico=====")
                                    lexemas.append("=====Erro Lexico=====")
                                    linha.append(linhas)
                                    continue
                            token.append(36)
                            lexemas.append(lexema)
                            linha.append(linhas)
                    else:
                        token.append("=====Erro Lexico=====")
                        lexemas.append("=====Erro Lexico=====")
                        linha.append(linhas)
                    
                elif palavra[iniPalavra] == '"' :   #string
                    if palavra[i+1] == " " or palavra[i+1] == "\n":     
                        if palavra[i] == '"' and i != iniPalavra and len(lexema)>3:    
                            token.append(38)
                            lexemas.append(lexema)
                            linha.append(linhas)        
                        else:
                            
                            token.append("=====Erro Lexico=====")
                            lexemas.append("=====Erro Lexico=====")
                            linha.append(linhas)
                    
                elif palavra[iniPalavra] == "'" :   #char
                    if palavra[i+1] == " " or palavra[i+1] == "\n":     
                        if palavra[i] == "'" and i != iniPalavra and len(lexema) == 3:    
                            token.append(39)
                            lexemas.append(lexema)
                            linha.append(linhas)
                            
                        else:
                            token.append("=====Erro Lexico=====")
                            lexemas.append("=====Erro Lexico=====")
                            linha.append(linhas)
                    
                elif lexema == ']':
                    token.append(40)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == '[':
                    token.append(41)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == ';':
                    token.append(42)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == ':':
                    token.append(43)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == '/':
                    token.append(44)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == '..':
                    token.append(45)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == '.':
                    if i == len(palavra)-1:
                        token.append(46)
                        lexemas.append(lexema)
                        linha.append(linhas) 
                    elif i < len(palavra):
                        if palavra[i+1] != '.':
                            token.append(46)
                            lexemas.append(lexema)
                            linha.append(linhas)
                    
                elif lexema == ',':
                    token.append(47)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == '*':
                    token.append(48)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == ')':
                    token.append(49)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == '(':
                    token.append(50)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == '$':
                    token.append(51)
                    lexemas.append(lexema)
                    linha.append(linhas)
                    
                elif lexema == '-':
                    if i<len(palavra)-1: 
                        if palavra[i+1].isdigit():
                            token.append("=====Erro Lexico=====")
                            lexemas.append("=====Erro Lexico=====")
                            linha.append(linhas)
                    else:
                        token.append(52)
                        lexemas.append(lexema)
                        linha.append(linhas)
                    
                elif palavra[iniPalavra].isalpha() == True and palavra[i+1] == " " or palavra[iniPalavra].isalpha() == True and palavra[i+1] == "\n" :
                    if len(lexema)<=15:
                        if "&" in lexema or "'" in lexema or '"' in lexema or "$" in lexema :
                            token.append("=====Erro Lexico=====")
                            lexemas.append("=====Erro Lexico=====")
                            linha.append(linhas)
                            
                        else:
                            token.append(16)
                            lexemas.append(lexema)
                            linha.append(linhas)
                            
                    else:
                        token.append("=====Erro Lexico=====")
                        lexemas.append("=====Erro Lexico=====")
                        linha.append(linhas)
            
            #Entrega do lexico - token - lexema - linha
            
            for i in range(0,len(token)):
                
                #print('Token: '+str(token[i]) + ' - Lexema: '+str(lexemas[i]) + ' - Linha: '+ str(linha))
                #registro.append(str(token[i]))
                registro.append('Token: '+str(token[i]) + ' - Lexema: '+str(lexemas[i]) + ' - Linha: '+ str(linha[i]))
                linhatoken.append(linha[i])
                tokens.append(token[i])
            #print(token) # [2, 11, 39, 15, 40, 20, 38]
            
            #salvar do lexico para entregar para o sintático
            token = np.array(token) #converte lista do python para numpy array
        
    
for i in range(0,len(registro)):
    print(registro[i])






print("\n======================\n analise sintatica\n======================")

print(tokens) 

        

tokens = np.array(tokens)
producoes = [[9,16,42,55,46,-1,-1,-1,-1,-1,-1,-1,-1,-1]] #P1
producoes = np.append(producoes, [[56,57,58,59,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P2
producoes = np.append(producoes, [[23,16,31,60,42,61,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P3
producoes = np.append(producoes, [[17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P4
producoes = np.append(producoes, [[16,31,60,42,61,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0);#P5
producoes = np.append(producoes, [[17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0);#P6
producoes = np.append(producoes, [[22,62,43,60,42,63,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P7
producoes = np.append(producoes, [[17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P8
producoes = np.append(producoes, [[16,64,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P9
producoes = np.append(producoes, [[47,16,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P10
producoes = np.append(producoes, [[17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P11
producoes = np.append(producoes, [[62,43,60,42,63,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P12
producoes = np.append(producoes, [[17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0);#P13
producoes = np.append(producoes, [[27,41,37,45,37,40,12,65,-1,-1,-1,-1,-1,-1]], axis = 0); #P14
producoes = np.append(producoes, [[14,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P15
producoes = np.append(producoes, [[24,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P16
producoes = np.append(producoes, [[5,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P17
producoes = np.append(producoes, [[7,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P18
producoes = np.append(producoes, [[14,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P19
producoes = np.append(producoes, [[24,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P20
producoes = np.append(producoes, [[5,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P21
producoes = np.append(producoes, [[7,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P22
producoes = np.append(producoes, [[10,16,66,58,59,42,56,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P23
producoes = np.append(producoes, [[17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P24
producoes = np.append(producoes, [[50,62,43,60,42,63,49,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P25
producoes = np.append(producoes, [[17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P26
producoes = np.append(producoes, [[26,67,42,68,19,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P27
producoes = np.append(producoes, [[67,42,68,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P28
producoes = np.append(producoes, [[17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P29
producoes = np.append(producoes, [[15,41,69,40,4,26,67,19,70,-1,-1,-1,-1,-1]], axis = 0); #P30
producoes = np.append(producoes, [[1,41,69,40,21,26,67,19,-1,-1,-1,-1,-1,-1]], axis = 0); #P31
producoes = np.append(producoes, [[6,2,41,69,40,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P32
producoes = np.append(producoes, [[8,50,71,49,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P33
producoes = np.append(producoes, [[25,16,72,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P34
producoes = np.append(producoes, [[0,50,73,74,49,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P35
producoes = np.append(producoes, [[18,41,16,31,69,40,3,41,69,40,21,26,67,19]], axis = 0); #P36
producoes = np.append(producoes, [[17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P37
producoes = np.append(producoes, [[50,62,49,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P38
producoes = np.append(producoes, [[17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P39
producoes = np.append(producoes, [[13,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P40
producoes = np.append(producoes, [[69,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P41
producoes = np.append(producoes, [[47,73,74,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P42
producoes = np.append(producoes, [[17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P43
producoes = np.append(producoes, [[75,76,77,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P44
producoes = np.append(producoes, [[78,79,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P45
producoes = np.append(producoes, [[37,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P46
producoes = np.append(producoes, [[16,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P47
producoes = np.append(producoes, [[38,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P48
producoes = np.append(producoes, [[39,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P49
producoes = np.append(producoes, [[36,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P50
producoes = np.append(producoes, [[50,69,49,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P51
producoes = np.append(producoes, [[31,80,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0);  #P52
producoes = np.append(producoes, [[34,80,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P53
producoes = np.append(producoes, [[30,80,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P54
producoes = np.append(producoes, [[29,80,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P55
producoes = np.append(producoes, [[33,80,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P56
producoes = np.append(producoes, [[32,80,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P57
producoes = np.append(producoes, [[17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P58
producoes = np.append(producoes, [[35,75,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P59
producoes = np.append(producoes, [[52,75,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P60
producoes = np.append(producoes, [[75,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P61
producoes = np.append(producoes, [[35,75,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P62
producoes = np.append(producoes, [[52,75,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P63
producoes = np.append(producoes, [[11,75,76,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P64
producoes = np.append(producoes, [[17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P65
producoes = np.append(producoes, [[48,78,79,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P66
producoes = np.append(producoes, [[44,78,79,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P67
producoes = np.append(producoes, [[28,78,79,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P68
producoes = np.append(producoes, [[17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P69
producoes = np.append(producoes, [[20,26,67,19,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P70
producoes = np.append(producoes, [[17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P71
producoes = np.append(producoes, [[17,81,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0); #P72
producoes = np.append(producoes, [[47,38,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0);  #P73
producoes = np.append(producoes, [[17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]], axis = 0);#P74


#inicializar a Matriz de Parsing com zeros.
tabParsing = [],[]
tabParsing = np.zeros((82, 54))

tabParsing[54][19] = 1;
tabParsing[55][10] = 2;
tabParsing[55][18] = 2;
tabParsing[55][19] = 2;
tabParsing[55][22] = 2;
tabParsing[56][10] = 23;
tabParsing[56][22] = 74;
tabParsing[56][18] = 74;
tabParsing[56][19] = 24;
tabParsing[56][46] = 24;
tabParsing[57][18] = 4;
tabParsing[57][19] = 3;
tabParsing[57][21] = 74;
tabParsing[57][22] = 74;
tabParsing[57][46] = 4;
tabParsing[58][18] = 7;
tabParsing[58][22] = 8;
tabParsing[59][22] = 27;
tabParsing[60][5] = 21;
tabParsing[60][7] = 22;
tabParsing[60][37] = 19;
tabParsing[60][20] = 20;
tabParsing[60][23] = 14;
tabParsing[61][39] = 5;
tabParsing[61][18] = 6;
tabParsing[61][46] = 6;
tabParsing[62][39] = 9;
tabParsing[63][39] = 12;
tabParsing[63][22] = 13;
tabParsing[63][49] = 13;
tabParsing[64][43] = 11;
tabParsing[64][47] = 10;
tabParsing[64][49] = 11;
tabParsing[65][5] = 17;
tabParsing[65][7] = 18;
tabParsing[65][37] = 15;
tabParsing[65][20] = 16;
tabParsing[66][18] = 26;
tabParsing[66][19] = 26;
tabParsing[66][46] = 26;
tabParsing[66][50] = 25;
tabParsing[67][0] = 35;
tabParsing[67][1] = 31;
tabParsing[67][2] = 37;
tabParsing[67][6] = 32;
tabParsing[67][8] = 33;
tabParsing[67][38] = 30;
tabParsing[67][14] = 36;
tabParsing[67][15] = 37;
tabParsing[67][21] = 34;
tabParsing[67][42] = 37;
tabParsing[68][0] = 75;
tabParsing[68][1] = 75;
tabParsing[68][6] = 75;
tabParsing[68][8] = 75;
tabParsing[68][38] = 30;
tabParsing[68][17] = 75;
tabParsing[68][18] = 75;
tabParsing[68][19] = 74;
tabParsing[68][25] = 75;
tabParsing[68][15] = 29;
tabParsing[69][39] = 44;
tabParsing[69][32] = 44;
tabParsing[69][33] = 44;
tabParsing[69][34] = 44;
tabParsing[69][45] = 44;
tabParsing[69][50] = 44;
tabParsing[70][2] = 71;
tabParsing[70][15] = 71;
tabParsing[70][16] = 70;
tabParsing[70][42] = 71;
tabParsing[71][39] = 72;
tabParsing[72][2] = 39;
tabParsing[72][15] = 39;
tabParsing[72][42] = 39;
tabParsing[72][50] = 38;
tabParsing[73][36] = 40;
tabParsing[73][39] = 41;
tabParsing[73][32] = 41;
tabParsing[73][33] = 41;
tabParsing[73][34] = 41;
tabParsing[73][45] = 41;
tabParsing[73][50] = 41;
tabParsing[74][47] = 42;
tabParsing[74][49] = 43;
tabParsing[75][39] = 45;
tabParsing[75][36] = 45;
tabParsing[75][32] = 45;
tabParsing[75][33] = 45;
tabParsing[75][34] = 45;
tabParsing[75][35] = 45;
tabParsing[75][50] = 45;
tabParsing[76][2] = 65;
tabParsing[76][11] = 64;
tabParsing[76][15] = 65;
tabParsing[76][25] = 65;
tabParsing[76][26] = 65;
tabParsing[76][27] = 65;
tabParsing[76][28] = 65;
tabParsing[76][29] = 65;
tabParsing[76][30] = 65;
tabParsing[76][31] = 62;
tabParsing[76][40] = 65;
tabParsing[76][42] = 65;
tabParsing[76][47] = 65;
tabParsing[76][49] = 65;
tabParsing[76][52] = 63;
tabParsing[77][2] = 58;
tabParsing[77][15] = 58;
tabParsing[77][25] = 55;
tabParsing[77][26] = 54;
tabParsing[77][27] = 52;
tabParsing[77][28] = 57;
tabParsing[77][29] = 56;
tabParsing[77][30] = 53;
tabParsing[77][40] = 58;
tabParsing[77][42] = 58;
tabParsing[77][47] = 58;
tabParsing[77][49] = 58;
tabParsing[78][39] = 47;
tabParsing[78][32] = 50;
tabParsing[78][33] = 46;
tabParsing[78][34] = 48;
tabParsing[78][36] = 76;
tabParsing[78][35] = 49;
tabParsing[78][50] = 51;
tabParsing[79][2] = 69;
tabParsing[79][11] = 69;
tabParsing[79][15] = 69;
tabParsing[79][24] = 68;
tabParsing[79][25] = 69;
tabParsing[79][26] = 69;
tabParsing[79][27] = 69;
tabParsing[79][28] = 69;
tabParsing[79][29] = 69;
tabParsing[79][30] = 69;
tabParsing[79][31] = 69;
tabParsing[79][40] = 69;
tabParsing[79][42] = 69;
tabParsing[79][44] = 67;
tabParsing[79][47] = 69;
tabParsing[79][48] = 66;
tabParsing[79][49] = 69;
tabParsing[79][52] = 69;
tabParsing[80][39] = 61;
tabParsing[80][31] = 59;
tabParsing[80][32] = 61;
tabParsing[80][33] = 61;
tabParsing[80][34] = 61;
tabParsing[80][45] = 61;
tabParsing[80][50] = 61;
tabParsing[80][52] = 60;
tabParsing[81][47] = 73;
tabParsing[81][49] = 74;

pilha = [51] #$ topo da pilha

aux = 0

pilha = np.hstack([producoes[0][:], pilha])


print(pilha)


X = pilha[0]
a = tokens[0]

while X != 75: #enquanto pilha nao estiver vazia
    
    print(X)
    print(a)
    print(pilha)
    aux = aux+1
    
    if X == 17: #se o topo da pilha for vazio
        pilha = np.delete(pilha,[0])
        X = pilha[0]
    else:
        if X <= 52: #topo da pilha eh um terminal
            if X == a: #deu match :D
                pilha = np.delete(pilha,[0])
                tokens = np.delete(tokens,[0])
                X = pilha[0]
                if tokens.size != 0:
                    a = tokens[0]
            else:
                print('Erro Sintatico na Linha 1: ' + str(linhatoken[aux-1]))
                break
        else: #topo da pilha é um não terminal 
            topo = np.hstack([producoes[int(tabParsing[X][a])-1][:], pilha]) #empilha as producoes correspondentes
            if topo[0] == 1: # se topo vazio X recebe o novo topo da pilha
                X = topo[0] #
            else:
                if topo[0] != 0: # se topo nao vazio atualiza a pilha
                    pilha = np.delete(pilha,[0])
                    pilha = np.hstack([producoes[int(tabParsing[X][a])-1][:], pilha])
                    pilha = pilha[pilha != 0]
                    X = pilha[0]
                else:
                    print('Erro Sintatico na Linha: '+ str(linhatoken[aux-1]))
                    break
                

        
print('Pilha: ')                
print(pilha)
print('Entrada: ')
print(tokens)




