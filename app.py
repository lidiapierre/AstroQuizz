import streamlit as st
import os
import openai
from transformers import pipeline, AutoTokenizer
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


signs = ['Aquarius', 'Aries', 'Cancer', 'Capricorn', 'Gemini', 'Leo', 'Libra', 'Pisces', 'Sagittarius', 'Scorpio', 'Taurus', 'Virgo']


mcq_prompt = """
Write a quizz about my personality traits, with 5 questions and 4 options for each question. Use the following format:\n
Q1. <question here>
a) <first option>
b) <second option>
c) <third option>
d) <fourth option>
"""


def generate_questions():
    messages = [{"role": "user", "content": mcq_prompt}]
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=0,
        max_tokens=1834,
    )
    result = response['choices'][0]['message']['content']
    return result


def parse_quizz_content(content):
    parsed_quizz = []
    current_q = ""
    for line in content.splitlines():
        if line.startswith('Q'):
            current_q = line
            parsed_quizz.append((line, []))
        elif line.rstrip() and current_q:
            parsed_quizz
    return parsed_quizz


def score_traits(traits):
    checkpoint = 'lidiapierre/astro-sign-classifier'
    tokenizer = AutoTokenizer.from_pretrained('distilbert-base-multilingual-cased')

    classify_pipe = pipeline("text-classification", model=checkpoint, tokenizer=tokenizer, return_all_scores=True)
    scores = {}
    for sign in signs:
        scores[sign] = 1

    for trait in traits:
        outcome = classify_pipe(trait)[0]
        for result in outcome:
            scores[result['label']] = scores[result['label']] * result['score']

    return dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))


def main():
    st.title("Astro Quizz")
    st.session_state.quizz = generate_questions()
    parsed_quizz = parse_quizz_content(st.session_state.quizz)
    answers = []

    for q in parsed_quizz:
        a = st.radio(q, parsed_quizz[q], index=None)
        if a:
            answers.append(a)
    if len(answers) == 5:
        print(answers)
        result = score_traits(answers)
        st.write(result)
        st.success(result[0])


if __name__ == "__main__":
    main()
