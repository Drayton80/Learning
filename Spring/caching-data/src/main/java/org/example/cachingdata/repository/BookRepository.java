package org.example.cachingdata.repository;

import org.example.cachingdata.model.Book;

public interface BookRepository {

    Book getByIsbn(String isbn);

}
