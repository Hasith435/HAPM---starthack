from . import db
from flask import session

def matcher_func(student_school, students_learning_type, preferred_language, current_subject):

    """takes these 3 variables as input and then returns a list of emails of tutors arranged according to the order of priority, which depends on 
    how many of the 3 criteria are matching"""

    possible_teachers = []
    count = 0

    docs = db.collection('teachers').get()

    for doc in docs:
        doc_dict = doc.to_dict()

        if doc_dict['teaching_subject'] == current_subject:
            count += 1
            if doc_dict['school'] == student_school:
                count += 1
            if doc_dict['teaching_method'] == students_learning_type:
                count += 1
            if doc_dict['language'] == preferred_language:
                count += 1
        
            possible_teachers.append([[doc_dict['email'], doc_dict['teaching_subject'], doc_dict['teaching_method'], doc_dict['language']], count])

            count = 0
        else:
            continue
    
    sorted_teacher_list = sorted(possible_teachers, key=lambda x:x[1], reverse = True)
    print(f"sorted_teacher_list: {sorted_teacher_list}")
    return sorted_teacher_list



