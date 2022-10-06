//this is a recursive solution to output the prefix sum of an array.
// int arr[] ={1,2,3,4,5,6} = 21

#include <bits/stdc++.h>

using namespace std;

int prefixSum(int arr[] ,int n){
    if (n<0) return 0;
    return prefixSum(arr,n-1)+arr[n];

}

int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cout<<prefixSum(arr,n-1);
    return 0;
}
