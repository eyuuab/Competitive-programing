class Solution {
public:
    int subarraySum(vector<int>& arr, int k) {
        unordered_map<int,int>mp;
        int ans=0,pref=0;
        mp[0]=1;
        for(int i=0;i<arr.size();i++){
            pref+=arr[i];
           ans+=mp[pref-k];
           mp[pref]++;
        }
        return ans;
    }
};
