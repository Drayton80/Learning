package com.example.testingweblayer.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HomeController {

    @RequestMapping("/")
    // @ResponseBody aqui define que a String será retornada no corpo do HTML
    public @ResponseBody String greeting(){
        return "<h1> Hello there </h1>";
    }

}
