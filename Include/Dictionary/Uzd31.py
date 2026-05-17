Score = {
    "Matematika" : 6,
    "Russian" : 7,
    "Latvian" : 4,
    "English" : 5,
    "Fizika" : 3
}
print(Score)

Score["Fizika"] = 5
Score["VAM"] = "None"
del Score["Russian"]
print(Score)