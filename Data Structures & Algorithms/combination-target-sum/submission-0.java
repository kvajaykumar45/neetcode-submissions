class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        generate(nums, target, 0, 0, new ArrayList<>(), result);
        return result;
    }

    static void generate(int nums[], int target, int index, int sum, List<Integer> comb, List<List<Integer>> result)
    {
        if(sum == target)
        {
            result.add(new ArrayList<>(comb));
            return;
        }        
        if(sum > target || index == nums.length)
        {
            return;
        }

        comb.add(nums[index]);
        sum = sum+nums[index];
        generate(nums, target, index, sum, comb, result);

        comb.remove(comb.size()-1);
        sum = sum - nums[index];
        generate(nums, target, index+1, sum, comb, result); 
    }
}
