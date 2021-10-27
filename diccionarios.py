#funcion(a,b,c,d=1, *args, **kwargs)

# diccionario = {
#     'nombre': 'Fernando',
#     'apellido1': 'Lopez',
#     'notas': [1,2,3,4,5]
# }

# diccionario['apellido2'] = 'García'
# diccionario['apellido1'] = 'López'

# print(type(diccionario))
# print(diccionario['nombre'])
# print(diccionario['apellido1'])
# print(diccionario['apellido2'])
# print(f"Nombre completo: {diccionario['nombre']} {diccionario['apellido1']}")
import pprint
vscode = {
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Archivo actual",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
        {'type': 'valor'
        }
    ]
}
vscode['configurations'][0]['type'] = 'Manolito'
tmp = vscode
pprint.pprint(tmp['configurations'][0].keys() )