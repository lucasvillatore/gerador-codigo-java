import json

classes = {}

def le_arquivo(nome_arquivo):
    
    arquivo = open(nome_arquivo, "r")
    arquivo_json = json.load(arquivo)

    return arquivo_json
    
def main_java():
    
    main_class = [
        "class",
        "Main"
    ]
    args = [
        'public',
        'static',
        'void',
        'main',
        '(String args[])'
    ]

    program_main = " ".join(main_class) + " {\n\t" + " ".join(args) + "{}" + "\n}"

    return program_main

def pega_atributo(atributo):
    
    if (isinstance(atributo, str)):
        return "String"
    if (isinstance(atributo, list)):
        return "ArrayList"
    
    return None

def existe_na_lista(classe, chave):
    global classes

    for lista in classes[classe]['list']:
        if (lista['valor'] == chave):
            return True

    return False

def monta_classes(nome_classe, instancias):
    global classes

    if nome_classe not in classes:
        classes[nome_classe] = {
            'str': [],
            'list': []
        }

    for instancia in instancias:
        for chave, valor in instancia.items():

            if (isinstance(valor, str)):
                if chave not in classes[nome_classe]['str']:
                    classes[nome_classe]['str'].append(chave)
            
            if (isinstance(valor, list)):
                if (len(valor) == 0):
                    print(classes[nome_classe]['list'])
                    if not existe_na_lista(nome_classe, chave):
                        classes[nome_classe]['list'].append({
                            'tipo': chave,
                            'variavel': chave.lower() + 's',
                            'valor': chave
                        })
                    monta_classes(chave, valor)
        
                else:
                    valor_copia = valor.copy().pop()
                    if (isinstance(valor_copia, dict)):
                        if not existe_na_lista(nome_classe, chave):
                            classes[nome_classe]['list'].append({
                                'tipo': chave,
                                'variavel': chave.lower() + 's',
                                'valor': chave
                            })
                        monta_classes(chave, valor)
                    else:
                        if not existe_na_lista(nome_classe, chave):
                            classes[nome_classe]['list'].append({
                                'tipo': 'String',
                                'variavel': chave.lower() + 's',
                                'valor': chave
                        })
        
def python_para_java(classe, atributos):
    
    imports = ""
    nome_classe = [
        'class',
        classe,
    ]

    codigo = " ".join(nome_classe) + " {\n"

    if len(atributos['str']) > 0:
        for atributo in atributos['str']:
            codigo += f"\tString {atributo};\n"
    
    if len(atributos['list']) > 0:
        imports = 'import java.util.ArrayList;\n\n'
        for atributo in atributos['list']:
            codigo += f"\tArrayList<{atributo['tipo']}> {atributo['variavel']};\n"
    
    codigo += "}\n\n"


    return imports + codigo

def main():
    
    arquivo = le_arquivo("arquivo.json")

    for chave, valor in arquivo.items():
        monta_classes(chave, valor)


    codigo = ""
    for classe, atributos in classes.items():
        codigo += python_para_java(classe, atributos)


    codigo += main_java()

    print(codigo)

if __name__ == '__main__':
    main()