// Backtracking program to print all permutations of a string

public class Solution {

    private void permute(String s, int l, int r)
    {
        
        if (l == r)
            System.out.print(s + " ");
        else {
            
            for (int i = l; i <= r; i++) {
                    str = swap(s, l, i);
                    permute(s, l + 1, r);
                    str = swap(s, l, i);
            }
        }
}
    public String swap(String a, int i, int j)
    {
        char temp;
        char[] charArray = a.toCharArray();
        temp = charArray[i];
        charArray[i] = charArray[j];
        charArray[j] = temp;
        return String.valueOf(charArray);
    }
    public static void main(String[] args)
    {
        String s = "ABC";
        int n = s.length();
        Solution permutation = new Solution();
        permutation.permute(s, 0, n - 1);
    }
}
