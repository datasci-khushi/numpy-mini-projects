# Employee salary data analysis
import numpy as np
emp_salaries = np.array([25000,40000,20000,45000,60000,54000,36000])
avg_salary = emp_salaries.mean()
print(avg_salary)
highest_salary = emp_salaries.max()
print(highest_salary)
lowest_salary = emp_salaries.min()
print(lowest_salary)
above_50000 = emp_salaries[emp_salaries > 50000]
print(above_50000)
print(above_50000.size)
increment_10 = emp_salaries * 1.1
print(increment_10)
total_salary = emp_salaries.sum()
print(total_salary)
diff_high_low = highest_salary - lowest_salary
print(diff_high_low)
after_increment = increment_10
print(after_increment)
below_avg = emp_salaries[emp_salaries < avg_salary]
print(below_avg)
