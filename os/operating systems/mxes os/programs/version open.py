while not end:
                    file_name=input(f"> What is the name of the file you want to open? to exit program input end\n> ")
                    if file_name!="end":
                        with open(file_name) as f:
                            code = f.read()
                            exec(code)
                    else:
                        end=True