from typing import Final
def greet(name:str)-> str:
    print(name)
    return f"Welcome, {name.title}"
#def add(x: int , y: int) -> int:
    #return x + y
#def area_circle(radius: float) -> float:
 #   pi = 3.14
  #  PI:  Final = 3.14
   # return PI * (radius ** 2)
def has_passed(average: float) -> bool:
    return  average >= 50
def compute_average(scores: list[int]) -> float:
    return sum(scores) / len(scores)
def students_performance() -> None:
    name: str = input("Enter student name: ")
    print(greet(name))
    scores: list[int] = []
    for i in range(3):
        while True:
            try:
                score = int(input(f"Enter score for subject {i+1}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be btwn 0 & 100")
            except ValueError:
                print("Please a valid number")
    average_score: float = compute_average(scores)
    is_pass: bool = has_passed(average_score)
    print("\n ---- Report Card ---- ")
    print(f"Name           : {name}")
    print(f"Scores         : {scores}")
    print(f"Average        :{average_score:.2f}")
    print(f"Status         :{'Pass' if has_passed else 'Fail'}")

    assignments_done: int = 5
    pts: float = 2.5
    total_score: float = average_score + pts

students_performance()
