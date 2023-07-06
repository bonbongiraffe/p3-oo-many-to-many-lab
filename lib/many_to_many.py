class Author:
    all = []

    def __init__( self, name ):
        self.name = name
        self.all.append(self)

    def contracts( self ):
        return [x for x in Contract.all if x.author == self]  

    def books( self ):
        return [x.book for x in Contract.all if x.author == self] 

    def sign_contract( self, book, date, royalties ):
        return Contract( self, book, date, royalties)  
    
    def total_royalties( self ):
        total = 0
        for contract in Contract.all:
            if contract.author == self:
                total += contract.royalties
        return total

class Book:
    all = []

    def __init__( self, title ):
        self.title = title
        self.all.append(self)

    def contracts( self ):
        return [x for x in Contract.all if x.book == self]
    
    def authors( self ):
        return [x.author for x in Contract.all if x.book == self]

class Contract:
    all = []
    def __init__( self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all.append(self)

    def contracts_by_date():
        return sorted(Contract.all, key=lambda contract: contract.date)

    #property methods follow:    
    def get_author( self ):
        return self._author
    
    def get_book( self ):
        return self._book

    def get_date( self ):
        return self._date
    
    def get_royalties( self ):
        return self._royalties
    
    def set_author( self, author ):
        if isinstance( author, Author):
            self._author = author
        else:
            raise Exception("")
    
    def set_book( self, book ):
        if isinstance( book, Book):
            self._book = book
        else:
            raise Exception("")

    def set_date( self, date ):
        if type(date) == str :
            self._date = date
        else:
            raise Exception("")
    
    def set_royalties( self, royalties ):
        if type(royalties) == int :
            self._royalties = royalties
        else:
            raise Exception("")
    
    author = property( get_author, set_author )
    book = property( get_book, set_book )
    date = property( get_date, set_date )
    royalties = property( get_royalties, set_royalties )