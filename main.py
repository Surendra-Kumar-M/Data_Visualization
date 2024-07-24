from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt


#Setting the Goal value
CALORIE_GOAL_LIMIT=3000
PROTEIN_GOAL=180
FAT_GOAL=80
CARBS_GOAL=300

#Initializing an empty list 
today=[]

#integrating the data class
@dataclass
class Food:
    name:str
    calories:int
    protein: int
    fats:int
    carbs: int

done=False

#To rum the code untill we quit
while not done:
    print("""
          (1) Add a new food
          (2) Visualize Progress
          (q)quit
          """)
    choice=input("Choose an option: ")

    if choice=="1":
        #getting the user data

        print("Adding a new food!")
        name=input("Name: ")
        calories=int(input("Calories: "))
        proteins=int(input("Proteins: "))
        fats=int(input("Fats: "))
        carbs=int(input("Carbs: "))
        food=Food(name,calories,proteins,fats,carbs)
        today.append(food)
        print("Successfully added!")
        
    elif choice=="2":
        #adding all the user data
        calories_sum=sum(food.calories for food in today)
        protein_sum=sum(food.protein for food in today)
        fats_sum=sum(food.fats for food in today)
        carbs_sum=sum(food.carbs for food in today)


        # Data Visualization Section
        fig,axs=plt.subplots(2,2)
        # Pie Chart for axis 1
        axs[0,0].pie([protein_sum,fats_sum,carbs_sum],labels=["Proteins","Fats","Carbs"], autopct="%1.1f%%")
        axs[0,0].set_title("Macronutrients Distribution")
        # Bar chart for axis 2
        axs[0,1].bar([0,1,2],[protein_sum,fats_sum,carbs_sum],width=0.4)
        axs[0,1].bar([0.5,1.5,2.5],[PROTEIN_GOAL,FAT_GOAL,CARBS_GOAL],width=0.4)
        axs[0,1].set_title("Macronutrients Progress")
        # Pie Chart for axis 3
        #Comparing the goals with progress
        axs[1,0].pie([calories_sum,CALORIE_GOAL_LIMIT],labels=["Calories","Remaining"],autopct="%1.1f%%")
        axs[1,0].set_title("Calories goal Progress")
        # Graph Plotting to see the progress
        axs[1,1].plot(list(range(len(today))),np.cumsum([food.calories for food in today]),label="Calories Eaten")
        axs[1,1].plot(list(range(len(today))),[CALORIE_GOAL_LIMIT]*len(today),label="Calories Goal")
        axs[1,1].legend()
        axs[1,1].set_title("Calories Goal over Time")
        fig.tight_layout()
        plt.show()

    #Exiting Section
    elif choice=="q":
        done=True
    else:
        print("Invalid Choice")
