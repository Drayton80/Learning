package com.example.demo.dao;

import com.example.demo.model.Person;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

// Indica que essa classe serve como um repositório com um nome de fakeDao, uma tag para referenciar ele,
// fazendo a substituição em locais que a interface DAO for chamada através da dependacy injection do spring,
// possibilitando assim que seja possível facilmente migrar entre diversos tipos de implementação de um mesmo DAO
@Repository("fakeDao")
// Essa classe serve como uma das possíveis implementações da interface DAO
public class FakePersonDataAccessService implements PersonDao {
    private static List<Person> DB = new ArrayList<>();

    @Override
    public int insertPerson(UUID id, Person person) {
        DB.add(new Person(id, person.getName()));
        return 1;
    }

    @Override
    public List<Person> selectAllPeople() {
        return DB;
    }

    @Override
    public Optional<Person> selectPersonById(UUID id) {
        return DB.stream().filter(person -> person.getId().equals(id)).findFirst();
    }

    @Override
    public int deletePersonById(UUID id) {
        Optional<Person> personMaybe = selectPersonById(id);

        if (personMaybe.isEmpty()){
            return 0;
        }else{
            DB.remove(personMaybe.get());
            return 1;
        }
    }

    @Override
    public int updatePersonById(UUID id, Person personUpdate) {
        return selectPersonById(id)
                .map(person -> {
                    int indexOfPersonToUpdate = DB.indexOf(person);

                    if (indexOfPersonToUpdate >= 0){
                        DB.set(indexOfPersonToUpdate, new Person(id, personUpdate.getName()));
                        return 1;
                    }else{
                        return 0;
                    }
                })
                .orElse(-1);
    }
}
