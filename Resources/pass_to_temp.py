def split_words(input_file, num_temp):

    with open(input_file, "r") as f:
        words = f.readlines()

    words = [word.strip() for word in words]

    # Create a list of 6 empty lists, one per group.
    temp = [[] for _ in range(num_temp)]

    # Add words to the temp.
    for i in range(len(words)):
        temp[i % num_temp].append(words[i])

    # Open the text files in write mode.
    for i in range(num_temp):
        with open(f"temp{i + 1}.txt", "w") as f:
            # Write the words in the group to the file.
            f.write("\n".join(temp[i]))

    # Return the list of text files.
    return temp




# Print the contents of the temp
# for i in range(num_temp):
#     print(f"Group {i + 1}: {groups[i]}")
