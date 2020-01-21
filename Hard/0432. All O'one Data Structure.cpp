using namespace std;

set<pair<int,string>> s;
unordered_map<string,int> mp;

class AllOne {
public:
    /** Initialize your data structure here. */
    AllOne() {
        mp.clear();
        s.clear();
    }
    
    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    void inc(string key) {
        if (mp.find(key) == mp.end()){
            mp[key] = 1;
            s.insert({mp[key],key});
            return;
        }
        s.erase({mp[key],key});
        mp[key] += 1;
        s.insert({mp[key],key});
        cout << key << " " << mp[key] << "\n";
    }
    
    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    void dec(string key) {
        if (mp.find(key) == mp.end()) return;
        if (mp[key]){
            s.erase({mp[key],key});
            mp[key]--;
        }
        if (mp[key]){
            s.insert({mp[key],key});
        }
        cout << key << " " << mp[key] << "\n";
    }
    
    /** Returns one of the keys with maximal value. */
    string getMaxKey() {
        if (s.empty()) return "";
        return (*(s.rbegin())).second; 
    }
    
    /** Returns one of the keys with Minimal value. */
    string getMinKey() {
        if (s.empty()) return "";
        return (*(s.begin())).second; 
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */
