from constant import DATA_FOR_DICT
from converter import convert_list_to_dict

def main():
  print(f"before converting:\n\n {DATA_FOR_DICT}\n\n after converting:\n\n\
  {convert_list_to_dict(DATA_FOR_DICT)}")

if __name__== "__main__":
  main()