package com.example.gettingstarted.servingwebcontent;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class GreetingControllerServingWeb {

    @GetMapping("/serving-web-content/greeting")
    public String greeting(@RequestParam(required = false, name = "name", defaultValue = "World") String name, Model model){
        model.addAttribute("name", name);
        return "greeting";
    }
}
