goods_category_num_dict = {'name': 1,
                  'code': 6734,
                  'dept': 12,
                  'deptd': 13
                  }
title = 'dfdsdf'
num = 1
for key in goods_category_num_dict.keys():
    print(key)
    if key in title:
        num = goods_category_num_dict[key]
        break
print(num)
