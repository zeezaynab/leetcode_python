import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        List<Integer> res = new ArrayList<>();
//iterating through first array
        for(int i : nums1){
//iterating thorugh second array
            for(int j : nums2){
                if(i==j){
//checking for duplicates
                    if(!res.contains(i)){
                        res.add(i);
                    }
                    break;
                }
            }
        }
        int[] result = new int[res.size()];
        for(int k=0; k<res.size(); k++){
            result[k] = res.get(k);
        }
        return result;
    }
}

