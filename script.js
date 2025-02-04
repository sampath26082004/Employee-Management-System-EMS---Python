// Sample employee data (in-memory storage)
let employees = [];

// Function to show the respective form
function showForm(formType) {
    // Hide all forms
    document.querySelectorAll('.employee-form').forEach(form => {
        form.classList.add('hidden');
    });
    // Show the specific form
    document.getElementById(`${formType}-form`).classList.remove('hidden');
    document.getElementById('employee-list').classList.add('hidden');
}

// Function to show employee list
function showEmployeeList() {
    document.getElementById('employee-list').classList.remove('hidden');
    const tableBody = document.getElementById('employee-table').getElementsByTagName('tbody')[0];
    tableBody.innerHTML = ""; // Clear the table
    employees.forEach(emp => {
        const row = tableBody.insertRow();
        row.innerHTML = `
            <td>${emp.employee_id}</td>
            <td>${emp.name}</td>
            <td>${emp.position}</td>
            <td>${emp.salary}</td>
        `;
    });
}

// Function to add a new employee
function addEmployee() {
    const id = document.getElementById('add-emp-id').value;
    const name = document.getElementById('add-name').value;
    const position = document.getElementById('add-position').value;
    const salary = document.getElementById('add-salary').value;

    if (id && name && position && salary) {
        employees.push({ employee_id: id, name, position, salary });
        alert("Employee added successfully!");
        showEmployeeList();
    } else {
        alert("Please fill in all fields.");
    }
}

// Function to remove an employee
function removeEmployee() {
    const id = document.getElementById('remove-emp-id').value;
    employees = employees.filter(emp => emp.employee_id !== id);
    alert(`Employee with ID ${id} removed successfully!`);
    showEmployeeList();
}

// Function to update employee details
function updateEmployee() {
    const id = document.getElementById('update-emp-id').value;
    const name = document.getElementById('update-name').value;
    const position = document.getElementById('update-position').value;
    const salary = document.getElementById('update-salary').value;

    const employee = employees.find(emp => emp.employee_id === id);
    if (employee) {
        if (name) employee.name = name;
        if (position) employee.position = position;
        if (salary) employee.salary = salary;
        alert("Employee updated successfully!");
        showEmployeeList();
    } else {
        alert("Employee not found.");
    }
}

// Function to search for an employee
function searchEmployee() {
    const id = document.getElementById('search-emp-id').value;
    const employee = employees.find(emp => emp.employee_id === id);
    if (employee) {
        alert(`Employee Found: ${employee.name}, Position: ${employee.position}, Salary: ${employee.salary}`);
    } else {
        alert("Employee not found.");
    }
}    