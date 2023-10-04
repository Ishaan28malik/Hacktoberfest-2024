class MyHashMap {
    struct Node{
        int key{};
        int value{};
    };
    const static int size = 1000;
    vector<vector<Node>> table;

    int hashFunction(int key, int f_size = size){
        return key % f_size;
    }
public:
    
    MyHashMap() {
        table.resize(size);
    }
    
    void put(int key, int value) {
        int hash_key = hashFunction(key);
        //update exist key
        if(!table[hash_key].empty()){
            for(int i = 0; i < table[hash_key].size(); i++){
                if(table[hash_key][i].key == key){
                    table[hash_key][i].value = value;
                    return;
                }
            }
        }
        table[hash_key].push_back({key, value});
    }
    
    int get(int key) {
        int hash_key = hashFunction(key);
        for(int i = 0; i < (int)table[hash_key].size(); i++){
            if(table[hash_key][i].key == key)
                return table[hash_key][i].value;
        }
        return -1;
    }
    
    void remove(int key) {
        // get hash_key
        int hash_key = hashFunction(key);
        for(int i = 0; i < (int)table[hash_key].size(); i++){
            if(table[hash_key][i].key == key){
                swap(table[hash_key][i], table[hash_key].back());
                table[hash_key].pop_back();
            }
        }
    }
};

