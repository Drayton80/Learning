package com.example.gsdata.model;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.Date;

public class Employee {
    private final int id;
    private final String name;
    private final String gender;
    private final Date birthDate;

    public Employee(
            @JsonProperty("id") int id,
            @JsonProperty("name") String name,
            @JsonProperty("gender") String gender,
            @JsonProperty("birth_date") Date birthDate) {
        this.id = id;
        this.name = name;
        this.gender = gender;
        this.birthDate = birthDate;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getGender() {
        return gender;
    }

    public Date getBirthDate() {
        return birthDate;
    }
}
