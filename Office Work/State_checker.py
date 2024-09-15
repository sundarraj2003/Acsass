"""
    This is field is used to open a excel and get a document and that location lists

    Fields = ['content', 'titles', 'location1', 'location2']
    python open file code






"""
#Excel inputs

content = ''
title = '' 
state_list = [ "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming" ]
state_list_shortend =  [ "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY" ] 
location1 = []
location2 = []

#our output locations

def find_staes(loc1, loc2, content, title):
    location1 = [i.lower() for i in loc1]
    location2 = [i.lower() for i in loc2]
    found_location1 = []
    found_location2 = []
    content_state_list = []
    content = content
    title = title
    for state in state_list:
        [found_location1.append(state) for words in content.split(" ") if words.lower().__contains__(state.lower())]
        [found_location2.append(state) for words in title.split(" ") if words.lower().__contains__(state.lower())]

    for state in state_list_shortend:
        [found_location1.append(state) for words in content.split(" ") if words.__contains__(state)]
        [found_location2.append(state) for words in title.split(" ") if words.__contains__(state)]
    output_location1 = []
    output_location2 = []
    [output_location1.append(i) for i in found_location1 if i.lower() not in location1]
    [output_location2.append(i) for i in found_location2 if i.lower() not in location2]
    return {'input_content':content, "input_title":title, "input_location1":loc1, "input_location2":loc2, "output_location1":found_location1, "output_location2":found_location2, "final_loaction1":output_location1,  "final_loaction2":output_location2}



#testing File Output
content = '''Got it! You want to extract U.S. state names from a single paragraph, but store them into **two separate variables**, such as `title` and `content`, both of which may contain U.S. state names. Here's how you can handle it:

### Python Program:

```python
# List of all US states
states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", 
    "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", 
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", 
    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", 
    "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", 
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", 
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", 
    "Wisconsin", "Wyoming"
]

def find_states_in_paragraph(paragraph):
    # Initialize a list to store found states
    found_states = []
    
    # Check each state if it is mentioned in the paragraph
    for state in states:
        if state in paragraph:
            found_states.append(state)
    
    return found_states

# Input paragraph from the user
paragraph = input("Enter a paragraph: ")

# Assume the first half of the paragraph is the title, and the second half is the content
# Split the paragraph into title and content based on the middle point
middle_index = len(paragraph) // 2
title = paragraph[:middle_index]
content = paragraph[middle_index:]

# Find states in title and content
states_in_title = find_states_in_paragraph(title)
states_in_content = find_states_in_paragraph(content)

# Output the states found in both title and content
print("States found in the title:", states_in_title)
print("States found in the content:", states_in_content)
```

### How this works:
1. **Input**: You enter a single paragraph.
2. **Split**: The paragraph is split into two parts:
   - The first half is treated as the `title`.
   - The second half is treated as the `content`.
3. **State Search**: The program searches for U.S. state names in both the `title` and `content`.
4. **Output**: It shows the U.S. state names found in each half (the title and content).

### Example:
#### Input:
```
Enter a paragraph: I visited California and Texas last summer. Later, I went to New York and Florida in winter.
```

#### Output:
```
States found in the title: ['California', 'Texas']
States found in the content: ['New York', 'Florida']
```

This way, the program extracts the U.S. state names and organizes them into `states_in_title` and `states_in_content`.'''
title = 'I am A good boy and i amm a hel-IA citycens'
locationn1 = []
locationn2 = ['IA']


print(find_staes(locationn1,locationn2,content=content,title=title))
print("hii")


    
    