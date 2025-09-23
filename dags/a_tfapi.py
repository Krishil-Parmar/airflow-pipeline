'''
taskflow api allows us to use decorators instead of operators
such as pythonoperator


task 1: start with a number (say 100) 
task 2: add 50 to the number 
task 3: to multipy the result by 2 
task 4: to divide the result by 10 
'''

from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(
    dag_id = 'arithmetic_operator_tfapi'
) as dag:
    
    # task 1: start with a number (say 100)
    @task
    def start_number():
        initial_value = 100
        print(f"starting number:, {initial_value}")
        return initial_value
    
    # task 2: add 50 to the number
    @task
    def add_50(number): 
        new_value = number + 50
        print (f"add 50 : {number} + 50 = [new_value]")
        return new_value

    #task 3: to multipy the result by 2 
    @task
    def multiply_two(number):
        new_value = number*2
        print(f"multiply by 2: {number}*2= {new_value}")
        return new_value

    #task 4: to divide the result by 10 
    @task
    def divide_ten(number):
        new_value = number/10
        print(f"divide by 10: {number} / 10 = {new_value}")
        return new_value
    
    #dependencies
    start_value = start_number()
    second_value = add_50(start_value)
    third_value = multiply_two(second_value)
    fourth_value = divide_ten(third_value)







