
"""
Needs to return:

FROM: key:values that were changed.
TO: Actual values that were actually changed.

actual values...
{
  "id":123,
  "name":"John",
  "last_name":"Doe",
  "phone":353672933
}

updated values..
{
  "id":123,
  "name":"Elias",
  "last_name":"Doe",
  "phone":353672933
}



{
    "id": 1234,
    "code": "applicants.model.applicant.update",
    "input_data": {
        "id": 45,
        "from": {
            "name": "John"
        },
        "to": {
            "name": "Elias"
        }
    }
    "user_id": 2,
    "created_at": "2021-11-05 16:20:32"
}
"""
# Change values to see the difference..
item_1 = {
  'id': '0c0b55b3-e4c8-4668-b458-e1a7e63e6w73d',
  'type': 1,
  'name': "flue"}

item_2 = {
  'id': '0c0b55b3-e4c8-4668-b458-e1a7e63e673d',
  'type': 0,
  'name': "flu"}

item_1_set = set(item_1.items())
item_2_set = set(item_2.items())

changed_value = dict(item_2_set - item_1_set)


def compare(first, second):
    # get similar keys from each dictionary.
    # return only what was changed.
    sharedKeys = set(first.keys()).intersection(second.keys())
    compared = {k:second[k] for k in sharedKeys}
    return compared 

print(compare(changed_value, item_1))


value = {
  "from": compare(changed_value, item_1),
  "to":changed_value
}

print("VALUE -->", value)


