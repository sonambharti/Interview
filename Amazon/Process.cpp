/*

Find the minimum amount of main memory used
by all of your process after the deletion of a 
contiguous segment of size n.

Input:
n = 4
processes = [10, 4, 8, 1]
m = 2 #size of contiguoussegment to be deleted.

Output:
9

*/

#include <bits/stdc++.h>
using namespace std;

int minimizeMem(vector<int> process, int m){
    int sum = accumulate(process.begin(), process.end(), 0);
    int t = 0, ans = 0;
    
    for(int i=0; i<m; i++){
        t += process[i];
    }
    ans = t;
    for(int i=0; i<process.size(); i++){
        t += process[i];
        t -= process[i-m];
        ans = max(ans, t);
    }
    
    return sum-ans;
}

int main(){
    int n, m, el;
    vector<int> process;
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>el;
        process.push_back(el);
    }
    cin>>m;
    
    int res = minimizeMem(process, m);
    cout<<res;
    
    return 0;
}

