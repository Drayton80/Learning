package com.example.gsdata.controller;

import com.example.gsdata.model.Employee;
import com.example.gsdata.service.EmployeeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Date;
import java.util.List;

@RequestMapping("api/v1/employee")
@RestController
public class EmployeeController {

    private final EmployeeService employeeService;

    @Autowired
    public EmployeeController(EmployeeService employeeService) {
        this.employeeService = employeeService;
    }

    @PostMapping
    public void addEmployee(@RequestBody Employee employee){
        employeeService.addEmployee(employee);
    }

    @PutMapping(path = "{id}")
    public void updateEmployeeById(@PathVariable("id") int id, @RequestBody Employee employee){
        employeeService.updateEmployeeById(id, employee);
    }

    @GetMapping("/names")
    public List<String> getAllEmployeesNames(){
        return employeeService.getAllEmployeesNames();
    }

    @GetMapping
    public List<Employee> getAllEmployees(){
        return employeeService.getAllEmployees();
    }
}
