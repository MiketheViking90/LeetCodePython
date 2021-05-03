from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = salary[0]
        max_salary = salary[0]

        sum = 0
        for i in range(len(salary)):
            cur_salary = salary[i]

            min_salary = min(min_salary, cur_salary)
            max_salary = max(max_salary, cur_salary)
            sum += cur_salary
        sum = sum - min_salary - max_salary
        return sum / (len(salary) - 2)

salaries = [4000,3000,1000,2000]
avg = Solution().average(salaries)
print(avg)