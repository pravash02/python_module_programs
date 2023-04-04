def get_count(state):
    return state["count"]

count = get_count(store.get_state())
print(count)  # Output: 1