import os
import openai
import csv
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def split_text_into_actions(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": f"You are a great text analyst. "
                        f"You should split the text below to detail actions for each role such as Fan, "
                        f"Management, etc. according to the logical flow of what is described in the text."
                        f"Each action should have such strong structure: "
                        f"Step Number, Role (role of the person who make this step. "
                        f"Manager, User, Assistant etc.), Action (2-5 words), "
                        f"Next Steps (follow this strong rules to fill this item: "
                        f"it is very important to specify which next step numbers are available in the"
                        f" 'Next Steps' item. If the step type is 'decision', you need to indicate which "
                        f"next steps are available in case of acceptance or rejection of this decision. "
                        f"The answer should be in the format if the decision is made - Yes: "
                        f"available next step numbers separated by '|', No: available next step numbers "
                        f"separated by '|'. USE ONLY THIS EXAMPLE OF FORMAT: 'Yes:4|6;No:1|3' not only "
                        f"numbers of the next steps), Step Type(can be: start, end, decision or process). "
                        f"This is template for you which describe two action just e.g. : "
                        f"1,Fan, post an idea,Yes:2|3,start \n"
                        f"2,Management,post a Proposal,Yes:8;No:1,process "},
            {"role": "user", "content": f"PLease split text: {text}."}
            ],
        max_tokens=2048
    )
    actions = response["choices"][0]["message"]["content"].split("\n")

    return actions


def write_actions_to_csv(actions, output_file):

    with open(output_file, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")

        for action in actions:
            csv_writer.writerow([action])

    print(f"Result saved to the file: {output_file}")


output_file = "actions.csv"
input_text = "Insert here text, which you want to split into actions"
actions = split_text_into_actions(input_text)
write_actions_to_csv(actions, output_file)
