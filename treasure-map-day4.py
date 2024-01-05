line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
print(f"{line1}\n{line2}\n{line3}")
position = input("\n") # Where do you want to put the treasure?

row = int(position[1])
column = position[0]
column_list = ["1","2","3"]

for i in range(len(column_list)):
  if column == "A":
    column = int(column_list[0])
    break
  elif column == "B":
    column = int(column_list[1])
    break
  else:
    column = int(column_list[2])
    break
map[row-1][column-1] = "X"
print(f"{line1}\n{line2}\n{line3}")