from composite import *

def main():

    #create leaf nodes
    file1 = File("file1.txt", 100)
    file2 = File("file2.txt", 200)
    photo = File("photo.jpg", 1500)
    video = File("video.mp4", 5000)

    #create composite nodes
    documents = Folder("Documents")
    pictures = Folder("Pictures")
    media = Folder("Media")

    root = Folder("Root")

    #build the tree structure
    documents.add(file1)
    documents.add(file2)


    pictures.add(photo)

    media.add(video)


    root.add(documents)
    root.add(pictures)
    root.add(media)

    #display the structure and sizes
    print("File System Structure:")
    root.print_structure()
    print()

    #delete a folder
    print("Deleting 'Documents' folder:")
    documents.delete()
    print()

    #display the structure after deletion
    print("File System Structure after deletion:")
    root.print_structure()
    print()


if __name__ == "__main__":
    main()

