

def test_del_group(app):
    app.session.login(username="admin", password="secret")
    app.group.del_first_group()
    app.session.logout()
