#Hey! Listen! ⌘
#This program was shared by Singe Stheos but was made and is owned by the lovely Secret#3621.
#CREDIT TO ORIGINAL AUTHOR, THEY ARE COOL AND YOU SHOULD TALK TO THEM!

print("THIS PROGRAM WILL EXPORT EVERY LINE IN INPUT.TXT TO AN INDIVIDUAL FILE. USE WITH CAUTION")
print("PROCEED? Y/N")
if input() != "y":
    exit()
with open("input.txt", "r") as input:
    count = 0
    for line in input:
        if not line:
            print("Empty or last line, Exiting.")
            break
        with open(((4 - len("%X" % count)) * "0") + ("%X" % count) + ".txt", "w") as out:
            out.write(line)
            out.close()
        count += 1
print("Finished.")
input.close()
