# HR Management System

## Classes

### Employees
Main class that represents an employee, containing three subclasses:
- information (personal and professional data)
- evaluation (performance metrics)
- payment (benefits and deductions)

### Information
Stores basic employee data:
- name, age, role, base salary, total salary, schedules and status
- uses "N/A" (Not Available) as default value for text fields
- uses "0" as default value for numeric fields

### Evaluation
Stores employee performance data:
- evaluation score
- performance description
- number of absences

### Payment
Manages financial information:
- total benefits and benefits list
- total deductions and deductions list

### Benefit and Discount
Similar classes that control salary changes:
- benefit/deduction name
- change type (percentage, multiplicative or additive)
- change value

## Functions

### Employee Management

#### Add_employee
- Registers new employees in the system
- Allows continuous data entry until user chooses to exit

#### Remove_Employee
- Removes employees from the system
- Allows individual or mass removal

#### Add_Information
- Collects basic employee data
- Records information such as name, age, role, etc.

#### Update_Information
- Allows modification of existing data
- Can update a specific employee or all

#### Print_Employee_Information
- Displays employee data
- Can show a specific employee or list all

### Evaluation System

#### Perform_Employee_Evaluation
- Records new evaluation
- Allows evaluating a specific employee or all

#### Employee_evaluation
- Collects evaluation data
- Records score, description and absences

#### Print_Employee_Evaluations
- Shows recorded evaluations
- Can display a specific evaluation or all

### Benefits Management

#### Add_Benefits
- Creates new types of benefits
- Records benefit name, type and value

#### Remove_Benefits
- Removes existing benefits
- Allows individual or mass removal

#### Print_Benefits_List
- Lists available benefits
- Can show a specific benefit or all

#### Register_Employee_Benefits
- Associates benefits to employees
- Can register for a specific employee or all

### Deductions Management

#### Add_Deductions
- Creates new types of deductions
- Records deduction name, type and value

#### Remove_Deductions
- Removes existing deductions
- Allows individual or mass removal

#### Print_Deductions_List
- Lists available deductions
- Can show a specific deduction or all

#### Register_Employee_Deductions
- Associates deductions to employees
- Can register for a specific employee or all

### Salary Calculations

#### Calculate_Total_Employee_Salary
- Calculates final salary considering benefits and deductions
- Can calculate for a specific employee or all

#### Calculate_Total_Benefits
- Sums all applicable benefits
- Considers different calculation types (percentage, multiplicative, additive)

#### Calculate_Total_Deductions
- Sums all applicable deductions
- Considers different calculation types (percentage, multiplicative, additive)

## System Overview

The system functions as a complete human resources manager, offering:
- Employee registration and management
- Performance evaluation system
- Benefits and deductions management
- Automated salary calculation
- Report generation and data visualization

All operations can be performed both individually and in bulk, allowing efficient management of teams of any size.
