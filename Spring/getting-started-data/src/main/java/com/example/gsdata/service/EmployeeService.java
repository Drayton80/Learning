package com.example.gsdata.service;

import com.example.gsdata.model.Employee;
import com.example.gsdata.repository.EmployeeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.List;

@Service
public class EmployeeService {

    private final EmployeeRepository employeeRepository;

    @Autowired
    public EmployeeService(EmployeeRepository employeeRepository) {
        this.employeeRepository = employeeRepository;
    }

    public void addEmployee(Employee employee){
        employeeRepository.addEmployee(employee);
    }

    public void updateEmployeeById(int id, Employee employee){
        employeeRepository.updateEmployeeById(id, employee);
    }

    public List<String> getAllEmployeesNames(){
        return employeeRepository.getAllEmployeesNames();
    }

    public List<Employee> getAllEmployees(){
        return employeeRepository.getAllEmployees();
    }
}
