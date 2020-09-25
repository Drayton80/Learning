package com.example.gettingstarted.resthateoas;

import com.example.gettingstarted.restservicecors.GreetingController;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.*;

@RestController
public class GreetingHateoasController {

    private static final String TEMPLATE = "Hello, %s!";

    @RequestMapping("/rest-hateoas/greeting")
    public HttpEntity<GreetingHateoas> greeting(@RequestParam(value = "name", defaultValue = "World") String name){
        GreetingHateoas greeting = new GreetingHateoas(String.format(TEMPLATE, name));

        greeting.add(linkTo(methodOn(GreetingController.class).greeting(name)).withSelfRel());

        return new ResponseEntity<>(greeting, HttpStatus.OK);
    }
}
