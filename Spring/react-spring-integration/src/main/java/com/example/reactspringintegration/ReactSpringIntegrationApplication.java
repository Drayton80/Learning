package com.example.reactspringintegration;

import com.example.reactspringintegration.model.User;
import com.example.reactspringintegration.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ReactSpringIntegrationApplication implements CommandLineRunner {

	public static void main(String[] args) {
		SpringApplication.run(ReactSpringIntegrationApplication.class, args);
	}

	@Autowired
	private UserRepository userRepository;

	@Override
	public void run(String... args) throws Exception {
		this.userRepository.save(new User("John", "Gregory", "john12@hotmail.com"));
		this.userRepository.save(new User("Thomas", "Greywood", "thom.grey@gmail.com"));
	}
}
