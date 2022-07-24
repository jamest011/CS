'''
Week 12 Team Activity
'''


user_pick = input('What scripture would you like to know about? ')
max_chapters = -1
max_book = ''
min_chapters = 99999999
min_book = ''

with open('books_and_chapters.txt') as book_file:
    for line in book_file:
        # Scripture: Old Testament, Book: Genesis, Chapters: 50
        parts = line.split(':')

        book = parts[0].strip()
        chapters = float(parts[1])
        scripture = parts[2].strip()

        if scripture.lower() == user_pick.lower():
            print(
                f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")

            if chapters > max_chapters:
                max_chapters = chapters
                max_book = book
            if chapters < min_chapters:
                min_chapters = chapters
                min_book = book
print()
print(
    f'The book with the most chapters is {max_book} with {max_chapters} chapters.')
print(
    f'The book with the least chapters is {min_book} with {min_chapters} chapters.')
