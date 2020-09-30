package com.example.testingweblayer;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.boot.web.server.LocalServerPort;
import static org.assertj.core.api.Assertions.assertThat;

// O parâmetro passado abaixo faz o servidor iniciar com uma porta aleatória no test
// para evitar conflitos em ambientes de teste
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class HttpRequestTest {
    // Define port com a porta padrão do servidor através dessa annotation
    @LocalServerPort
    private int port;

    @Autowired
    private TestRestTemplate restTemplate;

    @Test
    public void greetingShouldReturnDefaultMessage(){
        // Usa assertThat para checar se o retorno da rota em questão é aquilo que é desejado que se retorne
        assertThat(this.restTemplate.getForObject("http://localhost:" + port + "/", String.class))
                .contains("<h1> Hello there </h1>");
    }
}
