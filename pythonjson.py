import json

people_string = '''
{
	"people": [
		{
			"name" : "John Smoth",
			"phone": "2131234",
			"emails": ["johnsmith@gmail.com", "smithj@gmail.com"],
			"address": "Klaten"
		},
		{
			"name" : "Jane Meldi",
			"phone" : "234234523512",
			"emails": null,
			"address": "Merauke"
		}
	]
}
'''

data = json.loads(people_string)

for person in data['people']:
    print(person['name'])

new_string = json.dumps(data['people'], sort_keys=True)
print(new_string)

# print(new_string['people'])
