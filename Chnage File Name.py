import os

def main():
    count = 1
    for filename in os.listdir('Testing'):
        os.rename("Testing/"+filename,"Testing/"+str(count)+".txt")
        count += 1
main()