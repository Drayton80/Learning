package com.example.gettingstarted.restservicecors;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.concurrent.atomic.AtomicLong;

@RestController
public class GreetingController {
    private static final String template = "Hello, %s!";
    private final AtomicLong counter = new AtomicLong();

    // Define-se que a porta 9000 possibilitará uma requisição cross-origin, ou seja,
    // que esse recurso seja acessado por outros domínios através desse link
    @CrossOrigin(origins = "http://localhost:9000")
    @GetMapping("/rest-service-cors/greeting")
    public Greeting greeting(@RequestParam(required = false, defaultValue = "World") String name){
        return new Greeting(counter.incrementAndGet(), String.format(template, name));
    }

    @GetMapping("/rest-service-cors/greeting-javaconfig")
    public Greeting greetingWithJavaconfig(@RequestParam(required=false, defaultValue="World") String name) {
        System.out.println("==== in greeting ====");
        return new Greeting(counter.incrementAndGet(), String.format(template, name));
    }
}
