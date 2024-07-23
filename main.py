from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt


CALORIE_GOAL_LIMIT=3000
PROTIEN_GOAL=180
FAT_GOAL=80
CARBS_GOAL=300

today=[]

@dataclass
class Food:
    name:str
    calories:int
    protien: int
    fats:int
    carbs: int

done=False

while not done:
    print("""
          (1) Add a new food
          (2) Visualize Progress
          (q)quit
          """)
    choice=input("Choose an option: ")

    if choice=="1":
        print("Adding a new food!")
        name=input("Name: ")
        calories=int(input("Calories: "))
        protiens=int(input("Protiens: "))
        fats=int(input("Fats: "))
        carbs=int(input("Carbs: "))
        food=Food(name,calories,protiens,fats,carbs)
        today.append(food)
        print("Successfully added!")
    elif choice=="2":
        calories_sum=sum(food.calories for food in today)
        protien_sum=sum(food.protien for food in today)
        fats_sum=sum(food.fats for food in today)
        carbs_sum=sum(food.carbs for food in today)


        fig,axs=plt.subplots(2,2)
        axs[0,0].pie([protien_sum,fats_sum,carbs_sum],labels=["Protiens","Fats","Carbs"], autopct="%1.1f%%")
        axs[0,0].set_title("Macronutrients Distribution")
        axs[0,1].bar([0,1,2],[protien_sum,fats_sum,carbs_sum],width=0.4)
        axs[0,1].bar([0,4,1.4,2.4],[PROTIEN_GOAL,FAT_GOAL,CARBS_GOAL],width=0.4)
        axs[0, 1].set_title("Macronutrients Progress")
        fig.tight_layout()
        plt.show()
