class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        Hashtable<Character, Integer> sSet = new Hashtable<>();
        Hashtable<Character, Integer> tSet = new Hashtable<>();
        for (int i = 0; i < s.length(); i++) {
            if (sSet.containsKey(s.charAt(i))) {
                int val = sSet.get(s.charAt(i));
                sSet.put(s.charAt(i), val + 1);
            }
            if (tSet.containsKey(t.charAt(i))) {
                int val = tSet.get(t.charAt(i));
                tSet.put(t.charAt(i), val + 1);
            }
            if (!sSet.containsKey(s.charAt(i))) {
                sSet.put(s.charAt(i), 0);
            }
            if (!tSet.containsKey(t.charAt(i))) {
                tSet.put(t.charAt(i), 0);
            }
        }
        return sSet.equals(tSet);
    }
}
