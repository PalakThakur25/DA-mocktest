import pandas as pd 
 
def get_dataframe(df_name, columns): 
    print(f"\nEnter data for {df_name}") 
 
    num_rows = int(input(f"How many rows for {df_name}? ")) 
 
    data = {col: [] for col in columns} 
 
    for r in range(num_rows): 
        print(f"Row {r + 1}:") 
 
        for col in columns: 
            value = input(f"{col}: ").strip() 
 
            if value.isdigit(): 
                value = int(value) 
            else: 
                try: 
                    value = float(value) 
                except ValueError: 
                    pass 
 
            data[col].append(value) 
 
    df = pd.DataFrame(data) 
 
    print(f"\n{df_name}:\n{df}\n") 
 
    return df 
 
students_df = get_dataframe( 
    "Students", 
    ["StudentID", "Name", "Branch"] 
) 
 
marks_df = get_dataframe( 
    "Marks", 
    ["StudentID", "Marks"] 
) 
 
inner_merge = pd.merge( 
    students_df, 
    marks_df, 
    on="StudentID", 
    how="inner" 
) 
 
print("Inner Merge:") 
print(inner_merge) 
 
left_merge = pd.merge( 
    students_df, 
    marks_df, 
    on="StudentID", 
    how="left" 
) 
 
print("\nLeft Merge:") 
print(left_merge) 
 
right_merge = pd.merge( 
    students_df, 
    marks_df, 
    on="StudentID", 
    how="right" 
) 
 
print("\nRight Merge:") 
print(right_merge) 
 
outer_merge = pd.merge( 
    students_df, 
    marks_df, 
on="StudentID", 
how="outer" 
) 
print("\nOuter Merge:") 
print(outer_merge) 
df_a = students_df.set_index("StudentID") 
df_b = marks_df.set_index("StudentID") 
joined_df = df_a.join(df_b, how="inner") 
print("\nJoin:") 
print(joined_df) 
horizontal_concat = pd.concat( 
[students_df, marks_df], 
axis=1 
) 
print("\nHorizontal Concatenation:") 
print(horizontal_concat)