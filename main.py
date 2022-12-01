def main():
    elves_calories = []
    with open("data.txt", "r") as data:
        temp = []
        for line in data:
            if line == "\n":
                elves_calories.append(temp)
                temp = []
                continue
            cleaned_line = line[0:len(line)-1]
            temp.append(cleaned_line)
    
    for elf in elves_calories:
        for i in range(0, len(elf)):
            elf[i] = int(elf[i])

    most_calories_held_by_an_elf = 0
    for elf_cal_count in elves_calories:
        if sum(elf_cal_count) > most_calories_held_by_an_elf:
            most_calories_held_by_an_elf = sum(elf_cal_count)
    
    print(f"The elf with the most snacks is holding {most_calories_held_by_an_elf} calories!")

    top_three_cal_counts = [0,0,0]
    for elf_cal_count in elves_calories:
        if sum(elf_cal_count) > top_three_cal_counts[0]:
            top_three_cal_counts.insert(0, sum(elf_cal_count))
        elif sum(elf_cal_count) > top_three_cal_counts[1]:
            top_three_cal_counts.insert(1, sum(elf_cal_count))
        elif sum(elf_cal_count) > top_three_cal_counts[2]:
            top_three_cal_counts.insert(2, sum(elf_cal_count))
        
        if len(top_three_cal_counts) > 3:
            top_three_cal_counts.pop()
    
    print(f"The sum of the calories held by the three elves carrying the most snacky energy is {sum(top_three_cal_counts)}")
        

main()

