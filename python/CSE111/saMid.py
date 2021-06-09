class Author:
    totalBooks=0
    def __init__(self,a=""):
        self.authorName=a
        self.genre=[]
        self.bookTitle=[[]]
    def setName(self,a):
        self.authorName=a
    def addBook(self,a,b):
        if self.authorName=="":
            print("A book can not be added without author name")
        else:
            Author.totalBooks+=1
            if b not in genre:
                self.genre.append(b)
                self.bookTitle[-1].append(a)
            else:
                for x in range(len(self.genre)):
                    if genre[x]==b:
                        self.bookTitle[x].append(a)
    def printDetail(self):
        print("Number of Book(s):",len(self.bookTitle))
        print("Author Name:",self.authorName)
        for a in range(len(self.bookTitle)):
            print(self.genre[a]+":",self.bookTitle[a])
print("Total Books: ", Author.totalBooks)
print("=================================")
a1 = Author()
print("=================================")
a1.addBook("Ice", "Science Fiction")z
print("=================================")
a1.setName("Anna Kavan")
a1.addBook("Ice", "Science Fiction")
a1.printDetail()
print("=================================")
a2 = Author("Humayun Ahmed")
a2.addBook("Onnobhubon", "Science Fiction")
a2.addBook("Megher Upor Bari", "Horror")
print("=================================")
a2.printDetail()
a2.addBook("Ireena", "Science Fiction")
print("=================================")
a2.printDetail()
print("=================================")
print("Total Books: ", Author.totalBooks)

"""
Total Books: 0
=================================
=================================
A book can not be added without author name
=================================
Number of Book(s): 1
Author Name: Anna Kavan
Science Fiction: Ice
=================================
=================================
Number of Book(s): 2
Author Name: Humayun Ahmed
Science Fiction: Onnobhubon
Horror: Megher Upor Bari
=================================
Number of Book(s): 3
Author Name: Humayun Ahmed
Science Fiction: Onnobhubon, Ireena
Horror: Megher Upor Bari
=================================
Total Books: 4
"""