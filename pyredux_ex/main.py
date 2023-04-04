import pyredux as redux

initial_state = {"count": 0}


def counter_reducer(state, action):
    if action["type"] == "INCREMENT":
        return {**state, "count": state["count"] + 1}

    elif action["type"] == "DECREMENT":
        return {**state, "count": state["count"] - 1}

    else:
        return state


store = redux.create_store(counter_reducer, initial_state)

# store.dispatch({"type": "INCREMENT"})
#
# state = store.get_state()
#
# print(state)  # Output: {"count": 1}
