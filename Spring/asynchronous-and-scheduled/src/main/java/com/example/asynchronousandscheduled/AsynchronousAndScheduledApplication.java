package com.example.asynchronousandscheduled;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

import java.util.concurrent.Executor;

@SpringBootApplication
@EnableAsync // Indica que os métodos assíncronos estarão habilitados
@EnableScheduling // Indica que os métodos que utilizam Schedule estarão disponíveis
public class AsynchronousAndScheduledApplication {

	public static void main(String[] args) {
		// Define que a aplicação ficará rodando indefinidamente, é possível chamar
		// o método .close() para fazer com que isso rode apenas uma vez e feche
		SpringApplication.run(AsynchronousAndScheduledApplication.class, args);
	}

	@Bean
	public Executor taskExecutor() {
		ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
		executor.setCorePoolSize(2);
		executor.setMaxPoolSize(2);
		executor.setQueueCapacity(500);
		executor.setThreadNamePrefix("GithubLookup-");
		executor.initialize();
		return executor;
	}
}
