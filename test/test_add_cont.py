from model.contact import Contact


def test_add_contact(app):
    app.contact.add_new_contact(Contact(first_name="Taras", last_name="Balyuk", mobile_phone="2244270997"))
