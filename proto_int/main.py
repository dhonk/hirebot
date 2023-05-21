import openai
import string
import matplotlib.pyplot as plt
import gen_sub

# String that stores applicant response from speech to text program
applicant_response = ''

# use gen_sub to turn audio into string
def get_audio(): 
    applicant_response = gen_sub.text()

# initialize specification array
spec_arr[]
def get_specs(specifications):
    spec_arr = specifications.split()

# generate prompt based 
def prompt_gen(spec_arr: String[], ) -> int:
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

# Sets up openai API credentials
def set_api():
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

def response_gen(prompt: String)
    response = chat_with_gpt(gpt_prompt)

    res_arr = response.split('\n')

    for i in range(len(res_arr)):
        res_arr[i] = int(''.join(c for c in res_arr[i] if c.isdigit()))

if __name__ == '__main__':
    plt.bar(spec_arr, res_arr, width=0.3)
    plt.xlabel('Trait')
    plt.ylabel('Affinity')
    plt.title('Applicant Affinity')
    plt.ylim(0,100)

    plt.show()

