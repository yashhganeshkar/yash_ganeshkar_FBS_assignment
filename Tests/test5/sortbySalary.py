
Data = [
    [101,"Seema",45000],
    [340,"Rajani",13000],
    [210,"Tannu",14000],
    [320,"Suresh",35000]
]


for ele in range(1, len(Data)):
    for i in range(len(Data)-ele):
        if(Data[i][2] > Data[i+1][2]):
            Data[i][2], Data[i+1][2] = Data[i+1][2], Data[i][2]

print(Data)