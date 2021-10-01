# gerador_codigo_java

*Como usar:*

```bash
    $ python3 main.py --path <caminho-para-arquivo-json>
```

*Ver os comandos:*

```bash
    $ python3 main.py -h
```


O programa irá gerar uma arquivo main.java de acordo com o JSON passado como parâmetro.

Observações:

É possível criar atributos:
- String
- ArrayList\<String\>
- ArrayList\<Classes\>

sendo classes uma classe existente.

Quando uma chave no JSON possuir como valor, um atributo objeto (ou um array de objetos), o programa interpretará como uma nova classe e os atributos desse JSON serão os atributos dessa classe.

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

class Main {
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

class Main {
	public static void main (String args[]){}
}
```