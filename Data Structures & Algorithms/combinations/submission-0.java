class Solution {
    public List<List<Integer>> combine(int n, int k) {
        
        List<List<Integer>> result = new ArrayList<>();
        generate(n, k, 1, new ArrayList<>(), result);
        return result;
    }

    static void generate(int n, int k, int index, List<Integer> comb, List<List<Integer>> result)
    {
        if(comb.size() == k)
        {
            result.add(new ArrayList<>(comb));
            return;
        }
        for(int i=index; i<=n; i++)
        {
        comb.add(i);
        generate(n, k, i+1, comb, result);
        comb.remove(comb.size()-1);
        }
    }
}