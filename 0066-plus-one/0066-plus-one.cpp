class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int rem = 1;
        for(int i=digits.size()-1;i>=0;i--){
            int tmp = digits[i]+rem;
            digits[i] = tmp % 10;
            if(tmp ==10){
                rem =1;
            }
            else if(tmp >10){
                rem = tmp - digits[i];
            }else{
                rem = 0;
            }
        }
        if(rem ==1){
            digits.insert(digits.begin(),1);
        }
        
        cout << rem << "";
        return digits;
    }
};