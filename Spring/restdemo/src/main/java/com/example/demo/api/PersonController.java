package com.example.demo.api;

import com.example.demo.model.Person;
import com.example.demo.service.PersonService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.lang.NonNull;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.UUID;

// Esta annotation define a rota para que seja possível utilizar isso através de uma requisição
@RequestMapping("api/v1/person")
// Esta anotação serve para indicar que essa classe servirá como um Controller REST
@RestController
// Esta classe serve como um controller para o acesso ao PersonService, ou seja, ela delimita, qual será a rota
// e tipos de retorno ou alterações para cada possível tipo de método HTTP
public class PersonController {
    private final PersonService personService;

    @Autowired // Define que aqui haverá uma dependancy injection, que nesse caso é a da classe PersonService, delimitada como um @Service
    public PersonController(PersonService personService) {
        this.personService = personService;
    }

    // Define que o método servirá como um POST request
    @PostMapping
    public void addPerson(@RequestBody Person person){ // @RequestBody define que as informações estarão no body da requisição
                                                       // aqui também é definido que Person será a classe que receberá aquilo
                                                       // que está no body da requisição
        personService.addPerson(person);
    }

    // Define que o método servirá como um GET request
    @GetMapping
    public List<Person> getAllPeople(){
        return personService.getAllPeople();
    }

    // Torna possível colocar após a rota api/v1/person um "/{id}" no método GET
    @GetMapping(path = "{id}")
    public Person getPersonById(@PathVariable("id") UUID id){ // Transforma o id pego na rota para o UUID id
        return personService.getPersonById(id)
                .orElse(null);
    }

    @DeleteMapping(path = "{id}")
    public void deletePersonById(@PathVariable("id") UUID id){
        personService.deletePersonById(id);
    }

    @PutMapping(path = "{id}")
    public void updatePersonById(@PathVariable("id") UUID id, @RequestBody Person person){
        personService.updatePersonById(id, person);
    }
}
