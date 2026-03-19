from LRUCache import LRUCache
class DemoClass:
    @staticmethod
    def main():
        print('--------------------')
        lru_cache = LRUCache(capacity=3)
        lru_cache.put("Adi","123")
        lru_cache.put("Anu","345")
        lru_cache.put("Mee","678")

        print(lru_cache.get("Adi"))
        lru_cache.put("Sai", "987")

        print("Cache")
        print(lru_cache.print_cache())


        print('-------------------')


if __name__ == '__main__':
    DemoClass.main()