from URLShortenService import URLShotenService
from reporsitory.InMemURLRepo import InMemURLRepo
from strategies.RandomStrategy import RandomStrategy
def resolve_print(shortener, short_url):
    resolve_url = shortener.resolve(short_url)
    if resolve_url is not None:
        print(f"Resolved short URL {short_url} -> {resolve_url}")
    else:
        print(f"No original URL found for {short_url}")


def main():
    shortener = URLShotenService.get_instance()
    shortener.configure('http://short.ly/',RandomStrategy(), InMemURLRepo())
    print("--- URL Shortener Service Initialized ---\n")

    original_url1 = "https://www.verylongurl.com/with/lots/of/path/segments/and/query/params?id=123&user=test"
    print("Shortening: " + original_url1)
    short_url1 = shortener.shorten(original_url1)
    print("Generated Short URL: " + short_url1)
    print()

    print("Shortening the same URL again...")
    short_url2 = shortener.shorten(original_url1)
    print("Generated Short URL: " + short_url2)
    if short_url1 == short_url2:
        print("SUCCESS: The system correctly returned the existing short URL.\n")


    original_url2 = "https://www.anotherdomain.com/page.html"
    print("Shortening: " + original_url2)
    short_url3 = shortener.shorten(original_url2)
    print("Generated Short URL: " + short_url3)
    print()


    resolve_print(shortener, short_url1)
    resolve_print(shortener, short_url2)
    resolve_print(shortener, short_url3)


if __name__ == "__main__":
    main()