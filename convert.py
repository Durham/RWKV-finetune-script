import json
import random
import sys
input_file = 'alpaca_data_cleaned.json'
output_txt_file = "alpaca_data_cleaned_for_training.txt"

# Load the JSON file
with open(input_file , 'r') as f:
    data = json.load(f)

#Shuffle data
random.shuffle(data)
# Concatenate the records into a single string in the desired format
text = ''
dtext = ''
q = 0
basic_text=''
for record in data:
   print(q,end='\n')
   q =q +1
   if not 'instruction' in record:
      continue
   period = "." if random.randint(0,1)==0 else ""

   instruction =   record['instruction']
   if random.randint(0,1)==0:
     instruction = instruction[:-1]
   if random.randint(0,1)==0:
     instruction = instruction[0].strip().lower() + instruction[1:]


   if random.randint(0,1)==0:

    text = f"user: {instruction} {record['input']}{period}\nbot: {record['output']}<|endoftext|>\n".replace('\n\n','\n').replace(" . ",'').replace(" .\n",'\n')
   else:
    text = f"user: {record['input']}. {instruction}\nbot: {record['output']}<|endoftext|>\n".replace('\n\n','\n').replace(" . ",'').replace(" .\n",'\n')
   d={}
   d['text'] = text
   dtext = dtext+'\n'+json.dumps(d)
   basic_text= basic_text+text
# Print the resulting text
#print(text)
# write resulting text to a file
#with open('output_alpaca_cleaned.jsonl', 'w') as f:
#    f.write(dtext)

with open(output_txt_file,'w')
  f.write(basic_text)



