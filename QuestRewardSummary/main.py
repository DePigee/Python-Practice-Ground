DEFAULT_BONUS_PER_TASK = 5

#returns total gold for a quest
def calculate_quest_reward(base_gold, side_tasks=0, bonus_per_task=DEFAULT_BONUS_PER_TASK):
    return base_gold + (side_tasks * bonus_per_task)

#returns back formatted string
def build_quest_summary(quest_name, base_gold, side_tasks=0, bonus_per_task=DEFAULT_BONUS_PER_TASK):
    total_gold = calculate_quest_reward(base_gold, side_tasks, bonus_per_task)
    
    return (
        f"Quest: {quest_name}\n"
        f"Base gold: {base_gold}\n"
        f"Side tasks: {side_tasks}\n"
        f"Bonus per task: {bonus_per_task}\n"
        f"Total gold: {total_gold}"
    )

print(calculate_quest_reward(20,2,5))
print(build_quest_summary("Goblin Camp", 20, 2, 5))