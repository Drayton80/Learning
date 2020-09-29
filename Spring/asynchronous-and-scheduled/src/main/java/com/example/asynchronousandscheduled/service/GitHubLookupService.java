package com.example.asynchronousandscheduled.service;

import com.example.asynchronousandscheduled.model.Employee;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.concurrent.CompletableFuture;

@Service
public class GitHubLookupService {

    private static final Logger logger = LoggerFactory.getLogger(GitHubLookupService.class);
    private final RestTemplate restTemplate;

    public GitHubLookupService(RestTemplateBuilder restTemplateBuilder){
        this.restTemplate = restTemplateBuilder.build();
    }

    // A annotation Async marca o método como assíncrono para o Spring
    @Async
    public CompletableFuture<Employee> buildEmployeeFromGithub(String employeeGithubUsername) throws InterruptedException {
        logger.info("Looking up " + employeeGithubUsername);
        String url = String.format("https://api.github.com/users/%s", employeeGithubUsername);

        Employee results = restTemplate.getForObject(url, Employee.class);
        Thread.sleep(1000L); // Delay artificial para demonstrar o uso do asynchronous

        // CompletableFuture é uma biblioteca do Java que serve justamente
        // para fazer o gerenciamento do pipeline de métodos assincronos
        return CompletableFuture.completedFuture(results);
    }

}
