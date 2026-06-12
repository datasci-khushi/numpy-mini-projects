# Employee salary data analysis
import numpy as np
emp_salaries = np.array([25000,40000,20000,45000,60000,54000,36000])
avg_salary = emp_salaries.mean()
print("Mean Salary =", avg_salary)
highest_salary = emp_salaries.max()
print("Maximum Salary =", highest_salary)
lowest_salary = emp_salaries.min()
print("Minimum Salary =", lowest_salary)
above_50000 = emp_salaries[emp_salaries > 50000]
print("Salaries above 50000 =", above_50000)
print("Count above 50000 =", above_50000.size)
increment_10 = emp_salaries * 1.1
print("Salaries after 10% increment =", increment_10)
total_salary = emp_salaries.sum()
print("Total Salary =", total_salary)
diff_high_low = highest_salary - lowest_salary
print("Difference of highest and lowest salary =", diff_high_low)
after_increment = increment_10
print("Salary after increment =", after_increment)
below_avg = emp_salaries[emp_salaries < avg_salary]
print("Salaries below average =", below_avg)
