"""Test beans.py"""

from streamlit.testing.v1 import AppTest

# ---------------------------------------------------------------------------
# Simple tests
# ---------------------------------------------------------------------------

# You retrieve elements
# - By order on page (e.g., [0])
# - Via key
# - Via container then element e.g., at.form(key="signup").text_input[0]

def test_increment_and_add():
    """User increments number input then clicks Add"""

    # Initialise and run app
    at = AppTest.from_file("../pages/beans.py").run()

    # Increment number then run
    at.number_input(key="bean_increment").increment().run()

    # Click button then run
    at.button(key="bean_add").click().run()

    # Check markdown
    assert at.markdown[0].value == "Beans counted: 1"


def test_selectbox():
    at = AppTest.from_file("../pages/beans.py").run()
    assert at.selectbox[0].value == None
    assert at.selectbox[0].label == "A"
    assert at.selectbox[0].options == ["1","2","3"]
    assert at.selectbox[0].index == None
    assert at.selectbox[0].help == "Pick a number"
    assert at.selectbox[0].placeholder == "Pick me"
    assert at.selectbox[0].disabled == False
