from datetime import date
class hotel:
    def __init__(self):
        self.rooms={}
        self.avl_rooms={'std':[101,102,103],'deluxe':[201,202,203],'elite':[301,302,303],'h.offc':[401,402,403]}
        self.roomprice={1:2000,2:4000,3:6000,4:8000}
        pass
    def checkin(self,name,address,phone):
        roomtype=int(input("room type:\n1.standard \n2.deluxe \n3.elite \n4.h.offc \nSelect a room type:"))
        if roomtype==1:
            if self.avl_rooms['std']:
                room_no=self.avl_rooms['std'].pop(0)
            else:
                print("sorry,standard rooms not available")
                return
        if roomtype==2:
            if self.avl_rooms['deluxe']:
                room_no=self.avl_rooms['deluxe'].pop(0)
            else:
                print("sorry,deluxe rooms not available")
                return
        if roomtype==3:
            if self.avl_rooms['elite']:
                room_no=self.avl_rooms['elite'].pop(0)
            else:
                print("sorry,elite rooms not available")
                return
        if roomtype==4:
            if self.avl_rooms['h.offc']:
                room_no=self.avl_rooms['h.offc'].pop(0)
            else:
                print("sorry,h.offc rooms not available")
                return
        else:
            print("choose a valid room type")
        d,m,y=map(int,input('enter check-in-date in date,month,year').split())
        check_in=date(y,m,d)
        self.rooms[room_no]= {
            'name':name,
            'address':address,
            'check_in_date':check_in,
            'room_type':roomtype,
            'roomservice':0
        }
        print(f"checked in{name},{address} to room:{room_no} on {check_in}")
    def room_service(self,room_num):
        if room_num in self.rooms:
            print("******star hotel menu*****")
            print("1.tea/coffee:RS.20 2.dessert:70 3.breakfast:100 4.lunch:150 5.dinner:120 6.exit")
            while 1:
                c=int(input("select your choice"))
                if c==1:
                    q=int(input("enter the quantity:"))
                    self.rooms[room_num]['roomservice']+=20*q
                elif c==2:
                      q=int(input("enter the quantity:"))
                      self.rooms[room_num]['roomservice']+=70*q
                elif c==3:
                      q=int(input("enter the quantity:"))
                      self.rooms[room_num]['roomservice']+=100*q
                elif c==4:
                      q=int(input("enter the quantity:"))
                      self.rooms[room_num]['roomservice']+=150*q
                elif c==5:
                       q=int(input("enter the quantity:"))
                       self.rooms[room_num]['roomservice']+=120*q
                elif c==6:
                    break;
                else:
                    print("invalid option")
            print("Room service rs:",self.rooms[room_num]['roomservice'],"\n")
        else:
            print("invalid room number")
    def display_occupied(self):
        if not self.rooms:
            print("no rooms are occupied at the moment.")
        else:
            print("oocupied rooms: ")
            print("----------------------")
            print('room num  name')
            print("----------------------")
            for room_num,details in self.rooms.items():
                print(room_num,'\t',details['name'])
    def check_out(self,room_number):
        if room_number in self.rooms:
            check_out_date=date.today()
            check_in_date=self.rooms[room_number]['check_in_date']
            duration=(check_out_date - check_in_date).days
            roomtype=self.rooms[room_number]['room_type']
            if roomtype==1:
                self.avl_rooms['std'].append(room_number)
            elif roomtype==2:
                 self.avl_rooms['deluxe'].append(room_number)
            elif roomtype==3:
                 self.avl_rooms['elite'].append(room_number)
            elif roomtype==4:
                 self.avl_rooms['h.offc'].append(room_number)
            print("--------------------------")
            print('star hotel reciept')
            print(f"name:{self.rooms[room_number]['name']}\nAddress:{self.rooms[room_number]['address']}")
    
            print(f"Room number:{room_number}")
            print(f"check_in_date: {check_in_date.strftime('%d %B %y')}")
            print(f'check_out_date:{check_out_date.strftime("%d %B %y")}')
            print(f'no.of.days: {duration}\tprice per day:rs.{self.roomprice[roomtype]}')
            roombill=self.roomprice[roomtype]*duration
            roomservice=self.rooms[room_number]['roomservice']
            print('Room bill:RS',roombill)
            print('Roomservice:RS',roomservice)
            print('Totalbill:',roombill+roomservice)
            del self.rooms[room_number]
        else:
            print(f"Room{room_number} is not occupied.")
    def startapp(self):
        while True:
            print("---------------------")
            print("welcome to Star hotel")
            print("1.checkin")
            print("2.room service")
            print("3.display occupied rooms")
            print("4.checkout")
            print("5.exit")
            choice=input("enter your choice(1 to 5): ")
            if choice == '1':
                name=input("enter the name:")
                address=input("enter the address: ")
                phone=int(input("enter the contact number: "))
                self.checkin(name,address,phone)
            elif choice == '2':
                room_num=int(input("select room num: "))
                self.room_service(room_num)
            elif choice == '3':
                self.display_occupied()
            elif choice == '4':
                room_number=int(input("enter the room number: "))
                self.check_out(room_number)
            elif choice == '5':
                break; 
            else:
                print("invalid choice please try again")
h=hotel()
h.startapp()

                

