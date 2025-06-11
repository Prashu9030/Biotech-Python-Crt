Size=int(input("Enter the Number of songs :"))
Play_List=[]
for i in range(Size):
    song_name=input(f"Enter the Song number  :")
    Play_List.append(song_name)
print(Play_List)
print(Play_List[::-1])