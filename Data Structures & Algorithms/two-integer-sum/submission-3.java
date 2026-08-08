class Solution {
    public int[] twoSum(int[] nums, int target) {
        Hashtable<Integer, Integer> sumTable = new Hashtable<>();
        int[] result = {0, 0};
        for (int i = 0; i < nums.length; i++) {
            int comp = target - nums[i];
            if (sumTable.containsKey(nums[i]) && (comp + nums[i] == target)) {
                result[0] = sumTable.get(nums[i]);
                result[1] = i;
                return result;
            }
            sumTable.put(comp, i);
        }
        return result;
    }
}
