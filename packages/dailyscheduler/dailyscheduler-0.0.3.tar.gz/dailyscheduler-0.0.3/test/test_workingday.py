import datetime
import unittest
from dailyscheduler.abstract_classes import Task
from dailyscheduler.classes import WorkingDay


class TaskSubclass(Task):
    id = None
    additional_1 = None
    additional_2 = None
    
    def __init__(self, from_hour: datetime.time, to_hour: datetime.time, id: int, additional_1=None, additional_2=None):
        super().__init__(from_hour, to_hour, id)
        self.id = id
        self.additional_1 = additional_1
        self.additional_2 = additional_2
    
    def __str__(self):
        return "TaskSubclass"

class TestDay(unittest.TestCase):
    
    def test_correct_init(self):
        """ Test if the Day class is initialized correctly """ 
        WorkingDay(start=8, end=16, slot_duration=5)
        
    def test_incorrect_init(self):
        pass
    
    def test_hours(self):
        """ Test if the hours property returns the correct value """
        day = WorkingDay(start=8, end=16, slot_duration=5)
        self.assertEqual(day.hours, 8)

    def test_length(self):
        """ Test if the __len__ method returns the correct value """
        day = WorkingDay(start=8, end=16, slot_duration=5)
        self.assertEqual(len(day), 96)

    def test_get_hour_index(self):
        """ Test if the get_hour_index method returns the correct index """
        day = WorkingDay(start=8, end=16, slot_duration=5)
        self.assertEqual(day.get_hour_index(datetime.time(8, 0)), 0)
        self.assertEqual(day.get_hour_index(datetime.time(13, 30)), 66)
        self.assertEqual(day.get_hour_index(datetime.time(15, 30)), 90)

    def test_slot_to_hour(self):
        """ Test if the slot_to_hour method returns the correct hour """
        day = WorkingDay(start=8, end=16, slot_duration=5)
        self.assertEqual(day.slot_to_hour(0), datetime.time(8, 0))
        self.assertEqual(day.slot_to_hour(11), datetime.time(8, 55))
        self.assertEqual(day.slot_to_hour(15), datetime.time(9, 15))
        
    def test_get_hour_index_outside_working_hours(self):
        """ Test if the get_hour_index method raises ValueError for hours outside working hours """
        day = WorkingDay(start=8, end=16, slot_duration=5)
        with self.assertRaises(ValueError):
            day.get_hour_index(datetime.time(7, 0))
        with self.assertRaises(ValueError):
            day.get_hour_index(datetime.time(17, 0))

    def test_slot_to_hour_outside_working_hours(self):
        """ Test if the slot_to_hour method raises ValueError for slots outside working hours """
        day = WorkingDay(start=8, end=16, slot_duration=5)
        with self.assertRaises(ValueError):
            day.slot_to_hour(-1)
        with self.assertRaises(ValueError):
            day.slot_to_hour(96)

    def test_get_hour_index_seconds_time(self):
        """ Test if the get_hour_index method raises ValueError for time with seconds """
        day = WorkingDay(start=8, end=16, slot_duration=5)
        day.get_hour_index(datetime.time(8, 30, 15))
        self.assertEqual(day.get_hour_index(datetime.time(8, 33, 15)), 6) ## 8:30:00 - 8:34:59 is 6th slot

    def test_slot_to_hour_invalid_slot(self):
        """ Test if the slot_to_hour method raises ValueError for invalid slot """
        day = WorkingDay(start=8, end=16, slot_duration=5)
        with self.assertRaises(ValueError):
            day.slot_to_hour(100)

    def test_get_hour_index_exact_end_time(self):
        """ Test if the get_hour_index method returns the correct index for the exact end time """
        day = WorkingDay(start=8, end=16, slot_duration=5)
        self.assertEqual(day.get_hour_index(datetime.time(15, 55)), 95) ## beacause last hour (16:00) is not included

    def test_slot_to_hour_exact_end_slot(self):
        """ Test if the slot_to_hour method returns the correct hour for the exact end slot """
        day = WorkingDay(start=8, end=16, slot_duration=5)
        self.assertEqual(day.slot_to_hour(95), datetime.time(15, 55))
        
    def test_base_methods_fails(self):
        day = WorkingDay(start=8, end=16, slot_duration=5)
        with self.assertRaises(ValueError):
            day.get_hour_index(datetime.time(7, 0))
    
if __name__ == '__main__':
    unittest.main(verbosity=2)