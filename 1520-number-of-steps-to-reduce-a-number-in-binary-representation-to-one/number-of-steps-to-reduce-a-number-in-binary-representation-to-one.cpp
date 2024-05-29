#include <string>
#include <cmath>

class Solution {
public:
    int numSteps(std::string s) {
        int k = 0;
        while (s != "1") {
            if (s.back() == '0') {
                s.pop_back();  
            } else {
                int i = s.length() - 1;
                while (i >= 0 && s[i] == '1') {
                    s[i] = '0'; 
                    i--;
                }
                if (i >= 0) {
                    s[i] = '1'; 
                } else {
                    s = '1' + s;
                }
            }
            k++;
        }
        return k;
    }
};
