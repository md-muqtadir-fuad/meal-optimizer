# Meal Optimization System

## Overview

This project was developed for the course **IPE 307: Operations Research** at **Bangladesh University of Engineering and Technology (BUET)**. It optimizes the monthly meal planning for a student dormitory (Titumir Hall) dining system by minimizing total food procurement costs while satisfying daily nutritional requirements, dietary restrictions, and budget constraints using linear programming (Gurobi Optimizer).

## Author

- **Name:** Md. Muqtadir Fuad  
- **Student ID:** 2008079  
- **Course Teacher:** Dr. Nafisa Mahbub  
- **Date Submitted:** 06 Jan 2024

## Scenario

- **Monthly Budget:** BDT 1,200,000  
- **Number of Students:** 480  
- **Meal Participation Rate:** ~75% (~360 active students/day)  
- **Requirements & Considerations:**
  - All meals must satisfy minimum daily nutritional requirements per student.
  - Daily staples include lentils, soybean oil, and lemon slices.
  - Weekly variation is required (e.g., beef, mutton, or fish rotation).
  - Non-Muslim students (~15%) do not consume beef.
  - Students with allergies or dietary preferences opt for chicken over allergen-prone items like Bagda Chingri.
  - Fresh vegetables have quantity bounds to control for spoilage and food waste.

## Daily Nutritional Requirements (Per Student)

- **Protein:** ≥ 50 g  
- **Carbohydrates:** ≥ 150 g  
- **Fat:** ≥ 30 g  

## Mathematical Model

### Decision Variables
- `x_i`: Quantity (in kg) of ingredient `i` to procure for the month.

### Objective Function
Minimize total procurement cost:
$$\min \sum c_i x_i$$
where $c_i$ is the unit cost of ingredient $i$.

### Constraints
1. **Nutritional Requirements:**
   $$\sum a_{ij} x_i \ge b_j$$
   where $a_{ij}$ is the amount of nutrient $j$ in ingredient $i$, and $b_j$ is the minimum required intake across all students.

2. **Item Consumption Bounds:**
   $$L_i \le x_i \le U_i$$
   reflecting weekly variety, perishability limits, and daily inclusion staples.

## Setup & Execution

### Prerequisites

Install dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```

> **Note:** The model uses `gurobipy`. Because this model has 34 variables, it runs on Gurobi's free size-limited license without requiring an academic or commercial license key.

### Running the Model

Run the optimization script from the root directory:
```bash
python "Titumir Hall/TITUMIRmodel.py"
```

## Data Source

- Nutritional data collected from [Nutritionix](https://www.nutritionix.com)
