import openai
import string
import matplotlib.pyplot as plt
import gen_sub

# use gen_sub to turn audio into string
def get_audio()->str: 
    response = gen_sub.text()
    return response

# Get specification array
def get_specs(specifications: str)->list[str]:
    spec_arr = specifications.split()
    return spec_arr

# generate prompt based 
def prompt_gen(spec_arr: list[str], response: str)->str:
    variables = string.ascii_lowercase
    gpt_prompt = ''
    gpt_prompt = response + '\n\n'
    gpt_prompt += 'Pretend that you are a interviewer for job applicants. Grade this prompt with this rubric:\n'
    for i in range(len(spec_arr)):
        gpt_prompt += f"a variable {variables[i]} indicating {spec_arr[i]} from a scale of 1-100, 50 being an acceptable college essay or job application"
    gpt_prompt += 'Grade this prompt exactly with this rubric with this format:\n'
    for i in range(len(spec_arr)):
        gpt_prompt += f"{spec_arr[i]}\n"
        gpt_prompt += f"{variables[i]}\n"
    return gpt_prompt

# Sets up openai API credentials
def set_api()->None:
    openai.api_key = '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'

# Define a function to interact with the ChatGPT model
def chat_with_gpt(prompt: str)->str:
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

def response_gen(prompt: str)->list[int]:
    response = chat_with_gpt(prompt)
    res_arr = response.split('\n')
    for i in range(len(res_arr)):
        res_arr[i] = int(''.join(c for c in res_arr[i] if c.isdigit()))
    return res_arr

if __name__ == '__main__':
    set_api()
    temp = get_audio()
    specs = input("Specs: ")
    spec_arr = get_specs()
    prompt = prompt_gen(spec_arr, temp)
    temp = chat_with_gpt(prompt)
    res_arr = response_gen(temp)

    plt.bar(spec_arr, res_arr, width=0.3)
    plt.xlabel('Trait')
    plt.ylabel('Affinity')
    plt.title('Applicant Affinity')
    plt.ylim(0,100)

    plt.show()

