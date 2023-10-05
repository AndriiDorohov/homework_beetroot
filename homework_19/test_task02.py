from unittest import TestCase
import os
from task_01 import FileManager


class TestFileManager(TestCase):
    def test_init(self):
        with FileManager("temp.txt", "w") as opened_file:
            opened_file.write_log("test run")

        with FileManager("temp.txt", "r") as file:
            text = file.file_name.read()
            self.assertEqual(text, "test run")

    def test_enter(self):
        with FileManager("temp.txt", "w") as opened_file:
            self.assertEqual(FileManager.get_num_of_usage(), 3)

        with FileManager("temp.txt", "w") as opened_file:
            self.assertEqual(FileManager.get_num_of_usage(), 4)

    def test_exit(self):
        with FileManager("temp.txt", "w") as opened_file:
            pass

        self.assertFalse(os.path.exists("temp.txt"))

    def test_error(self):
        with self.assertRaises(FileNotFoundError):
            with FileManager("none.txt", "r") as opened_file:
                pass


if __name__ == "__main__":
    unnitest.main()
