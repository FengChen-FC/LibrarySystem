from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Admin(db.Model):
    __tablename__ = 'admin'
    AdminID = db.Column(db.String(11), primary_key=True)
    UserID = db.Column(db.String(11), db.ForeignKey('user.UserID'))
    AName = db.Column(db.String(8), nullable=False)
    ContactInformation = db.Column(db.String(11), nullable=False)


class Book(db.Model):
    __tablename__ = 'book'
    BookID = db.Column(db.String(12), primary_key=True)
    CategoryID = db.Column(db.String(5), db.ForeignKey('book_category.CategoryID'))
    Title = db.Column(db.String(20), nullable=False)
    publishers = db.Column(db.String(20))
    Author = db.Column(db.String(20))
    Num = db.Column(db.Integer, nullable=False)
    Position = db.Column(db.String(8), nullable=False)


class BookCategory(db.Model):
    __tablename__ = 'book_category'
    CategoryID = db.Column(db.String(5), primary_key=True)
    CategoryName = db.Column(db.String(8), nullable=False)
    CategoryDescription = db.Column(db.String(20))


class Borrow(db.Model):
    __tablename__ = 'borrow_record'
    UserID = db.Column(db.String(11), db.ForeignKey('user.UserID'), primary_key=True)
    BookID = db.Column(db.String(12), db.ForeignKey('book.BookID'), primary_key=True)
    LoanDate = db.Column(db.Date)
    DueDate = db.Column(db.Date)
    ReturnDate = db.Column(db.Date)
    RenewalCount = db.Column(db.Integer)


class Reader(db.Model):
    __tablename__ = 'reader'
    ReaderID = db.Column(db.String(11), primary_key=True)
    UserID = db.Column(db.String(11), db.ForeignKey('user.UserID'))
    RName = db.Column(db.String(8), nullable=False)
    ContactInformation = db.Column(db.String(11), nullable=False)


class User(db.Model):
    __tablename__ = 'user'
    UserID = db.Column(db.String(11), primary_key=True)
    UserName = db.Column(db.String(20), nullable=False)
    Password = db.Column(db.String(20), nullable=False)
    UserRole = db.Column(db.String(8), nullable=False)

    admins = db.relationship('Admin', backref='user', lazy=True)
    readers = db.relationship('Reader', backref='user', lazy=True)
    borrow_records = db.relationship('BorrowRecord', backref='user', lazy=True)

    # Optionally define any additional constraints or methods here
