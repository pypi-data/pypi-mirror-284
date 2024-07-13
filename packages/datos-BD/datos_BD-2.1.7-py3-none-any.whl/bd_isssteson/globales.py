
# def main():
#     """
#     Módulo para Retornar nombres de Servidores, Catálogos,
#     Usuarios y Contraseñas de MSSQL Server de ISSSTESON

#     Returns:
#         [llave]: [LLave para la encriptación]
#         [servidor1]: [Servidor Isssteson01]
#         [servidor2]: [Servidor sql-oc]
#         [S1_catalogo01]: [BD Ingresos]
#         [S1_catalogo02]: [BD Sipes]
#         [S1_catalogo03]: [BD Creditos]
#         [S2_catalogo01]: [BD Expedientes de Pensiones]
#         [S2_catalogo02]: [BD Expedientes de Prestaciones]
#         [sql_usuario01]: [Usuario Informática]
#         [U1_password]: [Contraseña para el sql_usuario01]
#     """


## ==============
##    LLAVES
## ==============
llave = 'uti-isssteson'                             ## --LLave para generar ecriptación y decriptación
# ==============
#   SERVIDORES
# ==============
servidor1 = 'isssteson01'                           ## --Servidor ISSSTESON01
servidor2 = 'servidorsql-oc'                        ## --Servidor SERVERSQL-OC
# ==================
#   BASES DE DATOS
# ==================
S1_catalogo01 = 'Ingresos'                          ## --BD Ingresos
S1_catalogo02 = 'Sipesdb'                           ## --BD Sipesdb
S1_catalogo03 = 'Creditos'                          ## --BD Créditos
S2_catalogo01 = 'ExpedientePensiones'               ## --BD Expedientes de Pensiones
S2_catalogo02 = 'ExpedientePrestaciones'            ## --BD Expedientes de Prestaciones
# ==================
#   USUARIOS MSSQL
# ==================
sql_usuario01 = 'Informatica'                       ## --Usuario Informática
# ====================
#  CONTRASEÑAS MSSQL
# ====================
U1_password = 'Erw47gLS'                            ## --Contraseña del usuario Informática

#     return llave, servidor1, servidor2, S1_catalogo01, S1_catalogo02, S1_catalogo03, S2_catalogo01, S2_catalogo02, sql_usuario01, U1_password


# if __name__ == "__main__":
#     main()