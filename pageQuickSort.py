def do_sort(input_file):
  data_file = open(input_file)
  arr = []
  dict = {}
  for line in data_file.readlines():
    lpn = line.split()[0]
    arr.append(lpn)
    if lpn in dict:
      dict[lpn] += 1
    else:
      dict[lpn] = 1
  sorted_dict = sorted(dict.items(), key = lambda item: item[1])
  for i in range(1, 10):
    print(list(sorted_dict[-i]))

if __name__ == "__main__":
    do_sort("/Users/oseunghyeon/Desktop/--main/linkbench_short.trc")