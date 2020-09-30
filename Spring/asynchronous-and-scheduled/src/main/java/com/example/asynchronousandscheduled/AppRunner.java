package com.example.asynchronousandscheduled;

import com.example.asynchronousandscheduled.components.ScheduledTasks;
import com.example.asynchronousandscheduled.model.Employee;
import com.example.asynchronousandscheduled.service.GitHubLookupService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import java.util.concurrent.CompletableFuture;

@Component
// O CommandLineRunner define uma segunda execução na linha do comando para o programa
// fazendo com que aquilo que esteja no método run sobrescrito execute após
// o SpringApplication.run() ser chamado na main definida na classe Application
public class AppRunner implements CommandLineRunner {
    // Cria-se uma variável para poder interagir com o terminal da aplicação via código aqui nessa classe:
    private static final Logger logger = LoggerFactory.getLogger(AppRunner.class);

    private final GitHubLookupService gitHubLookupService;

    public AppRunner(GitHubLookupService gitHubLookupService) {
        this.gitHubLookupService = gitHubLookupService;
    }

    @Override
    public void run(String... args) throws Exception {
        // Start the clock
        long start = System.currentTimeMillis();

        // Kick of multiple, asynchronous lookups
        CompletableFuture<Employee> page1 = gitHubLookupService.buildEmployeeFromGithub("Drayton80");
        CompletableFuture<Employee> page2 = gitHubLookupService.buildEmployeeFromGithub("ewertondns");
        CompletableFuture<Employee> page3 = gitHubLookupService.buildEmployeeFromGithub("Douglasliralima");
        CompletableFuture<Employee> page4 = gitHubLookupService.buildEmployeeFromGithub("Armandotgt");

        // Wait until they are all done
        CompletableFuture.allOf(page1,page2,page3,page4).join();

        // Print results, including elapsed time
        logger.info("Elapsed time: " + (System.currentTimeMillis() - start));
        logger.info("--> " + page1.get());
        logger.info("--> " + page2.get());
        logger.info("--> " + page3.get());
        logger.info("--> " + page4.get());
    }

}
