## PUNTO A: GRAMATICAS ##

def clasificar_gramatica(string):
    reglas = string.splitlines();
    condicionincorrecta="";
    condicionincorrectar2="";
    condicionincorrectar1="";
    print(reglas);
    condiciones = [];
    condicionesr2 = [];
    condicionesr1 = [];
    expresiones = [];
    expresionesr2 = [];
    expresionesr1 = [];
    izq = 0;
    der = 0;
    terminal = 'false';
    noterminal = 'false';
    despuesdedospuntos = 'false';
    distinguido = ' ';
    expresionlambda = [];
    hubolambda = 'false';
    distinguidoader = 'false';
    lambdaendistinguido = 'false';
    auxletra = ' ';
    expresionderecha = [];
    condicionesg3 = "no pertenece a ninguna de las formas NT -> t, NT -> NT t, NT -> t NT";
    condicionesg2 = "no pertence a ninguna de las formas NT -> cualquier combinación de n terminales y no terminales";
    condicionesg1 = "no pertenece a ninguna de las formas de que la cant. de elementos(NT*,T*) a izq(NT*T) sea inferior a la cantidad de elementos a der";
    for expresion in reglas:
        izq=0;
        der=0;
        cantizq = 0;
        cantder = 0;
        terminal = 'false';
        noterminal = 'false';
        despuesdedospuntos='false';
        distinguidoader='false';
        lambdaendistinguido='false';
        hubolambda='false';
        for letra in expresion:
            izq=izq+1;
            if(izq==1):
                if (letra.isupper()):
                    noterminal = 'true';
                    if distinguido == ' ':
                        distinguido = expresion.split(':')[0].split()[0];                   
                if (letra.islower()):
                    terminal='true';
                    cantizq=cantizq+1;
            if(despuesdedospuntos=='false'):
                if (letra==' '):
                    auxletra=letra;
                if (letra.isupper()):
                    auxletra=letra;
                    cantizq=cantizq+1;
                if ((letra.islower())& (auxletra[0].isupper())):
                    auxletra=auxletra+letra;
                if ((letra.islower()) & (auxletra==' ')):
                    auxletra = auxletra + letra;
                    cantizq=cantizq+1;
            if (letra==":"):
                auxletra = ' ';
                despuesdedospuntos = 'true';
                izq=izq-1;
                noterminal='false';
                if (cantizq > 1):
                    condiciones.append(condicionesg3);
                    expresiones.append(expresion);
                    condicionesr2.append(condicionesg2);
                    expresionesr2.append(expresion);
            if (despuesdedospuntos=='true'):
                palabrareservada = expresion.split(":")[1];
                expresionderecha = expresion.split(":")[1].split();
                for simbolo in expresionderecha:
                    if simbolo == distinguido:
                        distinguidoader='true'
                if (palabrareservada == 'lambda'):
                    expresionlambda.append(expresion);
                    hubolambda='true';
                    if expresion.split(':')[0].split()[0] == distinguido:
                        lambdaendistinguido = 'true';
                    break;
                    
                        
                if (letra.islower()):
                    if cantder==0:
                        cantder=cantder+1;
                        auxletra=letra;
                if (letra==' '):
                    auxletra=letra;
                if (letra.isupper()):
                    auxletra=letra;
                    cantder=cantder+1;
                if ((letra.islower())& auxletra[0].isupper()):
                    auxletra=auxletra+letra;
                if ((letra.islower())& auxletra.islower()):
                    auxletra=auxletra+letra;
                if ((letra.islower()) & (auxletra==' ')):
                    auxletra = letra;
                    cantder=cantder+1;
        print (cantizq,cantder);

        if (cantder) > 2:
            condiciones.append(condicionesg3);
            expresiones.append(expresion);
            expresiones=list(set(expresiones));

        if ((lambdaendistinguido == 'false') and (hubolambda == 'true')): ##Si hay lambda pero el antecedente no es el distinguido, NO es G1
            condicionesr1.append(condicionesg1);
            expresionesr1.append(expresion);
            despuesdedospuntos='false';
            lambdaendistinguido == 'false';
            distinguidoader == 'false';
            hubolambda == 'false';
            der=0;izq=0;cantizq=0;cantder=0;

        if ((lambdaendistinguido == 'true') and (distinguidoader == 'true') and (hubolambda == 'true')): ##Si hay lambda y el antecedente es el distinguido pero este tiene recursión, NO es G1
            condicionesr1.append(condicionesg1);
            expresionesr1.append(expresion);
            despuesdedospuntos='false';
            lambdaendistinguido == 'false';
            distinguidoader == 'false';
            hubolambda == 'false';
            der=0;izq=0;cantizq=0;cantder=0;

        if (cantizq>cantder):
            condicionesr1.append(condicionesg1);
            expresionesr1.append(expresion);
            despuesdedospuntos='false';
            lambdaendistinguido == 'false';
            distinguidoader == 'false';
            hubolambda == 'false';
            der=0;izq=0;cantizq=0;cantder=0;
    print ('El distinguido es:', distinguido);

    """--------------------------------------------------------------------------------------------------------------"""

    if (not(condiciones)==[]):
        condicionincorrecta="no pertenece a ninguna de las formas NT -> t, NT -> NT t, NT -> t NT)";
    if (not(condicionesr2)==[]):
        condicionincorrectar2="no pertenece a ninguna forma  NT -> combinacion de (t)y(NT) o biceversa";
    if (not (condicionesr1) == []):
        condicionincorrectar1 = "no pertenece a ninguna de las formas de que la cant. de elementos(conformado por cualquier combinación de NT y T) a izq.(conformado por cualquier combinación de NT y T) sea inferior a la cantidad de elementos a der.";
    resultado={3: [tuple(expresiones),condicionincorrecta],
               2: [tuple(expresionesr2),condicionincorrectar2],
               1: [tuple(expresionesr1),condicionincorrectar1],
               0: []
               }

    print ("G3:",resultado[3]);
    print ("G2:",resultado[2]);
    print ("G1:",resultado[1]);
    print ("G0:",resultado[0]);


## PUNTO B: AUTÓMATA DE PILA ##

class AutomataPila:
    """ Esta clase implementa un automáta de pila a partir de la definición de
    estados y transiciones que lo componen, pudiendo validar si una cadena dada
    puede ser reconocida por el mismo.
    """

    def __init__(self, estados, estados_aceptacion):
        """ Constructor de la clase.

        Args
        ----
        estados: dict
            Diccionario de estados que especifica en las claves los nombres de los
            estados y como valores una lista de transiciones salientes de dicho estado.
            Cada transición se compone de: (s,p,a,e) siendo
            s -> símbolo que se consume de la entrada para aplicar la transición.
            p -> símbolo que se consume del tope de la pila para aplicar la transición.
            a -> lista de símbolo/s que se apila una vez aplicada la transición.
            e -> estado de destino.

            Ejemplo:
            {'a': [('(', 'Z0', ['Z0'], 'a'), 
                   ('(', '(', ['(', '('], 'a'), 
                   (')', '(', [''], 'b')],
             'b': [(')', '(', [''], 'b'), 
                   ('$', 'Z0', ['Z0'], 'b')]}
        
        estados_aceptacion: array-like
            Estados que admiten fin de cadena.

            Ejemplo: 
            ['b']
        """

        self.estados = []
        self.estado_actual = None
        self.cadena_restante = ''

    def validar_cadena(self, cadena):
##        estados = {'a': [('a','',['a'],'a'),                             ## Estados de prueba de un autómata que reconoce a^p b^q c^x donde q = p + x (siendo "q" mayor o igual a 1, y "p" y "x" mayor o iguales a 0)
##                         ('b','a',[''],'b'),
##                         ('b','Z0',['Z0','b'],'b')],                     ## Agregamos "self." antes de "estados" para la entrega, nosotros para las pruebas no lo usamos.
##                   'b': [('b','Z0',['Z0','b'],'b'),
##                         ('b','b',['b','b'],'b'),
##                         ('b','a',[''],'b'),
##                         ('$','Z0',[''],'c'),
##                         ('c','b',[''],'c')],
##                   'c': [('c','b',[''],'c'),
##                         ('$', 'Z0', [''], 'c')]}; 
        claves = list(self.estados.keys());
        go_clave = claves[0];
        pila=['Z0'];    ## Inicializamos la pila con Z0 como en la práctica.
        for letra in cadena:
            validez=False;    ## Esto sirve para evitar que en el caso de llegar a la ultima transicion de un estado y no se haya podido avanzar o hacer algo, que corte la ejecucion porque la cadena no seria válida.
            if self.estados[go_clave]:
                tran = self.estados[go_clave]  ## tran: son las diferentes transiciones que tiene un estado
                for transicion in tran:
                    if transicion[0] == letra:
                        if transicion[1] == pila[-1]:
                            pila.pop()
                            if not(transicion[2] == ['']):
                                for simbolo in transicion[2]:
                                    pila.append(simbolo)
                            go_clave = transicion[3];
                            validez=True
                            break; ## Los break los usamos para pasar al siguiente estado o letra de la cadena a evaluar.
                        else:
                            if transicion[1] == '':
                                if not(transicion[2] == ['']):
                                    for simbolo in transicion[2]:
                                        pila.append(simbolo)
                                go_clave = transicion[3];
                                validez=True
                                break;
                            else:
                                if (transicion == tran[len(tran)-1]) and (validez==False):
                                    return(False);
                                else:
                                    continue  ## Esto sirve para que, cuando lo que haya que sacar de la pila en una transicion determinada(que no es la última de ese estado) no sea igual a "nada" o a lo que hay en el tope de la pila en ese momento, entonces continua la ejecucion hacia la siguiente transicion en ese estado.
                    else:
                        if (transicion == tran[len(tran)-1]) and (validez==False):
                            return(False);
                            
                                
                                
        if pila == []:  ## Al igual que en la práctica, evaluamos que si al finalizar la ejecución sin errores, la pila este vacía o no.
            return(True)
        else:
            return(False);

