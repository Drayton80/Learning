package com.example.testingweblayer;

import com.example.testingweblayer.controller.HomeController;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import static org.assertj.core.api.Assertions.assertThat;

// Qualquer classe dentro de test marcada com essa annotation será chamada e terá os métodos
// marcados com @Test executados para validar a aplicação em etapas quando
// for executado o test do gradle ou maven
@SpringBootTest
public class SanityTest {

    @Autowired
    private HomeController homeController;

    @Test
    // Faz um teste que checa, utilizando o assertThat, se uma instância
    // de homeController está retornando um objeto nulo
    public void contextLoads() throws Exception {
        assertThat(homeController).isNotNull();
    }
}
