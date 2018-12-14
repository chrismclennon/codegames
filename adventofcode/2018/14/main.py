# Part 1
# Time: 00:27:11
# Rank: 765
#
# Part 2
# Time: 00:33:46
# Rank: 374


input_val = 890691

recipes = [3, 7, 1, 0]
elf_positions = [0, 1]

for _ in range(1, 890691*50):
    elf1, elf2 = elf_positions
    new_recipe_score = str(recipes[elf1] + recipes[elf2])
    if len(new_recipe_score) > 1:
        recipes.append(int(new_recipe_score[0]))
        recipes.append(int(new_recipe_score[1]))
    else:
        recipes.append(int(new_recipe_score))
    elf_positions[0] = (elf1 + recipes[elf1] + 1) % len(recipes)
    elf_positions[1] = (elf2 + recipes[elf2] + 1) % len(recipes)

    
ans = ''.join(map(str, recipes[input_val:input_val+10]))
print('Part one:', ans)

recipes_str = ''.join(map(str, recipes))
