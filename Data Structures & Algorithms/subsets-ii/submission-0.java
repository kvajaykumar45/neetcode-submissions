class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {

        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        generate(nums, 0, new ArrayList<>(), result);
        return result;        
    }
    public static void generate(int nums[], int index, List<Integer> subset, List<List<Integer>> result)
    {
        result.add(new ArrayList<>(subset));
        for(int i=index; i<nums.length; i++)
        {
            if(i>index && nums[i] == nums[i-1])
            {
                continue;
            }
            subset.add(nums[i]);
            generate(nums, i+1, subset, result);
            subset.remove(subset.size()-1); 
        }

    }
}
