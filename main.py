import pandas as p
import matplotlib.pyplot as plt

# provide these column names: ['DATE', 'TAG', 'POSTS']
df = p.read_csv("QueryResults.csv", names=["Date", "Tag", "Posts"])

clean_df = df.dropna()

# Look at the first and last 5 rows of the DataFrame.
first_5 = clean_df.head()
last_5 = clean_df.tail()


# How many rows and how many columns does it have?
amount = clean_df.shape

# Count the number of entries in each column
entries_count = clean_df.count()

# figure out how to count the number of posts per language?
# Which programming language had the most number of posts since the creation of Stack Overflow

months_of_posts_per_language = clean_df.groupby("Tag").count()
post_amount = clean_df.groupby("Tag").sum()
most_language_with_posts = post_amount.idxmax()
language = post_amount.loc[most_language_with_posts]


# Selecting an Individual Cell
cell = clean_df["Date"][1]


# Inspecting the Data Type
type(clean_df["Date"][1])

# change the format with pandas method to_datetime()
clean_df["Date"] = p.to_datetime(clean_df.Date)

# there is a whole file that explains the pivot method
# Can you pivot the df DataFrame so that each row is a date and each column is a programming language?
# Store the result under a variable called reshaped_df.

reshaped_df = clean_df.pivot(columns="Tag", index="Date", values="Posts")
reshaped_df.fillna(0, inplace=True)
# The inplace argument means that we are updating reshaped_df.
# Without this argument we would have to write something like this: reshaped_df = reshaped_df.fillna(0)


# Examine the dimensions of the reshaped DataFrame. How many rows does it have? How many columns?
reshaped_df.shape

# Examine the head and the tail of the DataFrame. What does it look like?
head = reshaped_df.head()
tail = reshaped_df.tail()

# Print out the column names
column_names = reshaped_df.columns


# Count the number of entries per column
entry_amount = reshaped_df.count()

# plot the popularity of the Java programming language.
graph = plt.plot(reshaped_df.index, reshaped_df["java"])
# to see the graph we need a notebook

# styling the graph:
# makes the size bigger by setting the width to 16 and the height to 10
plt.figure(figsize=(16, 10))

plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# plotting both java and python
plt.plot(reshaped_df.index, reshaped_df["java"], reshaped_df["python"])
# or to simply calling the .plot() method twice once for java and once for python

# plot all the languages in one graph
for language in reshaped_df.columns:
    plt.plot(reshaped_df.index,
             reshaped_df[language], linewidth=3, label=reshaped_df[language].name)

plt.legend(fontsize=16)


# smoothing out time-series data

roll_df = reshaped_df.rolling(window=6).mean()
plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)
