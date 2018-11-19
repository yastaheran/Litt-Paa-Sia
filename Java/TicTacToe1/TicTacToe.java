import java.util.Scanner;
public class TicTacToe {
	public static int rad, kolonne;
	public static Scanner sc = new Scanner(System.in);
	public static char[][] board = new char[3][3];
	public static char tur = 'X';
	
	public static void main(String[] args) {
		for(int i = 0; i < 3; i++) {
			for(int j = 0; j < 3; j++) {
				board[i][j] = '_';  //''-brukes når det er char
			}
		}
		Play();
	}
	public static void Play() {
		boolean spiller = true;
		PrintBoard();
		while(spiller) {
			System.out.println("Skriv inn rad og kolonne:");
			rad = sc.nextInt() - 1;
			kolonne = sc.nextInt() - 1;
			board[rad][kolonne] = tur;
			if(GameOver(rad, kolonne)) {
				spiller = false;
				System.out.println("Game over! Spiller " + tur + " vinner!");
			}
			PrintBoard();
			if(tur == 'X') {
				tur = 'O';
			} else {
				tur = 'X';
			}
		}
	}
	public static void PrintBoard() {
		for(int i = 0; i < 3; i++) {
			System.out.println();
			for(int j = 0; j < 3; j++) {
				System.out.print(" | " + board[i][j] + " | ");
			}
		}
		System.out.println();
	}
	public static boolean GameOver(int rMove, int cMove) {
		if(board[0][cMove] == board[1][cMove] && board[0][cMove] == board[2][cMove])
			return true;
		if(board[rMove][0] == board[rMove][1] && board[rMove][0] == board[rMove][2] && board[1][1] != '_')
			return true;
		if(board[0][2] == board[1][1] && board[0][2] == board[2][0] && board[1][1] != '_')
			return true;
		return false;
	}
}
