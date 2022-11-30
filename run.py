from puzzle import Puzzle

def main():
    p = Puzzle()
    if not p.validate():
        print("Something went wrong")
        return
    output = p.run()
    print(f'Params[Year: {p.year}, Day: {p.day}, Part: {p.part}]\nOutput: {output}')
    
if __name__ == "__main__":
    main()