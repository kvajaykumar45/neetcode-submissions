class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        
        List<List<Integer>> result = new ArrayList<>();
        generate(nums, 0, new ArrayList<>(), result);
        return result;
    }

    public static void generate(int nums[], int index, List<Integer> subset, List<List<Integer>> result)
    {
        if(index == nums.length)
        {
            result.add(new ArrayList<>(subset));
            return;
        }

        subset.add(nums[index]);
        generate(nums, index+1, subset, result);
        subset.remove(subset.size() -1);
        generate(nums, index+1, subset, result);
    }
}
