import random

type_of_stimulus = random.choice(['voice', 'voice_image', 'voice_text', 'voice_image_text'])
print(type_of_stimulus)

STIMULI_COUNT = 3
number_of_stimulus = random.randrange(1, STIMULI_COUNT+1)
print(number_of_stimulus)



print(random.sample(range(1, 4), 3))
