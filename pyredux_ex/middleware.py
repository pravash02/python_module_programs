import redux


def logger_middleware(store):
    def logger(next):
        def middleware(action):
            print(f"Action: {action}, State: {store.get_state()}")
            return next(action)
        return middleware
    return logger


store = redux.create_store(counter_reducer, initial_state, middleware=[logger_middleware])