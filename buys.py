import pandas as pd

# Create the DataFrame
df = pd.DataFrame({
    'income': ['very high', 'high', 'medium', 'high', 'very high', 'medium', 'high', 'medium', 'high', 'low'],
    'credit': ['excellent', 'good', 'excellent', 'good', 'good', 'excellent', 'bad', 'bad', 'bad', 'bad'],
    'decision': ['authorize', 'authorize', 'authorize', 'authorize', 'authorize', 'authorize', 'request id', 'request id', 'reject', 'call police']
})

# Calculate prior probabilities
prior_probabilities = df['decision'].value_counts(normalize=True)

# Function to calculate the conditional probabilities
def calculate_conditional_probability(income, credit, decision):
    income_count = df[(df['income'] == income) & (df['decision'] == decision)].shape[0]
    credit_count = df[(df['credit'] == credit) & (df['decision'] == decision)].shape[0]
    total_count = df[df['decision'] == decision].shape[0]
    
    p_income_given_decision = income_count / total_count if total_count > 0 else 0
    p_credit_given_decision = credit_count / total_count if total_count > 0 else 0
    
    return p_income_given_decision, p_credit_given_decision

# Tuple to classify
tuple_to_add = ('medium', 'good')

# Calculate posterior probabilities
posterior_probabilities = {}

for decision in prior_probabilities.index:
    p_income, p_credit = calculate_conditional_probability(*tuple_to_add, decision)
    posterior_prob = prior_probabilities[decision] * p_income * p_credit
    posterior_probabilities[decision] = posterior_prob

# Find the class with the maximum posterior probability
max_decision = max(posterior_probabilities, key=posterior_probabilities.get)
max_prob = posterior_probabilities[max_decision]

print(f"Maximum posterior probability is {max_prob}")
print(f"Tuple classified into {max_decision}")