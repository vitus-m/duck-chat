from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def btn_search_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.check_box_1.checked = False
    query = self.txt_area_query_input.text
    Notification("Query added!").show()
    response = f"Here is input:\n{query}"
    self.txt_area_response.text = response
    self.check_box_1.checked = True
    Notification("Done!").show()
