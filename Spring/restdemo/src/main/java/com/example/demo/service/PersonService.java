package com.example.demo.service;

import com.example.demo.dao.PersonDao;
import com.example.demo.model.Person;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

// Esta annotation define que essa classe operará como um Service
@Service
// Esta classe serve como um ponto de acesso que efetivamente define qual será a classe que estará realmente
// sendo usada no local da interface personDao, fazendo com que, caso seja utilizada outra implementação do
// DAO, apenas seja necessário mudar a tag da classe que implementa aqui
public class PersonService {

    private final PersonDao personDao;

    // Autowired define que será feita uma dependancy injection aqui baseado no que foi
    // definido através das annotations em outras classes
    @Autowired
    public PersonService(@Qualifier("postgres") PersonDao personDao) { // Nesse caso PersonDao não teve definição pois ele é apenas uma interface, então usa-se
                                                                      // o @Qualifier para delimitar que o que será utilizado é a classe que implementa o
                                                                      // personDao e possui a tag fakeDao a ela atrelada
        this.personDao = personDao;
    }

    public int addPerson(Person person){
        return personDao.insertPerson(person);
    }

    public List<Person> getAllPeople(){
        return personDao.selectAllPeople();
    }

    public Optional<Person> getPersonById(UUID id){
        return personDao.selectPersonById(id);
    }

    public int deletePersonById(UUID id){
        return personDao.deletePersonById(id);
    }

    public int updatePersonById(UUID id, Person person){
        return personDao.updatePersonById(id, person);
    }
}
