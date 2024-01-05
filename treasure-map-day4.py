line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
print(f"{line1}\n{line2}\n{line3}")
position = input("\n") # Where do you want to put the treasure?

row_index = int(position[1])
column = position[0].upper()
column_list = ["A","B","C"]
column_index = column_list.index(column)
map[row_index-1][column_index] = "X"

print(f"{line1}\n{line2}\n{line3}")