def load_model_from_file():
    with open("weight", "r") as f:
        model = f.read().encode("utf-8")
        print(model)

def load_model_from_python():
    from weight import model
    return model


if __name__ == "__main__":
    # load_model_from_file()
    load_model_from_python()
    import findlang
    print(findlang.classify("This is a test"))