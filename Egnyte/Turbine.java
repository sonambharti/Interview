//Turbine Question

import java.util.*;
import java.io.*;
import static java.lang.Math.*;

public class Turbine
{
    public static void helper(int[][] A, int x, int y, int K){
        int r = A.length;
	    int c = A[0].length;
	    int p = max(0, x-K), q = min(r, x+K+1);
	    while(p < q)
	    {
		    int a = K-abs(p-x), b = max(0, y-a), f = min(c, y+a+1);
		    while(b < f)
		    {
    			if(A[p][b] == 0)
	    			A[p][b] = 2;
		    	b++;
		    }
		    p++;
	    }
    }
    
    public static int solution(int[][] A, int K){
        int r = A.length;
	    int c = A[0].length;
        int res = 0;
	    for(int i=0; i<r; i++)
	    {
		    for(int j=0; j<c; j++)
		    {
			    if(A[i][j] == 1)
				    helper(A, i, j, K);
		    }
	    }
        for(int i=0; i<r; i++)
	    {   
		    for(int j=0; j<c; j++)
		    {
			    if(A[i][j] == 0)
				    res++;
		    }
	    }
        return res;
    }
    
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
	    int[][] A = new int[3][4];
	    for(int i=0; i<3; i++){
	        for(int j=0; j<4; j++){
	            A[i][j] = sc.nextInt();
	        }
	    }
	    
	    int K;
	    K = sc.nextInt();
	    //solution(int [][]A, int K);
	    
	    System.out.println("Maximum No of Wind Turbines = "+ solution(A, K));
	}
}
