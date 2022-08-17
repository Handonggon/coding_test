import java.util.HashMap;

class Solution {
    static public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        HashMap<String, Integer> wantHashMap = new HashMap<String, Integer>();
        for (int i = 0; i < want.length; i++) {
            wantHashMap.put(want[i], number[i]);
        }
        for (int i = 0; i <= discount.length - 10; i++) {
            HashMap<String, Integer> discountHashMap = new HashMap<String, Integer>();
            int count = 0;
            for (int j = i; j < i + 10; j++) {
                discountHashMap.put(discount[j], discountHashMap.getOrDefault(discount[j], 0) + 1);
            }
            for (String st : want ) {
                if(wantHashMap.get(st) == discountHashMap.get(st)){
                    count++;
                }else{
                    break;
                }
            }
            if (count == want.length)
                answer++;
        }
        return answer;
    }
}