from proxy import *

def main():
     # Create lightweight proxies instead of full image objects
    image1 = ImageProxy("photo1.jpg")
    image2 = ImageProxy("photo2.png")  # Never displayed
    image3 = ImageProxy("photo3.gif")

    print("\nGallery initialized. No images actually loaded yet.")
    print(f"Image 1 Filename: {image1.get_file_name()}")  # Does not trigger image load


    image1.display()  # Loads and displays the high-res image
    print()

    image1.get_file_name()  # Just gets the file name, no loading
    print()

    image3.display()  # Loads and displays the high-res image
    print()

    image2.display()  # Loads and displays the high-res image



if __name__ == "__main__":
    main()