Question Bank:

Easy: Introduce basic concepts

1.  
X = "Hello World"  
What Data Type is X?  
A. String (correct) B. Integer C. Boolean D. Char 

2.  
X = 1.0  
What Data Type is X?  
A. Integer B. Double (correct) C. String D. Char

3.  
How many bits are in a byte?  
A. 4 B. 2. C. 8 (correct) D. 12

4.  
How many bytes are in a megabyte?  
A. 1000000 (correct) B. 100000000 C. 100 D. 1000000000000

5.  
Convert Binary to Decimal: What is 1010 in decimal?  
A. 9 B. 8 C. 10 (correct) D. 4  

6.  
Convert Binary to Decimal: What is 0001 in decimal?
A. 0 B. 3 C. 4. D 1 (correct)

7.  
Pick the best password:
A. ABCDEF B. apple1234 C. 4rlyp3q@#9MYn24 (Correct) D. NSPHOUSCERATEME

Medium: Execute basic statements  

1.  
x = "Hello World"  
print(x)  
The code above would output?  
A. Hello World (correct) B. x C. x = "Hello World" D. "Hello World"

2.  
x = 5
if x == 5  
{  
     print(x)  
} 
else  
{  
  print("x is not 5")  
}  
The code above would output?  
A. x is not 5 B. nothing C. 5 (correct) D. 6  

3.
for(int i = 1; i <= 5; i++)  
{  
    print(i + " ")  
}  
The code above would output?  
A. i i i i i B. 1 2 3 4 C. 1 2 3 4 5 (correct) D. 0 1 2 3 4  

4.  
int x = 1
while ( x < 6 )
{  
   print(x + " ")  
}  
The code above would output?  
A. i i i i i B. 1 2 3 4 C. 1 2 3 4 5 (correct) D. 0 1 2 3 4  

5. How do you recognise a phishing scam?
A. Email the sender back and ask if they meant to send the email B. Click on the links in the email and fill out the forms  
C. Forward the email to everyone D. Look at the sender's email, verify any logos and do not respond to anything within the email (correct)


Hard: Algorithm questions?

1. Which of the folowing is considered a definite indicator of an incident?
A. Changes to system logs (correct) B. Activities at unexpected times C. Presence of new accounts D. Presence of unfamiliar files

2. Which data structure is indexable?  
A. Array (correct) B. Graph C. Linked List D. Tree

3. What layer is the data link layer in the OSI model?
A. First B. Second (Correct) C. Third D. Fourth 

4. What is a Linked List?
A. a data structure consisting of a collection of elements (values or variables), each identified by at least one index or key. B. a hierarchical tree structure, with a root value and subtrees of children with a parent node C. an ordered set of data elements, each containing a link to its successor (correct) D. a String

5. What runtime is the fastest?
A. O(nlogn) B. O(n) C. O(1) (correct) D. O(logn)



Concepts:

General: 
     - bits and bytes
     - Runtime

Data Structure:
     - Linked List
 
Programming: 
     - Data types: Integer, string, double, float, variables, and chars
     - If statements & Loops
     - Executing basic statements

Security and passwords
     - Security and phishing recognition
     - Memory allocation and recall, creating - arrays
     - OSI model and incident indication




ABOUT: 

Bits & Bytes  
     -There are 8 bits in a byte
     -
     
     
     
Programming
    - Primative Data Types
          - Int: 4, -4, 2, 234, 123, -398313
          - Double: 3.2, 4.0, 321.23
          - Float: 3.3f, -43.4f, 3f, 1.23e4        
          - Boolean: True, False
          - String: "Hello" , "3432342", "142342.12321", "2.123e4", " ", "A string can be any character"
     
     
     - Conditional Statements
          - Equals: a == b
          - Doesn't Equal: a != b
          - Less than: a<b
          - Less Than or equal to: a <=b
          - Greater than: a>b
          - Greater than or equal to: a >= b
          
    - Declairing a variable 
         ~In Java~
               - [data type] [variable_name];
               - int x;
               - String name;
               - boolean true_or_false
               - float f;
               - double d;
                    or
               - [data type] [variable_name] = [data]
               - int x = 5;
               - String name = "Paul";
               - bloolean true_or_false = false;
               - float f = 43.2e3f;
               - double d = 23.3;
               
         ~In Python~
               - [varialbe name] = [data]
               - Int
                    -x = 5
               - String
                    -name = "Johnny"
               - Boolean
                    -true_or_false = True
               - Float
                    - f = 34.34e2f
               - Double
                    - d = 4.3
              
              
              
    - Print Statements
          ~In Java~
               - using a variable 
          String helloworld = "Hello World"
          System.out.println(helloworld);
          
          output: Hello World
          
               -No variable
          System.out.println("Hello World") 
         
         output: Hello World
         
               - Concatination
         String name = "Johnny"
         System.out.println("Hello my name is " + name);
         
         output: Hello my name is Johnny
         
         
         ~In Python~
               - using a variable
          helloworld = "Hello World"
          print(helloworld
          
          output: Hello World
          
               - no variable
          print("Hello World")
          
          output: Hello World
          
                - Concatination
         name = "Johnny"
         print("Hello My name is ", name)
         
         output: Hello My name is Johnny
         
          
         
     - If Statements
          ~In Java~
           
           int age = 22;
           if(age > 16)
           {
           System.out.println("You are old enough to drive!!");
           }

          output: You are old enough to drive!!


          ~In Python~
          a = 22
          b = 16
          if a > b: 
               print("You are old enough to drive!!")
               
          output: You are old enough to drive!!     
               
   -If Else Statements
          ~In Java~
          
          int age = 10;
          if(age > 18)
          {
               System.out.println("You can vote") ;
          } 
          else
          {
               System.out.println("You are too young to vote");
          }
          
          output: You are too young to vote
          
          
          ~In Python~
          
          age = 10
          if age > 18:
               print("you are old enough to vote")
          else:
               print("you aren't old enough to vote")
               
          output: You aren't old enough to vote 
               
          
