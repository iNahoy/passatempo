package controle;

import java.util.Scanner;

public class Tabuada{
	public static void main(String[] args) {
		Scanner entry = new Scanner(System.in);

        System.out.println("Digite o número que você quer tirar a tabuada: ");
        int multiplicador = entry.nextInt();

        System.out.println("Até quanto você quer saber a tabuada do seu número? ");
        int vezes = entry.nextInt();

        int contador = 1;
        while (contador <= vezes) {
            int resultado = multiplicador * contador;
            System.out.printf("%d * %d = %d\n", multiplicador, contador, resultado);
            contador++;
        }
        entry.close();
	}
}