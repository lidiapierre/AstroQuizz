# AstroQuizz: a fun personal project

AstroQuizz is a fun and interactive Streamlit app designed for predicting your astrological sign based on a short personality quiz.
This repository serves as a prototype for a personal project, aiming to explore the latest technologies in natural language processing, Transformers models and classification.


## Approach
The project commenced with data collection on the unique characteristics associated with each astrological sign.
Then, a BERT model was fine-tuned on  this data for classification, processing personality traits to predict astrological signs.
Finally, a Streamlit app interface engages users with 5 questions, generating personality trait sentences based on their responses. 
The overall score from these questions from the fine-tuned BERT model predictions is used to 'guess' the final astrological sign.

How it Works:
1. Questionnaire: Users are prompted with 5 engaging questions related to their personality traits.
2. Personality Trait Sentences: For each user response, a corresponding personality trait sentence is generated.
3. BERT Model Classification: A fine-tuned BERT model takes the personality trait sentence as input and predicts the astrological sign label.
4. Final Prediction: The overall score from the 5 questions is used to determine the final predicted astrological sign.


## Getting Started
Clone the repository & install dependencies
```bash
git clone https://github.com/your-username/AstroQuizz.git
cd AstroQuizz
pip install -r requirements.txt
```

Run the Streamlit app.
```bash
streamlit run app.py
```
Answer the quiz questions and discover the app's prediction for your astrological sign!

## Limitations
AstroQuizz is just a proof of concept. More training data and fine-tuning iterations will be needed to enhance accuracy.

Future Improvements:
- Collect more data for each astrological sign
- Perform additional fine-tuning iterations for improved accuracy
- Review overall scoring system
- Enhance the user interface and experience
