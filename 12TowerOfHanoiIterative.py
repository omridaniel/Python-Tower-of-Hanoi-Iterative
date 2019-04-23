'''
Name: Omri Daniel
Date: 10/26/2018
Desc: Tower of Hanoi Iterative Method
Note: COMMENTS AND PRINTING MAY BE OFF ASK TO VIEW ON MY COMPUTER IN CLASS IF NEEDED
'''
#Tower/Stack Class
class Stack:
    def __init__(self,name):
        self.items = []
        self.name=name

    def __str__(self):
    	return str(self.items)

    def push(self, item): self.items.append(item)

    def pop(self): return self.items.pop()

    def peek(self): return self.items[len(self.items)-1]

    def size(self): return len(self.items)
    
    def moveRingTo(self,newPeg,move):									#Function to move the rings
    		newPeg.push(self.peek())
    		self.pop()
    		print('\nMove:',move,'\n'+'Moved a disk from',self.name,'to',newPeg.name)	#Describes the move just made and the num move(pic.2)

    def validMove(self,other,move):										#Function to check if move is valid
    	if self.size()>0 and (other.size()==0 or self.peek()<other.peek()):	#Algorithim followed from the word doc 
    		self.moveRingTo(other,move)
    	elif other.size()>0 and (self.size()==0 or other.peek()<self.peek()): 
    		other.moveRingTo(self,move)

    def highestTower(self,other,another):								#Function to check which tower has most rings and how many it has
    	if self.size()>other.size() and self.size()>another.size(): 	#Series of if statements to compare stack with most items
    		return self.size()											#Return the length of stack with most items
    	elif other.size()>self.size() and other.size()>another.size():
    		return other.size()
    	else: 
    		return another.size()

#Functions
def oddPlay(move):														#Function called when there are odd num of rings
	pegA.validMove(pegC,move)
	move+=1															
	if pegC.size()!=rings:
		printTower()													#Calls print after each move made
		pegA.validMove(pegB,move)
		move+=1															#Updates move after each move made
		printTower()
		pegB.validMove(pegC,move)
		move+=1
	printTower()
	return move 														#Returns move to update the number of moves made

def evenPlay(move):														#Function called when there are even num of rings
	pegA.validMove(pegB,move)
	move+=1																#Updates move after each move made
	printTower()														#Calls print function after each move made
	pegA.validMove(pegC,move)
	move+=1
	printTower()
	pegB.validMove(pegC,move)
	move+=1
	printTower()
	return move 														#returns move to update num of moves made

def printTower():														#very inefficent Print function (Not a part of stack class because was not necessary)
	print('Tower 1:',pegA,'\n'+'Tower 2:',pegB,'\n'+'Tower 3:',pegC)	#Print each tower as list(pic.1)
	for i in range(pegA.highestTower(pegB,pegC)-1,-1,-1):				#Takes range of most items but backwords to allow indexing
		
		if pegA.highestTower(pegB,pegC)-1==i:
			for k in range(rings-i): 
				print()
				for j in range(3): print('|',end=' '*19)				#nested loop to add in the missing poles for each tower
																		#Slightly off centered for printing but closest I got for horizontal method (pic.2)
		if pegA.highestTower(pegB,pegC)==pegA.size():					#be nice i spent 2 days on printing :'( 
			print('\n'+'='*pegA.items[i]*2,end=' '*(20-pegA.items[i]*2)) #since tower A has most rings begin with printing its rings
			
			if pegB.size()==i+1: 
				print('='*pegB.items[i]*2,end=' '*(20-pegB.items[i]*2))	#If size adds up with i then call for the ring to be printed based on i
			else: 
				print('|',end=' '*20)									#Else just put in pole

			if pegC.size()==i+1: 										#Same if/else check for other towers
				print('='*pegC.items[i]*2,end=' '*(20-pegC.items[i]*2))
			else:
				print('|',end='')

		elif pegA.highestTower(pegB,pegC)==pegB.size():					#Aboe steps repeated for each other tower to ensure proper printing order(ya ya ya not efficent sorry :/ )
			if pegA.size()==i+1:
				print('\n','='*pegA.items[i]*2,end=' '*(20-pegA.items[i]*2))
			else:
				print('\n|',end=' '*20)

			print('='*pegB.items[i]*2,end=' '*(20-pegB.items[i]*2))

			if pegC.size()==i+1: 
				print('='*pegC.items[i]*2,end=' '*(20-pegC.items[i]*2))
			else: 
				print('|',end='')

		else:
			if pegA.size()==i+1:
				print('\n','='*pegA.items[i]*2,end=' '*(20-pegA.items[i]*2))
			else:
				print('\n|',end=' '*20)

			if pegB.size()==i+1: 
				print('='*pegB.items[i]*2,end=' '*(20-pegB.items[i]*2))
			else:
				print('|',end=' '*20)

			print('='*pegC.items[i]*2,end=' '*(20-pegC.items[i]*2))

	print('\n'+'#'*60)													#Print for bottum bar (The above was really not a fun time :((( but i put lots of comments :) )

#Main Loop prep
move=1																	#Declaring necessary classes and move to count moves made
pegA=Stack('first')
pegB=Stack('second')
pegC=Stack('third')

while True:																#While loop for input using try and except to recieve only integer 1-6 so doesnt crash/take long 
	try:
		rings=int(input('Please enter an integer(1-6) number for the amount of rings: '))
		if 0<rings<7: break
	except:
		pass

for r in range(rings,0,-1): pegA.push(r)								#Set up the stack with proper amount of rings and prints them
printTower()

#Main Loop
while pegC.size()!=rings:												
	if rings%2==1: move=oddPlay(move)									#If rings num is odd call go through odd moves
	else: move=evenPlay(move)											#If even go through even moves
print('Tower of Hanoi completed.')										#End game output