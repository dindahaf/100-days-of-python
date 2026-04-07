student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_exam_score = sum(student_scores)
print(total_exam_score)

sum = 0
for score in student_scores:
    sum += score
print(sum)

max_score = max(student_scores)
print(max_score)


find_max_score = 0
for score in student_scores:
    if score > find_max_score:
        find_max_score = score

#print in the outside the for in loop so that we only print once(the result number)
print(find_max_score)

# Do not need to give other scenarios because if the "if code above" is not happen so we do nothing and do not need to catch anything.
# so we do not need these codes :
# (
#     elif score < find_max_score:
#         find_max_score = find_max_score
#     elif score == find_max_score:
#         find_max_score = find_max_score
# )
