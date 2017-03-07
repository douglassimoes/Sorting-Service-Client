from operator import itemgetter

class SortingAlgorithm():
   
    def sort(self,books,rules):
        """
        This method sorts a list of books according to the rules described.
        Removing the algorithm from the sorter allow us to implement another 
        algorithms in the future if its necessary.
        
        Arguments:
            books (list): Books to be sorted
            rules (dictionary): Rules for How to order the book list
            
        Returns:
            books(list): It returns a list of books sorted
    
        """
        if not rules:
            books = []
            return books
        else:
            for rule in rules:
                if rule[1] == 0:
                    descending = True
                else:
                    descending = False
                books = sorted(books,key=itemgetter(rule[0]), reverse=descending)

        return books



    
        