#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> rank,parent;
    int find(int i){
        if(parent[i]==i) return i;
        else{
            int r=find(parent[i]);
            parent[i]=r;
            return r;
        }
    }
    void union_(vector<int> a){
        int i=a[0],j=a[1];
        int irep=find(i),jrep=find(j);
        if(irep==jrep) return;

        int irank=rank[irep],jrank=rank[jrep];
        if(irank<jrank){
            parent[irep]=jrep;
        }
        else if(jrank<irank){
            parent[jrep]=irep;
        }
        else{
            parent[jrep]=irep;
            rank[irep]++;
        }
    }
    int makeConnected(int n, vector<vector<int>>& connections) {

        if(connections.size()<n-1) return -1;
        for(int i=0;i<n;i++){
            parent.push_back(i);
            rank.push_back(0);
        }
        for(int i=0;i<connections.size();i++){
            union_(connections[i]);
        }
        int c=0;
        for(int i=0;i<n;i++){
            parent[i]=find(i);
        }
        unordered_set<int> xset;
        for(int i=0;i<parent.size();i++){
            if(xset.find(parent[i])==xset.end()){
                xset.insert(parent[i]);
                c++;
            }
        }
        return c-1;
    }
};