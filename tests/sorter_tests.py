import unittest

import os.path, sys

# Just adding the bookssorter directory path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + '/src')

from bookssorter import BooksSorter, SSCException

books = [
    {
        'id': 1,
        'title': 'Java How to Program',
        'author': 'Deithel & Deithel',
        'edition year': 2007
    },
    {
        'id': 2,
        'title': 'Patterns of Enterprise Application Architeture',
        'author': 'Martin Fowler',
        'edition year': 2002
    },
    {
        'id': 3,
        'title': 'Head First Design Patterns',
        'author': 'Elisabaeth Freeman',
        'edition year': 2004
    },
    {
        'id': 4,
        'title': 'Internet & World Wide Web: How to Program',
        'author': 'Deithel & Deithel',
        'edition year': 2007
    }
]

def get_ids_list_from(books):
        ids_list = []
        for book in books:
            ids_list.append(book['id'])
        return ids_list

class BooksSorterTest(unittest.TestCase):
    
    def test_title_ascending(self):
        rules = [['title',1]]
        bookssorter = BooksSorter()
        books_test = bookssorter.sort_books(books,rules)
        myresult = []
        
        myresult = get_ids_list_from(books_test)
        
        correct_result = [3,4,1,2]
        
        self.assertEqual(correct_result,myresult)
        
    def test_author_ascending_title_descending(self):
        rules = [['title',0],['author',1]]
        bookssorter = BooksSorter()
        books_test = bookssorter.sort_books(books,rules)
        myresult = []
        
        myresult = get_ids_list_from(books_test)
        
        correct_result = [1,4,3,2]
        
        self.assertEqual(correct_result,myresult)
        
    def test_edition_descending_author_descending_title_ascending(self):
        rules = [['author',0],['title',1],['edition year',0]]
        bookssorter = BooksSorter()
        books_test = bookssorter.sort_books(books,rules)
        myresult = []
        
        myresult = get_ids_list_from(books_test)
        
        correct_result = [4,1,3,2]
        
        self.assertEqual(correct_result,myresult)
        
    def test_null(self):
        rules = None
        bookssorter = BooksSorter()
        
        self.assertRaises(SSCException, bookssorter.sort_books,books,rules)
        
    def test_empty_set(self):
        rules = []
        bookssorter = BooksSorter()
        books_test = bookssorter.sort_books(books,rules)
        myresult = []
        
        myresult = get_ids_list_from(books_test)
        
        correct_result = []
        
        self.assertEqual(correct_result,myresult)
        
    def test_title_descending(self):
        rules = [['title',0]]
        bookssorter = BooksSorter()
        books_test = bookssorter.sort_books(books,rules)
        myresult = []
        
        myresult = get_ids_list_from(books_test)
        
        correct_result = [2,1,4,3]
        
        self.assertEqual(correct_result,myresult) 
        
    def test_title_ascending_author_descending(self):
        rules = [['title',1],['author',0]]
        bookssorter = BooksSorter()
        books_test = bookssorter.sort_books(books,rules)
        myresult = []
        
        myresult = get_ids_list_from(books_test)
        
        correct_result = [2,3,4,1]

        self.assertEqual(correct_result,myresult)   
        
    def test_edition_ascending_author_ascending_title_descending(self):
        rules = [['author',1],['title',0],['edition year',1]]
        bookssorter = BooksSorter()
        books_test = bookssorter.sort_books(books,rules)
        myresult = []
        
        myresult = get_ids_list_from(books_test)
        
        correct_result = [2,3,1,4]
        
        self.assertEqual(correct_result,myresult)    

    
if __name__ == '__main__':
    unittest.main()