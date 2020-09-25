package com.example.gettingstarted;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@SpringBootApplication
public class GettingstartedApplication {

	public static void main(String[] args) {
		SpringApplication.run(GettingstartedApplication.class, args);
	}

	// Este método serve para definir como será feito o cross-origin
	@Bean
	public WebMvcConfigurer corsConfigurer() {
		return new WebMvcConfigurer() {
			// Fazendo esse override é possível habilitar a cross-origin globalmente daqui
			// essa é uma segunda forma de fazer o cross-origin
			@Override
			public void addCorsMappings(CorsRegistry registry) {
				registry.addMapping("/rest-service-cors/greeting-javaconfig").allowedOrigins("http://localhost:9000");
			}
		};
	}
}
