# AstroQuizz: a fun personal project

AstroQuizz is a fun and interactive project that serves as a personal hands-on exploration of the Transformers models and fine-tuning techniques.

## Approach
The project commenced with data collection on the unique characteristics associated with each astrological sign.
Then, a BERT model was fine-tuned on  this data for classification, processing personality traits to predict astrological signs.
Finally, a Streamlit app interface engages users with 5 questions, generating personality trait sentences based on their responses. 
The overall score from these questions from the fine-tuned BERT model predictions is used to 'guess' the final astrological sign.

## Limitations
AstroQuizz is just a proof of concept. More training data and fine-tuning iterations will be needed to enhance accuracy.
It underscores the challenges of merging subjective fields like astrology with the objectivity of machine learning.
