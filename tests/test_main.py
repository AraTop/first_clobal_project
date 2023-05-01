from utils import view_screem , data_sorted , return_data , data , open_json

def test_first():
   assert return_data(data) == data_sorted

def test_second():
   assert view_screem(data_sorted) == view_screem(data_sorted)

def test_three():
   assert type(open_json()) == list
