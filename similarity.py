from sentence_transformers import SentenceTransformer, util
from flask import Flask, request, render_template
from waitress import serve

app = Flask(__name__)

# Load pre-trained BERT model
#model = SentenceTransformer('bert-base-nli-mean-tokens')

# Existing answers and corresponding questions
questions_answers = {
    "future_career": "future career",
    "expertise": "expertise",
    "preferred_time": "preferred time",
    "self_rating": "self rating",
    "study_time": "study time"
}

# Fake coach details
coach_details = [
    {
        "name": "Dr. Jennifer Smith",
        "expertise": "Python Programming and Data Science",
        "self_rating": "9",
        "future_career": "Machine Learning Engineer",
        "preferred_time": "Weekdays evenings",
        "study_time": "30 minutes per topic"
    },
   
    {
        "name": "Prof. Michael Johnson",
        "expertise": "Python for Web Development",
        "self_rating": "8",
        "future_career": "Full Stack Developer",
        "preferred_time": "Flexible weekdays",
        "study_time": "20 minutes per topic"
    },
    {
        "name": "Dr. Emily Lee",
        "expertise": "Python for Artificial Intelligence",
        "self_rating": "7",
        "future_career": "AI Researcher",
        "preferred_time": "Weekends mornings",
        "study_time": "25 minutes per topic"
    },
    {
        "name": "Prof. David Garcia",
        "expertise": "Python for Data Analysis",
        "self_rating": "9",
        "future_career": "Data Scientist",
        "preferred_time": "Weekdays afternoons",
        "study_time": "30 minutes per topic"
    },
    {
        "name": "Dr. Sarah Clark",
        "expertise": "Python for Scientific Computing",
        "self_rating": "8",
        "future_career": "Research Scientist",
        "preferred_time": "Weekends afternoons",
        "study_time": "20 minutes per topic"
    },
    {
        "name": "Prof. John Roberts",
        "expertise": "Python for Software Engineering",
        "self_rating": "7",
        "future_career": "Software Developer",
        "preferred_time": "Weekdays mornings",
        "study_time": "25 minutes per topic"
    }
]

@app.route('/')
def index():
    return render_template('hw')

# @app.route('/result', methods=['POST'])
# def result():
#     student_answers = [request.form[value] for key, value in questions_answers.items()]
#     encoded_student_answers = model.encode(student_answers, convert_to_tensor=True)
#     similarities = []
#     for coach_detail in coach_details:
#         coach_answers = [
#             coach_detail["future_career"],
#             coach_detail["expertise"],
#             coach_detail["preferred_time"],
#             coach_detail["self_rating"],
#             coach_detail["study_time"]
#         ]
#         encoded_coach_answers = model.encode(coach_answers, convert_to_tensor=True)
#         similarity = util.pytorch_cos_sim(encoded_student_answers, encoded_coach_answers).cpu().numpy()[0][0]
#         similarities.append(similarity)
#     highest_similarity_index = similarities.index(max(similarities))
#     highest_similarity_coach = coach_details[highest_similarity_index]
#     return render_template('result.html', coach=highest_similarity_coach)

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)
