l = [n for n in range(1, 6)]
print(l)

for i in l:

    try:
        if i % 2 == 0:
            print(f"i четное = {i}")
        else:
            print(f"i нечетное = {i}")

    except:
        print("Error in 1_3_list_literate str 6-10")