
class Entry:
    def __init__(self, k ,v):
        self._key=k
        self._value=v
    def __str__(self):
        return str(self._value)

def CyclicShiftHashCode(str_key): # str_key is string 
    mask= (1 << 32) -1 # limit to 32‐bit integers
    h=0
    for ch in str_key:
        h= (h <<5& mask) | (h >> 27) # cyclic shift hash code
        h += ord(ch) #아스키 코드로 변환
    return h

class Bucket(Entry):
    def __init__(self):
        self._bucket=[] 
    def _getitem(self, k):
        for item in self._bucket: 
            if k == item._key:
                return item._value
        return None
    def _setitem(self, k, v):
        for item in self._bucket: 
            if k == item._key:
                item._value =v
                return
        self._bucket.append(Entry(k, v))

    def _delitem(self,k):
        for j in range(len(self.bucket)):
            if k==self._bucket[j]._key:
                self._bucket.pop(j)
                return 1
        return None
    def __len__(self):
        return len(self._bucket)

    def __iter__(self): 
        for item in self._bucket:
            yield item._key

class HashMap_Bucket(Bucket):
    def __init__(self, table_size=11, prm=109345121): 
        self._hash_tbl = table_size * [None] #버킷 리스트 생성
        self._hash_tbl_size = table_size  #버킷 개수
        self._num_entry = 0
        self._prime = prm

    def _hash_value(self, k):
        return CyclicShiftHashCode(k) % self._prime % self._hash_tbl_size #hash value를 구한다.
    def __len__(self):
        return self._num_entry
    def _getitem(self,k):
        hv=self._hash_value(k)
        bucket=self._hash_tbl[hv]
        return bucket._getitem(k)
    def _setitem(self, k, v): 
        hv = self._hash_value(k) 
        if self._hash_tbl[hv] is None: 
            self._hash_tbl[hv]= Bucket() #버킷 추가
        bucket= self._hash_tbl[hv] #버킷안에 entry를 추가
        bucket._setitem(k, v) 
        
    def _delitem(self, k): 
        hv = self._hash_value(k) 
        bucket= self._hash_tbl[hv] 
        bucket._delitem(k) 
        self._num_entry -=1
    
    def __str__(self): 
        s=''
        for h in range(len(self._hash_tbl)): 
            bucket= self._hash_tbl[h] 
            if bucket is not None:
                s += "bucket[{:2d}] : ".format(h) 
                for item in bucket:
                    s += str(item)+ ", " 
                s += "\n "  
        return s

    def num_table(self,key):
        result= CyclicShiftHashCode(key)% self._prime % self._hash_tbl_size
        
        return result
        #for h in range(len(self._haxh_tal)):
        #    bucket=self._hash_tbl[h]


if __name__=="__main__":
    HashMap_Capacity =10
    print("Creating a HashMap_Bucket of capacity ({})".format(HashMap_Capacity))
    hsMap = HashMap_Bucket(table_size = HashMap_Capacity) #해시 테이브 생성

    student_records = [ ("Kim", 19345, "ICE",4.0), ("Park", 18234, "CS", 4.2),
        ("Hong", 20456, "EE" , 3.9), ("Lee", 20987, "ME", 3.8),
        ("Yoon", 21654, "ICE", 3.7), ("Moon", 21001, "CHEM", 4.1) ,("Hwang", 21123, "CE", 3.7),
        ("Choi", 19003, "EE", 4.3), ("Yeo", 20234, "ME", 3.8),("Jeong", 18005, "PH", 4.3) ]
         
    for i in range(len(student_records)): 
        st_record = student_records[i]
        st_name = st_record[0] 
        hsMap._setitem(st_name, st_record) 
    print("Current HashMap Internal Structure:\n", hsMap)

    print("Checking entry searching in HashMap") 
    for i in range(len(student_records)):
        st_name = student_records[i][0] 
        st_record = hsMap._getitem(st_name) 
        print("key ({}) : Value ({})".format(st_name, st_record))

    while True:
        name=input("\ninput student name to search (. to quit) : ")
        if name=='.':
            break

        index=hsMap.num_table(name)
        st_value=hsMap._getitem(name)
        print("key({}) => hash_tbl[{}]".format(name,index))
        print("key ({}) : {}".format(name,st_value))





        



