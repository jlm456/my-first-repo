#this is the email_service_test file...


from app.email_service import send_email


def test_email_sending():

    assert send_email() == 202



