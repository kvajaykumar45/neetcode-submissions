class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        generate(n, n, "", result);
        return result;        
    }
    public static void generate(int open, int close, String exp, List<String> result)
    {
        if(open == 0 && close == 0)
        {
            result.add(exp);
            return;
        }
        if(open > 0)
            generate(open-1, close, exp+"(", result );
        
        if(open < close)
            generate(open, close-1, exp+")", result);

    }
}
