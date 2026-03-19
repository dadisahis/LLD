LRU Cache

Functional Requirements:
1. Support get(Key) and put(key, val) 
2. if cache extends capacity, evict the LRU
3. Both get and put should update the recency in Access
4. Key and value should be generic


NFR
1. Get and Put operation should be O(1)
2. Thread Safety: Implementation should be thread safe for concurrent env
3. Modularity: OOPs principle should be followed
4. Memory Efficient: Internal Data structures should space and speed optimized


Entites:
1. Node
2. DoublyLinkedList
3. LRUCache

Data Structures being used:
1. Map
2. DLL
