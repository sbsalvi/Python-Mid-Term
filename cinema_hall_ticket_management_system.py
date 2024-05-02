class Star_Cinema:
    hall_list=[]

    def entry_hall(self,hall_info):
        self.hall_list.append(hall_info)
        
class Hall:
    def __init__(self,rows,cols,hall_no):
        self.seats={}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        Star_Cinema().entry_hall(self)
    
    def entry_show(self,id,movie_name,time):
        show=(id,movie_name,time)
        self.show_list.append(show)

        r=[]
        for i in range(self.rows):
            c=[]
            for j in range(self.cols):
                c.append('0')
            r.append(c)
        ids={id:r}
        self.seats.update(ids)
    def book_seats(self,show_id,total_seat):
        if show_id in self.seats:
            seat_book=[]
            for i in range(total_seat):
                while True:
                    row=int(input("Enter Row: "))
                    col=int(input("Enter Col: "))
                    if(0<row<=self.rows and 0<col<=self.cols):
                        if(self.seats[show_id][row][col]=='X'):
                            print("Seat is booked")
                        else:
                            self.seats[show_id][row][col]='X'
                            seat_book.append((row,col))
                            break
                    else:
                        print("Invalid seat")
                        continue
            print(f"Your seat {seat_book} is booked")
        else:
            print("Invalid show_id")

    def view_show_list(self):
        for i in self.show_list:
            print(f"Show id : {i[0]} , Movie name : {i[1]} , Time : {i[2]}")
    
    def view_available_seats(self,show_id):
        if show_id in self.seats:
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.seats[show_id][i][j]=='0':
                        print("[0]",end=" ")
                    else:
                        print("[X]",end=" ")
                print("\n")
        else:
            print("Invalid show id")

movie=Hall(5,6,1)
movie.entry_show("2009","The Dark Knight","10:30 AM")
movie.entry_show("2010","Inception","03:30 AM")

while True:
    print("1.View all show today")
    print("2.View available seat")
    print("3.Book ticket")
    print("4.Exit")

    option=int(input("Enter Option: "))

    if option==1:
        movie.view_show_list()
    elif option==2:
        show_id=input("Enter show id: ")
        movie.view_available_seats(show_id)
    elif option==3:
        Show_id=input("Enter show id: ")
        Total_seat=int(input("Enter total seat to book: "))
        movie.book_seats(Show_id,Total_seat)
    elif option==4:
        break
    else:
        print("Invalid Option")
