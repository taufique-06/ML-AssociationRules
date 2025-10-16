import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None);
transactions = []
for i in range (0, 7501):
  transactions.append([str(dataset.values[i,j]) for jin range(0,20)])

# Apply the Apriori algorithm
# min_support = 0.003: Based on common sense, each product should appear at least 3 times per day,
# over 7 days => 3*7 = 21 times out of 7501 transactions => 0.003
# min_confidence = 0.2. Tried with 0.8 and 0.4 didnt get better results
# min_lift = 3: Ensures that the rules are relevant (lift > 3 considered strong).
# min_length = 2, max_length = 2: Only consider rules with exactly two products (1 on LHS, 1 on RHS),
# because testing this business scenario "buy one product A, get one product B".
rules = apriori(transactions = transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)

#Displaying the first results coming directly from the output of the apriori function
results = list(rules)

#Display the data for better visualization
def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])


#Sorting the results by LIFT
resultsinDataFrame.nlargest(n = 10, columns = 'Lift')
