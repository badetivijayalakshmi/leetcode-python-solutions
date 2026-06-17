class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> nMap = new HashMap<>();
        int n = nums.length;
        for(int i = 0; i < n; i++){
            int diff = target - nums[i];
            if(nMap.containsKey(diff)){
                return new int[]{nMap.get(diff),i};
            }
            nMap.put(nums[i],i);
        }
        return new int[]{};//No solution found
    }
}