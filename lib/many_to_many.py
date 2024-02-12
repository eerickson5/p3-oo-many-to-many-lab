class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        Contract.all.append(contract)
        return contract

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def total_royalties(self):
        total_royalties = 0
        for contract in self.contracts():
            total_royalties += contract.royalties
        return total_royalties

class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        
        self.author = author
        self.book = book
        
        if type(date) != str or type(royalties) != int:
            raise Exception
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)


    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]


    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception
