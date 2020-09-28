package org.example.cachingdata.repository;

import org.example.cachingdata.model.Book;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Component;

@Component
public class SimpleBookRepository implements BookRepository {

    @Override
    // Define que o método usará caching e a cache em questão
    // terá o nome de books atribuido a ela
    @Cacheable("books")
    // Obtém um livro baseado em seu isbn, uma espécie de ID
    public Book getByIsbn(String isbn) {
        simulateSlowService();
        return new Book(isbn, "Some book");
    }

    // Basicamente simula um acesso lento ao serviço para
    // demonstrar a maior eficiência da utilização de caching
    private void simulateSlowService() {
        try {
            long time = 3000L;
            Thread.sleep(time);
        } catch (InterruptedException e) {
            throw new IllegalStateException(e);
        }
    }

}
