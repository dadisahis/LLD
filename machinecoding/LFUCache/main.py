from LFUCache import LFUCache
def main():
    cache = LFUCache(capacity=3)
    cache.put(1, 3)
    cache.put(2, 4)
    cache.put(5, 6)

    print(cache.print_cache())
    print(cache.get(2))
    print(cache.get(1))
    print(cache.get(2))

    cache.put(4,8)

    print(cache.print_cache())

if __name__ == '__main__':
    main()