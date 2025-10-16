# ML-AssociationRules
Association Rule Learning with Apriori &amp; Eclat

# Apriori Algorithm
## Project Name - Market Basket Optimization
This project focuses on **Market Basket Optimization** using **Association Rule Learning**. The goal is to discover interesting relationships between products in a retail transactional dataset, helping to inform strategies like **product bundling**, **cross-selling**, and **promotions**.

Code can be seen in https://github.com/taufique-06/ML-AssociationRules/blob/main/Apriori.py

## Results
### Key Metrics Explained:
### Support
1. Measures how often a pair of products appear together in the dataset. Example: fromage blanc → honey has support 0.0033, meaning these two products appeared together in 0.33% of all transactions.

### Confidence
Measures how often the RHS product is purchased when the LHS product is purchased. Example: pasta → escalope has confidence 0.373, meaning 37.3% of the transactions that include pasta also include escalope.

### Lift
Measures how much more likely the RHS product is purchased when the LHS product is purchased compared to random chance. Example: fromage blanc → honey has lift 5.16, meaning customers buying fromage blanc are 5.16 times more likely to buy honey than if they bought products randomly.

<img width="962" height="500" alt="image" src="https://github.com/user-attachments/assets/71dd04c0-0dc5-4a6f-9189-ed309e51e8fe" />

# Eclat Algorithm
ECLAT and Apriori both find frequent itemsets, but the methods differ. Apriori uses a horizontal layout, scans all baskets level by level (breadth-first), and counts itemsets repeatedly. ECLAT uses a vertical layout, keeps a list of baskets for each item, and finds support by intersecting these lists (depth-first). ECLAT only uses support to find frequent itemsets; confidence and lift are only used later for association rules.

Code can be found: https://github.com/taufique-06/ML-AssociationRules/blob/main/eclar.py

## Results
<img width="458" height="331" alt="image" src="https://github.com/user-attachments/assets/fe732d70-5f51-41ed-a227-2bda7096eacf" />


