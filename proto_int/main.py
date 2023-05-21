import openai 
import string
import matplotlib.pyplot as plt
import gen_sub

#file_path = input("Applicant response file path: ")

applicant_response = ''
#try:
#        with open(file_path, 'r') as file:
#            applicant_response = file.read();

#except FileNotFoundError:
#    print(f"File '{file_path}' not found.")

applicant_response = gen_sub.text()

specifications = input("Specify a few traits you're looking for: ")
spec_arr = specifications.split()

variables = string.ascii_lowercase

gpt_prompt = ''
gpt_prompt = applicant_response + '\n\n'
gpt_prompt += 'Pretend that you are a interviewer for job applicants. Grade this prompt with this rubric:\n'
for i in range(len(spec_arr)):
    gpt_prompt += f"a variable {variables[i]} indicating {spec_arr[i]} from a scale of 1-100, 50 being an acceptable college essay or job application"
gpt_prompt += 'Grade this prompt exactly with this rubric with this format:\n'
for i in range(len(spec_arr)):
    gpt_prompt += f"{spec_arr[i]}\n"
    gpt_prompt += f"{variables[i]}\n"

# Set up your OpenAI API credentials
openai.api_key = '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'

# Define a function to interact with the ChatGPT model
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        top_p=1.0,
        n=1,
        stop=None,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    
    if len(response.choices) > 0:
        return response.choices[0].text.strip()
    else:
        return "Sorry, I couldn't generate a response."

response = chat_with_gpt(gpt_prompt)

res_arr = response.split('\n')

for i in range(len(res_arr)):
    res_arr[i] = int(''.join(c for c in res_arr[i] if c.isdigit()))

plt.bar(spec_arr, res_arr, width=0.3)
plt.xlabel('Trait')
plt.ylabel('Affinity')
plt.title('Applicant Affinity')
plt.ylim(0,100)

plt.show()

