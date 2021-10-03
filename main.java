import java.util.ArrayList;

class Aluno {
	String nome;
	String cpf;
	String telefone;
	ArrayList<Turma> turmas;
}

class Turma {
	String codigo;
	String nome;
	Professor Professor;
}

class Professor {
	String nome;
}

class Main {
	public static void main (String args[]){}
}