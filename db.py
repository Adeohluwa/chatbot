import firebase_admin
from firebase_admin import credentials, auth, firestore


if not firebase_admin._apps:
    cred = credentials.Certificate("babcock-6b68d-firebase-adminsdk-zakzq-be757502db.json")
    default_app = firebase_admin.initialize_app(cred)

db = firestore.client()


def save_feedback(user_id, feedback_text, rating):
    feedback_data = {
        'feedback': feedback_text,
        'rating': rating,
        'timestamp': firestore.SERVER_TIMESTAMP
    }
    doc_ref = db.collection('Feedback').document(user_id)
    doc_ref.set(feedback_data)



def save_enquiry(user_id, enquiry_text):
    enquiry_data = {
        'enquiry': enquiry_text,
        'status': 'pending',
        'timestamp': firestore.SERVER_TIMESTAMP
    }

    doc_ref = db.collection('Enquiries').document(user_id)
    doc_ref.set(enquiry_data)


def get_pending_enquiries():
    enquiries = db.collection('Enquiries').where('status', '==', 'pending').stream()
    pending_enquiries = []

    for enquiry in enquiries:
        enquiry_data = enquiry.to_dict()
        enquiry_data['id'] = enquiry.id
        pending_enquiries.append(enquiry_data)

    return pending_enquiries