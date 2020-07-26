from Question import Question
question_prompts = [
    "Who is the prime minister of India?\n(a) Narendra Modi\n(b) Rahul Gandhi\n(c) Manmohan Singh\n\n"
 ##"Who is the prime minister of India?\n(a) Narendra Modi\n(b) Rahul Gandhi\n(c) Manmohan Singh\n\n",
  
]
questions = [
Question(question_prompts[0], "a"),
#Question(question_prompts[1], "a"),

]
def run_test(questions):
    score = 0
for question in questions:
    answer = raw_input(question.prompt)
if answer == question.answer:
   score += 1
print("You got" +str(score) + "/" + str(len(questions))+ "correct ")
run_test(questions)


