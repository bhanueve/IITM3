select title from book_catalogue as bc inner join book_authors as ba on bc.isbn_no = ba.isbn_no where ba.author_fname = 'Joh Paul' and ba.author_lname = 'Mueller' order by title;
