package com.example.gettingstarted.resthateoas;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import org.springframework.hateoas.RepresentationModel;

public class GreetingHateoas extends RepresentationModel<GreetingHateoas> {

    private final String content;

    @JsonCreator
    public GreetingHateoas(@JsonProperty("content") String content) {
        this.content = content;
    }

    public String getContent(){
        return content;
    }
}
