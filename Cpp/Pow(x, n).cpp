// https://leetcode.com/problems/powx-n/
// LeetCode 50. Pow(x, n)


// Solution :


class Solution {
public:
    double myPow(double x, int n) {
        if(n==0) return 1;
        if(n%2==0){
            double ans = myPow(x,n/2);
            return ans*ans;
        }
        else{

            if(n>0){
                double ans = myPow(x,n-1);
                return x*ans;
            }
            else{
                double ans = myPow(x,n+1);
                return ans/x;    
            }
        }
    }
};
