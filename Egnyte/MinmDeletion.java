//Minimum Deletion
/*You are given a string s consisting only of characters 'a' and 'b',

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced. */

import java.util.*;

public class MinmDeletion
{
    
    public static int solution(String S){
        int res=0;
        Stack<Character> st=new Stack<>();
        for(int j=0;j<S.length();j++){
            if(st.isEmpty()){
                st.push(S.charAt(j));
            }
            else if(!st.isEmpty() && S.charAt(j)=='a' && st.peek()=='b'){
                st.pop();
                res++;
            }
            else{
                st.push(S.charAt(j));
            }
        }
        return res;
    }
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    String S;
	    S = sc.nextLine();
	    
	    System.out.println("Minimum No. of deletion = "+ solution(S));
	}
}
