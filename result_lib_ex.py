# def divide(a: int, b: int) -> int:
#     try:
#         if b == 0:
#             raise ValueError("Cannot divide by zero")
#         return a // b
#     except ValueError as e:
#         return str(e)
#
# values = [(10, 0), (10, 5)]
# for a, b in values:
#     result = divide(a, b)
#     if isinstance(result, int):
#         print(f"{a} // {b} == {result}")
#     else:
#         print(result)

from result import Result, Ok, Err

def divide(a: int, b: int) -> Result[int, str]:
    if b == 0:
        return Err("Can't divide by zero")
    return Ok(a // b)

values = [(10, 0), (10, 5)]
for a, b in values:
    match divide(a, b):
        case Ok(value):
            print(f"{a} // {b} == {value}")
        case Err(e):
            print(e)