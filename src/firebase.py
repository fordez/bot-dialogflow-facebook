import firebase_admin
import threading
from firebase_admin import firestore, credentials

cred = credentials.Certificate('keyfirebase.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def set(store, id, data):
    db.collection(store).document(id).set(data)

def getone(store, id):
    data = db.collection(store).document(id).get()
    if data.exists:
        print(f'Data: {data.to_dict()}')
        return data
    else:
        print(u'No such data!')

def getall(store,id):
    data = db.collection(store).where(id, u'==', True).stream()
    return data

def update(store, id, data):
    db.collection(store).document(id).update(data)

def delete(store, id):
    db.collection(store).document(id).delete()


callback_done = threading.Event()

def on_snapshot(doc_snapshot, changes, read_time):
  for doc in doc_snapshot:
    print(doc.id, doc.to_dict())
    callback_done.set()

db.collection('db1').document('1').on_snapshot(on_snapshot)
    


update('db1','1',{'name':'hola mundo jaime'})