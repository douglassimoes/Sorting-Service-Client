from sortingalgorithm import SortingAlgorithm


class BooksSorter():
    
    def sort_books(self,books,rules):
        """
        This method call an algorithm for order the books list according to the rules.
        
        Arguments:
            books (list): Books to be sorted
            rules (dictionary): Rules for How to order the book list
            
        Returns:
            books(list): It returns a list of books sorted

        Exceptions:
            SSCException: When the order is null
        """

        if rules is None:
            raise SSCException
    
        return SortingAlgorithm.sort(self,books,rules)
    
    
class SSCException(Exception):
        '''trigger this when the order is null'''