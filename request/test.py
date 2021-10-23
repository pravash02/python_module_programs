from request.dec_func import create_


create = create_("https://petstore.swagger.io/v2/user",
                 headers={
                     "accept": "application/json",
                     "content_type": "application/json"
                 },
                 auth=None,
                 json={
                     "id": 0,
                     "userStatus": 0
                 })

print(create.status_code)
print(create.json())
