# Meal optimization system at student dormitory

## Overview

This project is an individual assignment developed for the course **IPE 307: Operation Researches** at **Bangladesh University of Engineering and Technology (BUET)**. It aims to optimize the monthly meal planning for Titumir Hall’s dining system by minimizing costs while meeting the nutritional and dietary needs of students.

## Author

- **Name:** Md. Muqtadir Fuad  
- **Student ID:** 2008079  
- **Course Teacher:** Dr. Nafisa Mahbub  
- **Date Submitted:** 06 Jan 2024

## Scenario

- **Monthly Budget:** BDT 1,200,000  
- **Number of Students:** 480  
- **Meal Participation Rate:** ~75%  
- **Requirements:**
  - All meals must meet minimum daily nutrition requirements.
  - Meals should include daily items like lentils and lemon slices.
  - Weekly variation is required (e.g., beef or mutton at least once).
  - Special considerations:
    - Non-Muslim students (~15%) do not consume beef.
    - 5% health-conscious students opt for chicken instead of allergen-prone items like Bagda Chingri.
    - Fresh vegetables must be used wisely due to spoilage concerns.
    - Minimize food waste and allergens.

## Nutritional Requirements (Per Student, Per Day)

- **Protein:** ≥ 50g  
- **Carbohydrate:** ≥ 150g  
- **Fat:** ≥ 30g  

## Objective

Minimize the total cost of ingredients while ensuring all constraints are met.

## Ingredients Dataset

Each ingredient has associated:
- Protein, Carbs, Fat content (per 100g)
- Price per kg

(Full list available in the documentation)

## Mathematical Model

### Sets
- `I`: Set of ingredients

### Parameters
- `a_ij`: Nutrient value of ingredient `i` for nutrient `j`
- `b_i`: Minimum required intake of nutrient `i`
- `c_i`: Cost of ingredient `i`

### Decision Variables
- `x_i`: Quantity (in kg) of ingredient `i` to use

### Objective Function
Minimize ∑ c_i * x_i

### Constraints
1. **Nutritional Requirements:**  
   ∑ a_ij * x_i ≥ b_j  (for each nutrient j)

2. **Budget Constraint:**  
   ∑ c_i * x_i ≤ Budget

3. **Other Constraints:**  
   - Weekly and monthly variation (e.g. beef/mutton, Bagda Chingri)
   - Allergen and religious considerations
   - Daily inclusion of certain vegetables and condiments

## Data Source

- Nutritional data collected from [Nutritionix](https://www.nutritionix.com)
