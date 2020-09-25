package com.example.gsdata.repository;

import com.example.gsdata.model.Employee;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

@Repository
public class EmployeeRepository {

    @Autowired
    JdbcTemplate jdbcTemplate;

    public void addEmployee(Employee employee){
        final String sql = "INSERT INTO employees(id, name, gender, birth_date) VALUES (?, ?, ?, ?);";

        jdbcTemplate.update(sql, new Object[]{employee.getId(), employee.getName(), employee.getGender(), employee.getBirthDate()});
    }

    public void updateEmployeeById(int id, Employee employee){
        final String sql = "UPDATE employees SET name = ?, gender = ?, birth_date = ? WHERE id = ?";

        jdbcTemplate.update(sql, new Object[]{employee.getName(), employee.getGender(), employee.getBirthDate(), id});
    }

    public List<String> getAllEmployeesNames(){
        return jdbcTemplate.queryForList("SELECT name FROM employees;", String.class);
    }

    public List<Employee> getAllEmployees(){
        final String sql = "SELECT * FROM employees;";

        return jdbcTemplate.query(sql, (resultSet, i) -> {
           int id = resultSet.getInt("id");
           String name = resultSet.getString("name");
           String gender = resultSet.getString("gender");
           Date birth_date = resultSet.getDate("birth_date");

           return new Employee(id, name, gender, birth_date);
        });
    }

}
