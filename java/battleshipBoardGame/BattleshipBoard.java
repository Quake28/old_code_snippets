import java.util.* ;
import static java.lang.System.* ;
class Main
{
    public static void main(String[] args)
    {
        Scanner sc= new Scanner(in);
        int dimension = sc.nextInt();
        char waterSymbol = sc.next().charAt(0);
        
        BattleshipBoard x = new BattleshipBoard(dimension, waterSymbol);

        String str = sc.next();
        out.println(str);
        String[] y = str.split(" ");
        for(int m=0; m< y.length;m++) out.println(y[m]);

        /*
        x.addBoat();
        */

        sc.close();
    }
}

class BattleshipBoard
{
    BattleshipBoard(int dimension, char waterSymbol)
    {
        char player1Board[][] = new char[dimension][dimension];
        char player2Board[][] = new char[dimension][dimension];
        this.fill(player1Board,dimension,waterSymbol);
        this.fill(player2Board,dimension,waterSymbol);
        this.toString(player1Board,player2Board,dimension);
    }
    private void toString(char board1[][],char board2[][], int dimension)
    {
        for(int c=0; c<dimension; c++)
        {
            for(int d=0; d<dimension; d++)
            {
                if(d==0)
                {
                    out.println();
                }
                out.print(board1[c][d]);
            }
            out.print("\t");
            for(int e=0; e<dimension; e++)
            {
                out.print(board2[c][e]);
            }
        }
        out.println();
    }
    private void fill(char board[][], int dimension, char fillMaterial)
    {
        for(int a=0; a<dimension; a++)
        {
            for(int b=0; b<dimension; b++)
            {
                board[a][b]=fillMaterial;
            }
        }
    }
}