/*Take an integer array A of size N and int array for Query of size Q.
For each query, we have to find the no. of pairs (L,R) such that the bitwise
or of all A_i is equal to X.
*/

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, q, el, el1;
    cin>>n>>q;
    vector<int> A;
    vector<int> X;
    pair<int, int> p, Q;
    set<pair<int, int>> S;
    
    for(int i=0; i<n; i++){
        cin>>el;
        A.push_back(el);
    }
    
    for(int i=0; i<q; i++){
        cin>>el1;
        X.push_back(el1);
    }
    
    for(int k=0; k<q; k++){
        S.clear();
        for(int i=0; i<n; i++){
            for(int j=0;j<n;j++){
                if((A[i] | A[j]) == X[k]){
                    p.first = A[i];
                    p.second = A[j];
                    Q.first = A[j];
                    Q.second = A[i];
                    if(S.find(Q) != S.end()){
                        continue;
                    }
                    else{
                        S.insert(p);
                    }
                    
                }
            }   
        }
        cout<<S.size()<<endl;
    }
    
    return 0;
}