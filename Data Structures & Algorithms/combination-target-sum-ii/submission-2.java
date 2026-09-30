class Solution {
    static List<List<Integer>> result = new ArrayList<>();
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        result.clear();
        Arrays.sort(candidates);
        int index = 1;
        generate(candidates, target, 0, 0, new ArrayList<>());
        return result;
    }
    static void generate(int nums[], int target, int index, int sum, List<Integer> subset)
    {
        if(sum == target)
        {
            result.add(new ArrayList<>(subset));
            return;
        }
        if(sum > target || index == nums.length)
            return;
        for(int i=index; i<nums.length; i++)
        {
            if(i>index && nums[i] == nums[i-1])
                continue;
            else
            {
            subset.add(nums[i]);
            sum = sum + nums[i];
            generate(nums, target, i+1, sum, subset);
            subset.remove(subset.size()-1);
            sum = sum - nums[i];

            }
        }
    }
}
