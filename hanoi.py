def tower_of_hanoi(n, source , helper , destination):
    if n == 1:
        print("move disk 1 from", source, "to" , destination)
        return
    tower_of_hanoi (n-1 , source, destination, helper)
    print("move disk", n , "from" , source , "to" , destination)
    tower_of_hanoi(n-1 , helper , source , destination)
n = int(input("enter number of disks : "))
tower_of_hanoi(n , "A" , "B", "C" )
print("total moves : " , (2 ** n ) - 1)
        
