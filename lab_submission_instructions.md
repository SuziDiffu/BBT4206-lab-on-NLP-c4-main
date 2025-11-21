# Lab Submission Instructions

---

## Student Details

**Name of the team on GitHub Classroom:**

**Team Member Contributions:**

**Member 1**

| **Details**                                                                                        | **Comment** |
|:---------------------------------------------------------------------------------------------------|:------------|
| **Student ID:**                                                                                    |       150493      |
| **Name:**                                                                                          |    Muindi Catherine Mutheu         |
| **What part of the lab did you personally contribute to,** <br>**and what did you learn from it?** |   I created the course evaluation analysis file analysis.ipynb , downloaded the NLTK VADER lexicon, and ran the full analysis: loading data, preprocessing text, fitting LDA, assigning topics, computing sentiment, and saving outputs. I also launched the Gradio app locally. I learnt how to manage Python environments, perform NLP preprocessing and analysis, compute sentiment, and build a simple interactive app.        |

**Member 2**

| **Details**                                                                                        | **Comment** |
|:---------------------------------------------------------------------------------------------------|:------------|
| **Student ID:**  148886                                                                                  |             |
| **Name:**   Osimbo Vallerie Akhungu Martha                                                                                       |             |
| **What part of the lab did you personally contribute to,** <br>**and what did you learn from it?** |       I contributed by testing the existing NLP pipeline on new student course evaluations, predicting both the topics and the sentiment of each comment. I interpreted the results by mapping topic numbers to meaningful themes using the top words from the LDA model and verified that sentiment analysis accurately reflected positive, negative, or mixed feedback. I also prepared the output in a clear and readable format, making it easy to demonstrate and use for further course evaluation analysis.      |

**Member 3**

| **Details**                                                                                        | **Comment** |
|:---------------------------------------------------------------------------------------------------|:------------|
| **Student ID:**                                                                                    |  152548           |
| **Name:**                                                                                          |  Susan Diffu           |
| **What part of the lab did you personally contribute to,** <br>**and what did you learn from it?** | 
I contributed to the development and enhancement of the NLP pipeline by implementing the full text-preprocessing workflow, integrating VADER sentiment analysis, improving topic modelling interpretability through clear topic labels and keyword extraction, and conducting dataset-wide topic and sentiment analysis to generate meaningful insights. I also and added an interpretation and recommendations section to translate the model outputs into actionable guidance |

**Member 4**

| **Details**                                                                                        | **Comment** |
|:---------------------------------------------------------------------------------------------------|:------------|
| **Student ID:**                                                                                    |             |
| **Name:**                                                                                          |             |
| **What part of the lab did you personally contribute to,** <br>**and what did you learn from it?** |             |

**Member 5**

| **Details**                                                                                        | **Comment** |
|:---------------------------------------------------------------------------------------------------|:------------|
| **Student ID:**                                                                                    |             |
| **Name:**                                                                                          |             |
| **What part of the lab did you personally contribute to,** <br>**and what did you learn from it?** |             |

## Scenario

Your client, a university, is seeking to enhance their qualitative analysis of
student course evaluations collected from students. They have provided you
with a dataset containing student course evaluation for two courses in the
Business Intelligence Option. The two courses are:
- BBT 4106: Business Intelligence I
- BBT 4206: Business Intelligence II

The client wants you to use Natural Language Processing (NLP) techniques to identify
the key topics (themes) discussed in the course evaluations. They would also like to
get the sentiments (positive, negative, neutral) of each theme in the course evaluation.

Lastly, the client would like an interface through which they can provide input in the
form of new textual data (one student's textual evaluation at a time) and the output
expected is:
1. The topic (theme) that the new textual data is talking about.
2. The sentiment (positive, negative, neutral) of the new textual data.

Use one of the following to create a demo interface for your client:
- Hugging Face Spaces using a Gradio App – [https://huggingface.co/spaces](https://huggingface.co/spaces)
- Streamlit Community Cloud (Streamlit Sharing) using a Streamlit App – [https://share.streamlit.io](https://share.streamlit.io)
---
## Dataset

Use the course evaluation dataset provided in Google Classroom.

## Interpretation and Recommendation

Provide a brief interpretation of the results and a recommendation for the client.
- Interpret what the discovered topics mean and why certain sentiments dominate
- Provide recommendations based on your results. **Do not** recommend anything that is not supported by your results.

## Video Demonstration

Submit the link to a short video (not more than 4 minutes) demonstrating the topic modelling and the sentiment analysis.
Also include (in the same video) the user interface hosted on hugging face or streamlit.

| **Key**                             | **Value** |
|:------------------------------------|:----------|
| **Link to the video:**              |           |
| **Link to the hosted application:** |           |


## Grading Approach

| Component                            | Weight | Description                                                       |
|:-------------------------------------|:-------|:------------------------------------------------------------------|
| **Data Preprocessing & Analysis**    | 20%    | Cleaning, preprocessing, and justification of chosen methods.     |
| **Topic Modelling**                  | 20%    | Correctness, interpretability, and coherence of topics.           |
| **Sentiment Analysis**               | 20%    | Appropriate model choice and quality of sentiment classification. |
| **Interface Design & Functionality** | 20%    | Usability, interactivity, and deployment success.                 |
| **Interpretation & Recommendation**  | 10%    | Logical, evidence-based, and actionable insights.                 |
| **Presentation (Video & Clarity)**   | 10%    | Clarity, professionalism, and demonstration of understanding.     |
