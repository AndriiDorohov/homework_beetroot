# python mymod.py ../text_files/quote.txt


import sys

print("mymod.py")

def count_lines(read_data_l):
      print(f"Number of lines in the text:  {len(read_data_l)}")

def count_chars(read_data_s):
      print(f"Number of characters in the text:  {len(read_data_s)}")

def test(name):
    with open(name, encoding="utf-8") as f:
          read_data_l = f.readlines()
          f.seek(0)
          read_data_s = f.read()
          count_lines(read_data_l)
          count_chars(read_data_s)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mymod.py <file_name>")
    else:
        test(sys.argv[1])
