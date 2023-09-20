from application import db
from application.minions.models import Minion

db.drop_all()
print('Dropping database')
db.create_all()
print('Creating database')

print('Seeding database')
entry1 = Minion(name="Dave", appearance="Two-eyed and medium-sized minion with nice combed hair.")
entry2 = Minion(name="Bob", appearance="Short and bald with heterocromia. ")
entry3 = Minion(name="Kevin", appearance="Tall, two-eyed with sprout cut hair.")
entry4 = Minion(name="Jerry", appearance="Short and plump with spiky hair and two eyes.")
entry5 = Minion(name="Otto", appearance="Bigger than all the other minions with twelve sproutes of hair and braces.")

db.session.add_all([entry1, entry2, entry3, entry4, entry5])
db.session.commit()
