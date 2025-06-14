import ollama
import os
import logging

#CONSTANTS
MODEL_NAME = "TaskWing:latest"
INPUT_FILE = "./data/tasks.txt"
OUTPUT_FILE = "./data/agent37_logbook.txt"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logging.info(f"TaskWing initalized. Preparing for lift-off")

def file_reader(file_path):
    """Check if the input file exists and return its contents"""
    if os.path.exists(file_path):
        logging.info(f"Aha! I see what it is.")
        with open(file_path, "r") as f:
            return f.read()
    else:
        logging.error(f"Uhm are you sure you gave me something?")
        raise FileNotFoundError(f"Input file at {file_path} not found.")

#to read the tasks at hand:
def read_and_think(file_content):
    """Process the file content into a list of tasks"""
    tasks = file_content.strip().splitlines()
    return tasks

#preparation of prompt for the model

def prepare_prompt(tasks):
    prompt = f"""
        TaskWing, I want you to help me with these following tasks to get my work done with me
        and my team. I would mention when I am working solo, or with a team. Based on that,
        you will see if you need to give instruction for a solo person or a team. The team
        will have their names and roles as well, for you to have an easier time to unravel the
        tasks for the said team or solo person. If it is a team, you are ought to think and
        delegate the tasks based on the team's plan, so that they can have an easier time
        carrying out the tasks. The tasks they would be mentioning would be:

        {"\n".join(f"- {task}" for task in tasks)}

        You will also look through the team members names if given, you would be intelligent enough
        to read through their roles too. You are great at breaking down tasks from the situations.
        Apart from delegating tasks you are also supposed to give an estimated time to finish
        the tasks to each team member, giving them a deadline, to carry out the tasks for the
        further planning and endeavours. You will do this because you are their manager. And
        you also give them a sprinkle of motivation to get their job done.
        PLEASE ONLY LOOK AT THE TASKS GIVEN AT HAND, and DO NOT add anything new, just look
        at the tasks given, there is NO NEED to add new tasks or team members.

        Instructions:
        - If solo (e.g., 'I am solo'), create a time-blocked plan for tasks (e.g., numbered items), respecting any timeline (e.g., 'one week'), with completion times and deadlines.
        - If team (e.g., 'we are a team'), break down the task into specific subtasks and assign to members based on roles, with completion times and deadlines. If the task is broad (e.g., 'present performance'), infer subtasks like preparing visuals or writing reports based on roles.
        - Add a Nightwing-style motivational quip for each task.
        - For each team member's task, if the steps are unclear, ask for clarification instead of assuming too much.
        - When describing *how* to execute a task, suggest tools, platforms, or formats they likely use based on their roles.
        - ONLY use tasks and roles in the input—DO NOT add new tasks, members, or assume a team for solo inputs.

        Let’s make time our sidekick and save Gotham in NO TIME!!!

        Respond in the style of a confident, witty superhero like Nightwing, with playful banter
        and clear motivating task assignments
    """
    return prompt



#sending the prompt and getting the response

def get_response(prompt):
    try:
        response = ollama.generate(model=MODEL_NAME, prompt=prompt)
        generated_text=response.get("response","")
        logging.info(f"So, I see if we can do this in this manner, we can save Gotham in NO TIME!!! Hang tight, cause this is going to be a ride")
        print(generated_text)

        #saving the response in an output file
        with open(OUTPUT_FILE, "w") as f:
            f.write("\n".join(generated_text.strip().splitlines()))
            logging.info(f"Hah! the mission's set! Team, remember its business.. as casual.")
            print(f"The mission has been saved to {OUTPUT_FILE}, so we better get working now.")
            print("Remember Titan, we got this! ")

            return generated_text

    except Exception as e:
        logging.info(f"Uhmm I guess something is wrong, I can't sense the file in my radar. Try again. {str(e)}")
        return None


def main():
    """Main functions to orchestrate the program flow"""
    try:
        #reading the input file
        file_content = file_reader(INPUT_FILE)
        #process tasks
        tasks = read_and_think(file_content)
        #prepare the prompt
        prompt = prepare_prompt(tasks)
        #get and save the response
        get_response(prompt)

    except Exception as e:
        logging.error(f"Uh-oh. You need to try again. {str(e)}")
        exit(1)


if __name__=="__main__":
    main()
