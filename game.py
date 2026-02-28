import art
import random
print(art.logo)

data = [
    {
        'name' : 'Leo Messi',
        'follower' : 511,
        'description' : 'Footballer',
        'country' : 'Argentina'
    },
    {
        'name' : 'Cristiano Ronaldo',
        'follower' : 671,
        'description' : 'Footballer',
        'country' : 'Portugal'
    },
    {
        'name' : 'Neymar',
        'follower' : 233,
        'description' : 'Footballer',
        'country' : 'Brazil'
    },

    {
        'name' : 'Sergio Aguero',
        'follower' : 28,
        'description' : 'Footballer',
        'country' : 'Argentina'
    },

    {
        'name' : 'Kylian Mbappe',
        'follower' : 130,
        'description' : 'Footballer',
        'country' : 'France'
    },

    {
        'name' : 'Lamine Yamal',
        'follower' : 40,
        'description' : 'Footballer',
        'country' : 'Spain'
    },

  {
      'name' : 'Luis Suarez',
      'follower' : 47,
      'description' : 'Footballer',
      'country' : 'Uruguay'
  }
]



def higher_lower_game(data):
  compare_a = random.choice(data)

  guess = True
  score = 0
  while guess == True:
    compare_b = random.choice(data)
    while compare_a == compare_b:
            compare_b = random.choice(data)
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']} from {compare_a['country']}, his follower are {compare_a['follower']}M")
    print(art.vs)
    print(f"Compare B: {compare_b['name']}, a {compare_b['description']} from {compare_b['country']}")
    choose = input("who hase more follower? A or B: ").upper()

    if compare_a['follower'] >= compare_b['follower']:
      answer = 'A'
    else:
      answer = 'B'

    if choose == answer:
      score += 1
      print(f"You are right. Your score is {score}")
      compare_a = compare_b
    else:
      print(f"You are wrong. Your score is {score}")
      guess = False

higher_lower_game(data)