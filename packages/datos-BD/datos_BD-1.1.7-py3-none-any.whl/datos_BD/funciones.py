from encrypts import decrypt, encrypt, k


## Retornar servidores
def servidores():
    """ Función que retorna los Servidores Disponibles en la Librería

    Returns:
        [Tupla]: [Servidores disponibles para la Librería]
    """
    return (encrypt('isssteson01',k),encrypt('serversql-oc',k))  


## Retornar las bases de datos disponibles para la Librería
def bases_d_datos(servidor):
    """AI is creating summary for bases_d_datos

    Args:
        servidor ([Tupla]): [description]

    Returns:
        [Tupla]: [Listado de Bases disponibles en la Librería según servidor seleccionado]
    """
    serv = servidores()

    if decrypt(servidor,k).decode("utf-8") == decrypt(serv[0],k).decode("utf-8"):
        return (encrypt('ingresos',k),encrypt('sipesdb',k),encrypt('creditos',k))
    elif decrypt(servidor,k).decode("utf-8") == decrypt(serv[1],k).decode("utf-8"):
        return (encrypt('ExpedientePensiones',k),encrypt('ExpedientePrestaciones',k))
    else:
        return (None,None,None)


## Retornar los Datos para la Conexión dependiedo del Servidor
def DatosServidor(args):
    """Función para Retornar los parámetros para conexión a Base de Datos, según servidor

    Args:
        args ([Tupla]): [Servidor, Base de Datos]

    Returns:
        [Tupla]: [Servidor, Base de Datos, Usuario, Contraseña]
    """
    serv = servidores()
    
    if decrypt(args[0],k).decode("utf-8") == decrypt(serv[0],k).decode("utf-8"):
        cat = bases_d_datos(serv[0])
        if args[1] == cat[0]:
            return (serv[0],cat[0],encrypt('informatica',k),encrypt('erw47gls',k))
        elif decrypt(args[1],k).decode("utf-8") == decrypt(cat[1],k).decode("utf-8"):
            return (serv[0],cat[1],encrypt('informatica',k),encrypt('erw47gls',k))
        elif decrypt(args[1],k).decode("utf-8") == decrypt(cat[2],k).decode("utf-8"):
            return (serv[0],cat[2],encrypt('informatica',k),encrypt('erw47gls',k))
        else:
            return None
    elif decrypt(args[0],k).decode("utf-8") == decrypt(serv[1],k).decode("utf-8"):
        cat = bases_d_datos(serv[1])
        if decrypt(args[1],k).decode("utf-8") == decrypt(cat[0],k).decode("utf-8"):
            return (serv[1],cat[0],encrypt('informatica',k),encrypt('erw47gls',k))
        elif args[1] == cat[1]:
            return (serv[1],cat[1],encrypt('informatica',k),encrypt('erw47gls',k))
        else:
            return None
    else:
        return None
    
