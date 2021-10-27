from pprint import pp, pprint

variable = [('campo1','valor1'),
            ('campo2','valor2'),
            ('campo3','valor3'),
            ('campo4','valor4'),
            ('campo5','valor5'),
            ('campo6','valor6')]

dic = dict(variable)
pprint(dic.items())

for k,v in dic.items():
    print(k,v)

# -------------------------
claves = dic.keys()
valores = dic.values()
pprint(type(claves))
pprint(valores)

for c in list(claves):
    print(c)