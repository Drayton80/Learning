package com.example.asynchronousandscheduled.components;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.text.SimpleDateFormat;
import java.util.Date;

@Component
public class ScheduledTasks {
    // Cria-se uma variável para poder interagir com o terminal da aplicação via código aqui nessa classe:
    private static final Logger log = LoggerFactory.getLogger(ScheduledTasks.class);
    private static final SimpleDateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");

    // Basicamente essa annotation define para o Spring que, equanto
    // SpringApplication.run(AsynchronousAndScheduledApplication.class, args), estiver
    // rodando, esse método executará automaticamente em intervalos de tempo de 5 segundos
    // (devido ao fixedRate definido como 5000 ms).
    // OBS.: um detalhe é que apenas métodos que não possuam parâmetros de entrada que podem ser Scheduled
    @Scheduled(fixedRate = 5000)
    public void reportCurrentTime(){
        log.info("The time is now {}", dateFormat.format(new Date()));
    }
}
