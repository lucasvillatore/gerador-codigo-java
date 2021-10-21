# Gerador de código Java

Esse relatório tem como objetivo explicar como utilizar o programa de geração de código Java a partir de um arquivo JSON.
Também lista as ferramentas, detalhes de como funciona a implementação do algoritmo e também exemplos de entrada e saídas.

**Como usar:**

```bash
    $ python3 main.py --path <caminho-para-arquivo-json>
```

**Compilar código Java:**

```bash
	$ javac main.java
```

**Executar código Java:**

```bash
	$ java Principal.java
```

**Ver os comandos:**

```bash
    $ python3 main.py -h
```


### Ferramentas
- Python3
- Libs: 
  - json
  - argparse

### Detalhes de implementação
O programa irá gerar uma arquivo main.java de acordo com o JSON passado como parâmetro.
Utilizei python3 porque é uma linguaguem que já tenho familiaridade. Utilizo as libs json e argparse para manipulação de arquivos JSON e manipulação de argumentos de entrada.

**Implementação**

É possível criar atributos:
- String
- ArrayList\<String\>
- ArrayList\<Classes\>

sendo classes uma classe existente.

Quando uma chave no JSON possuir como valor, um atributo objeto (ou um array de objetos), o programa interpretará como uma nova classe e os atributos desse JSON serão os atributos dessa classe.
Para montar todas as classes do código Java, faço uma busca em profundidade nos atributos JSON e monto um grafo de dependências e, a partir desse grafo, eu gero o código Java resultante.


Entradas de exemplo:
```json
{
    "Aluno": [
        {
            "nome": "José",
            "cpf": "12341234",
            "telefone": "9999999",
            "Turma": [
                {
                    "codigo": "ci1030",
                    "sala": "a"
                },
                {
                    "codigo": "ci1031",
                    "sala": "b"
                }

            ]
        },
        {
            "nome": "Lucas",
            "cpf": "12345678",
            "telefone": "9999999",
            "Turma": [
                {
                    "codigo": "ci1030",
                    "sala": "A"
                },
                {
                    "codigo": "ci1031",
                    "sala": "a"
                }
            ]
        }
    ]
}
```
Saida:

```java
import java.util.ArrayList;

class Aluno {
	String nome;
	String cpf;
	String telefone;
	ArrayList<Turma> turmas;
}

class Turma {
	String codigo;
	String sala;
}

class Programa {
	public static void main (String args[]){}
}
```

Entrada:
```json
{
    "Aluno": [
        {
            "nome": "José",
            "cpf": "12341234",
            "telefone": "9999999",
            "Amigo": [
              "lucas",
              "joao"
            ]
        },
        {
            "nome": "Lucas",
            "cpf": "12345678",
            "telefone": "9999999",
            "Amigo": [
                "joao",
                "jose"  
              ]
        }
    ]
}
```

Saída:
```java
import java.util.ArrayList;

class Aluno {
	String nome;
	String cpf;
	String telefone;
	ArrayList<String> amigos;
}

class Programa {
	public static void main (String args[]){}
}
```