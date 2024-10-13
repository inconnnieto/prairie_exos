import random
import pandas as pd

# Function to simulate the Asch experiment and determine validity
def asch(ref, A, B, C, rep):
    if ref == A:
        if rep == 1:
            return True
        else:
            return False
    elif ref == B:
        if rep == 2:
            return True
        else:
            return False
    elif ref == C:
        if rep == 3:
            return True
        else:
            return False
    return False

# Function to introduce errors in the dataset
def introduce_errors(df, error_rate):
    df_with_errors = df.copy()
    num_errors = int(len(df) * error_rate)  # Calculate number of errors based on error rate
    
    # Randomly select rows to introduce errors
    error_indices = random.sample(range(len(df)), num_errors)
    
    for i in error_indices:		# Flip the 'valid' column (True <-> False)
        df_with_errors.at[i, 'valid'] = not df_with_errors.at[i, 'valid']
    return df_with_errors

# Generate 10 random test cases that are correct
octavia_test = []

for i in range(40): 
    values = [random.choice(range(1, 25)) for j in range(3)]
    A, B, C = values
    ref = random.choice(values)
    rep = values.index(ref) + 1  
    
    valid = asch(ref, A, B, C, rep) 
    octavia_test.append([ref, A, B, C, rep, valid])

# Create DataFrame for test dataset
columns = ['ref', 'A', 'B', 'C', 'rep', 'valid']
train_df_error = pd.DataFrame(octavia_test, columns=columns)

# Save the test dataset (baseline with correct responses)
train_df_error.to_csv('8_octavia_asch_train_dataset_40_false.csv', index=False)

# Show the test dataset
print(train_df_error)