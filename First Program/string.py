# multiline in a string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# String are array
name = "Yahya al Mahmud himel"
print(name[12])

# looping through a string
for s in "Yahya al Mahmud himel":
    print(s)

# find string lengh
name = "Yahya al Mahmud himel"
print(len(name))

# check string
paragraph = "Palestine, a region in the Middle East, holds historical and geopolitical significance as it has been at the center of the Israeli-Palestinian conflict for many decades. The area is home to a diverse population and has a rich cultural heritage. Palestine's history is marked by complex dynamics, including territorial disputes, efforts towards statehood, and challenges in achieving lasting peace. The status of an independent Palestinian state remains a subject of international debate and negotiations. The region's historical and cultural significance, along with its ongoing challenges, make it a topic of global importance in diplomacy and conflict resolution."
searchingWord = 'Palestine'
if searchingWord in paragraph:
    print(searchingWord + " word is found")
else:
    print("not found")

# 