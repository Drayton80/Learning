package com.example.testingweblayer;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.test.web.servlet.MockMvc;

import static org.hamcrest.Matchers.containsString;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

// Ao utilizar a annotation abaixo em conjunto com @SpringBootTest, a aplicação
// Spring inteira é inicializada sem o servidor. Ao utilizar apenas a @WebMvcTest
// é possível manter a execução apenas na camada Web, sem fazer com que contexto
// do Spring seja inicializado
@WebMvcTest
public class WebLayerTest {
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
