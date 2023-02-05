class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> v;
        map<int, int> m;
        for(int i=0; i<nums.size(); i++){
            m[nums[i]]++;
        }

        int max, ans = 0, count = 0;
        while(count < k){
            max = 0;
            for(auto i=m.begin(); i!=m.end(); i++){
                if(i->second > max){
                    max= i->second;
                    ans = i->first;
                }
            }

            v.push_back(ans);
            m.erase(ans);
            count++;
        }

        return v;
    }
};
