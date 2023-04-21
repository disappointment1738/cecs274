import Book
import ArrayList
# import ArrayQueue
# import RandomQueue
import SLLQueue
import DLList
import MaxQueue
#import SLLQueue
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
#import AdjacencyList
import time


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''

    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = MaxQueue.MaxQueue()
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()

    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f: # does this mean "For each row i in books.txt" ?
                (key, title, group, rank, similar) = line.split("^")
                b = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(b)
                self.sortedTitleIndices.add(key, self.bookCatalog.size() - 1)
            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = MaxQueue.MaxQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = MaxQueue.MaxQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def searchBookByInfix(self, infix: str, cnt: int):
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
            cnt: An int
        '''
        start_time = time.time()
        # keeping track of num of results (i.e., book titles containing infix)
        count = 0
        # iterate over the book catalog 
        for book in self.bookCatalog:
            # checking if a book title contains what the user is searching for <-- i.e., if infix is in title
            if infix in book.title:
                print(book)
                count += 1
                # checking if the num of results (count) is valid (i.e., less than or equal to cnt)
                # this is keeping track of the amount of book titles that are being printed
                if count == cnt:  
                    break
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def getCartBestSeller(self):
        """
        prints the title of the best booker seller amongst the rest of the books in the cart
        """
        start_time = time.time()
        title = self.shoppingCart.max().title
        elapsed_time = time.time() - start_time
        print(title)
        print(f"Completed in {elapsed_time} seconds")
    
    def addBookByKey(self, key):
        """
        adds the book with the given key to the shopping cart
        """
        start_time = time.time()
        book = self.bookIndices.find(key) # finds the book from given key
        if book is not None: # checks if the index exists
            self.shoppingCart.add(self.bookCatalog.get(book)) # adds to cart from the book catalog
            print(f"Added title: {self.bookCatalog.get(book).title}")
        else:
            print("Book not found.")
        elapsed_tme = time.time() - start_time
        print(f"addBookByKey Completed in {elapsed_tme} seconds")

    def addBookByPrefix(self, prefix):
        """
        adds the first matched book containing prefix in the title
        Book titles are sorted in alphabetical order
        """
        book = self.sortedTitleIndices.find_smallest_greater_node(prefix)
        if book.k[0:len(prefix)] == prefix and len(prefix) > 0:
            self.shoppingCart.add(self.bookCatalog.get(book.v))
            print(f'Added first matched title: {book.k}')
        else:
            print('Error: Prefix was not found.')
    
    def bestsellers_with(self, infix, structure, n=0):
        best_sellers = None

        if structure == 1:
            best_sellers = BinarySearchTree.BinarySearchTree()
        elif structure == 2:
            best_sellers = BinaryHeap.BinaryHeap()
        else:
            print("Invalid data structure.")
            return None

        if best_sellers is not None:
            if n == "":
                n = 0
            n = int(n)
            if infix == "":
                print("Invalid infix.")
                return None
            elif n < 0:
                print("Invalid number of titles.")
                return None
            else:
                start_time = time.time()

                if structure == 1:
                    for book in self.bookCatalog:
                        if infix in book.title:
                            best_sellers.add(book.rank, book)
                    bs = best_sellers.in_order()
                    bs.reverse()

                    if n == 0:
                        for book in bs:
                            print(book.v)
                    else:
                        n2 = n
                        for book in bs:
                            if n2 == 0:
                                break
                            print(book.v)
                            n2 -= 1

                if structure == 2:
                    for book in self.bookCatalog:
                        if infix in book.title:
                            book.rank = book.rank * -1
                            best_sellers.add(book)
                    if n == 0:
                        for book in range(best_sellers.size()):
                            book = best_sellers.remove()
                            book.rank *= -1
                            print(book)
                    else:
                        n2 = n
                        while not best_sellers.size() == 0 and n2 > 0:
                            book = best_sellers.remove()
                            book.rank = book.rank * -1
                            print(book)
                            n2 -= 1

                elapsed_time = time.time() - start_time
                print(f"Displayed bestsellers_with({infix}, {structure}, {n}) in {elapsed_time} seconds")
