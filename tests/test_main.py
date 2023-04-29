from utils import view_screem , data_sorted , return_data , data

def test_first():
   assert return_data(data) == data_sorted

def test_second():
   assert type(data_sorted) == list

