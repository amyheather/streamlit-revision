from streamlit.testing.v1 import AppTest

def test_balloons():
    at = AppTest.from_file("../app.py").run()

    at.switch_page("pages/first.py")
    at.session_state["magic_word"] = "Balloons"

    at.switch_page("pages/second.py").run()
    assert at.markdown[0].value == ":balloon:"
