id_count = [{'id': 33, 'star': 2, 'count': 3}]
all_list = [{'power': 20710, 'id': 33, 'skills': "", 'rank': 0, 'lv': 1, 'star': 1},
            {'power': 22296, 'id': 49, 'skills': "", 'rank': 0, 'lv': 1, 'star': 2},
            {'power': 25029, 'id': 53, 'skills': "", 'rank': 0, 'lv': 1, 'star': 3}]

for single_partner_info in all_list:
    flag = False
    for each in id_count:
        if each['id'] == single_partner_info['id']:
            each['count'] += 1
            flag = True
            break
    if not flag:
        id_count.append({'id': single_partner_info["id"], 'star': single_partner_info["star"], 'count': 1})

print(id_count)

# for single_partner_info in all_list:
#     flag = False
#     for each in id_count:
#         if ("id", single_partner_info["id"]) in each.items():
#             each["count"] += 1
#             flag = True
#     if not flag:
#         id_count.append(dict(id=single_partner_info["id"], star=single_partner_info["star"], count=1))
#
# print(id_count)
