package com.example.testingweblayer;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureWebMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;

import static org.hamcrest.Matchers.containsString;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
// A annotation abaixo faz com que seja possível testar sem inicializar completamente
// o servidor, mas sim apenas o layer em que o Spring lida com as requisições HTTP
// e entrega elas para o Controller
@AutoConfigureWebMvc
public class TestingWebApplicationTest {

    @Autowired
    private MockMvc mockMvc;

    @Test
    public void shouldReturnDefaultMessage() throws Exception {
        // Esse uso do mock basicamente pega aquilo que retorna-se da rota / através do perform(get())
        // e, após printar o resultado, checa se o status vindo da requisição foi OK e se o conteúdo
        // da String bate corretamente com o que é esperado
        this.mockMvc.perform(get("/"))
                .andDo(print())
                .andExpect(status().isOk())
                .andExpect(content().string(containsString("<h1> Hello there </h1>")));
    }
}
