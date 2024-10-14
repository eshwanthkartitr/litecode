class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        int cnt = 0;
        sort(g.begin(),g.end());
        sort(s.begin(),s.end());
        int p1=0;
        int p2=0;
        while(p1<g.size() and p2<s.size()){
            if(g[p1]>s[p2]){
                p2++;
            }else{
                p1++;
                p2++;
            }
        }  
        return p1;
    }
};