from pickle import load
from pandas import DataFrame


def predict_model(q1, q2, q3, q4,
                  q5, q6, q7, q8,
                  q9, q10, q11, q12,
                  q13, q14, q15, q16,
                  q17, q18, q19, q20,
                  q21, q22, q23, q24,
                  q25, q26, q27, q28):

    scaler = load(open('./saved_model/scaler.pickle', 'rb'))
    pca = load(open('./saved_model/pca.pickle', 'rb'))
    model = load(open('./saved_model/model.pickle', 'rb'))
    data = {
        'q1': [q1],
        'q2': [q2],
        'q3': [q3],
        'q4': [q4],
        'q5': [q5],
        'q6': [q6],
        'q7': [q7],
        'q8': [q8],
        'q9': [q9],
        'q10': [q10],
        'q11': [q11],
        'q12': [q12],
        'q13': [q13],
        'q14': [q14],
        'q15': [q15],
        'q16': [q16],
        'q17': [q17],
        'q18': [q18],
        'q19': [q19],
        'q20': [q20],
        'q21': [q21],
        'q22': [q22],
        'q23': [q23],
        'q24': [q24],
        'q25': [q25],
        'q26': [q26],
        'q27': [q27],
        'q28': [q28],
    }
    predict_df = DataFrame(data=data)
    predict_df = pca.transform(predict_df)
    predict_df = scaler.transform(predict_df)
    result = model.predict(predict_df)
    if result == 0:
        result = 'Like'
    elif result == 1:
        result = 'Neutral'
    else:
        result = 'Dislike'

    return result
