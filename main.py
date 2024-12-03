from openai import OpenAI
#client = OpenAI(api_key= )
messages=[ {"role": "system", "content": "You are a very helpful math tutor ."} ]

userinput = input("Say:")
messages.append({"role": "user", "content": userinput})
completion = client.chat.completions.create(
model="gpt-3.5-turbo",
#messages=[ {"role": "system", "content": "You are a math teacher but are breif."},{"role": "user", "content": userinput}]

messages = messages

  )


tutor_outputs = completion.choices[0].message.content
messages.append({"role": "assistant", "content": tutor_outputs})
print(tutor_outputs)







