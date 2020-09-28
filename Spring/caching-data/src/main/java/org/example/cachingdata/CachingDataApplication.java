package org.example.cachingdata;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cache.annotation.EnableCaching;

@SpringBootApplication
@EnableCaching // Habilita o uso de Caching e faz com que haja uma checagem buscando em todos os beans do spring por qualquer marcação de caching
public class CachingDataApplication {

    public static void main(String[] args) {
        SpringApplication.run(CachingDataApplication.class, args);
    }

}
