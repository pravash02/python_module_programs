import pandas as pd

occupations = {
    0: {'title': 'import export manager', 'code' : '132', 'ess_skills': [{'title': 'title', 'description': 'desciption'}, {'title': 'title', 'description': 'desciption'}]},
    1: {'title': 'water quality analyst', 'code': '2133', 'ess_skills': [{'title': 'title', 'description': 'description'}, {'title': 'title', 'description': 'description'}]}
}

# Convert dictionary to DataFrame
df = pd.DataFrame.from_dict(occupations, orient='index')

# Create a new DataFrame to hold the results
result_df = pd.DataFrame(columns=['title', 'code', '', 'ess_skills_title', 'ess_skills_description'])

# Loop through each row in the original DataFrame and append new rows to the new DataFrame
for i, row in df.iterrows():
    title = row['title']
    code = row['code']
    added_code = False
    for skill in row['ess_skills']:
        skill_title = skill['title']
        skill_description = skill['description']
        if not added_code:
            result_df = pd.concat([result_df, pd.DataFrame({'title': [title], 'code': [code], '': ['ess_skill'], 'ess_skills_title': [skill_title], 'ess_skills_description': [skill_description]})])
            added_code = True
        else:
            result_df = pd.concat([result_df, pd.DataFrame({'title': [''], 'code': [''], '': [''], 'ess_skills_title': [skill_title], 'ess_skills_description': [skill_description]})])

# Set the index of the result DataFrame to the 'title' and 'code' columns
result_df.set_index(['title', 'code'], inplace=True)

# Print the result
print(result_df)
