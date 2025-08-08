# Write a function book_info(title, author, year) that prints book details.Call the function using
# keyword arguments in different orders.

def book_info(title, author, year):
    print(f"Title : {title} \nAuthor : {author} \nYear : {year}")

print(book_info(author="Laxmi Prasad Devkota", year= 1997, title="Muna Madan"))
print()
print(book_info(year=2008, author="Prem Raj Khadka", title="Test Book"))
print()
print(book_info(title="Test Book 2", author="Prem Raj Khadka", year=2023))