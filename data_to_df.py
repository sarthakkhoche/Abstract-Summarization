import os
# with open("./Parsed_Papers/S0142694X1500054X.txt", "r") as file: 
#     data = file.readlines() 
#     # print(len(data))
#     count = 0
#     start = 3
#     end = 3
#     tag = ""
#     for line in data:
#         if (line[:3] == '@&#'):
#             i = 3
#             while(i < len(line)):
#                 if (line[i] == '@'):
#                     end = i
#                     break
#                 i += 1
#             tag = line[start:end] 
#             print(tag)

columns = []
for file in os.listdir("Parsed_Papers"):
    with open("./Parsed_Papers/S0142694X1500054X.txt", "r") as file: 
        data = file.readlines() 
        
        start = 3
        end = 3
        tag = ""
        flag = 0
        for line in data:
            if (line[:3] == '@&#'):
                flag = 1^flag
                i = 3
                while(i < len(line)):
                    if (line[i] == '@'):
                        end = i
                        break
                    i += 1
                tag = line[start:end]
                if (tag not in columns): 
                    columns.append(tag)
            # else:
            #     if (line[:3] == '@&#'):
            #         flag = 1^flag
                
            #     if (flag == 1):
                
            #     # print(tag)
