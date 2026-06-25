class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> seenlist = new HashSet<>();
        for(int num : nums){
            if(seenlist.contains(num))
                return true;
            seenlist.add(num);
        }
        return false;
    }
}