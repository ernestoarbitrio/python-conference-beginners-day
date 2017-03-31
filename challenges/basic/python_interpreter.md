## Exercises

Practice using the **Python interpreter** as a calculator:
	1. The volume of a sphere with radius r is 43 πr 3. What is the volume of a sphere with radius 5? Hint: 392.7 is wrong!
	2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?


### Order of Operations

When more than one operator appears in an expression, the order of evaluation depends on the rules of precedence. For mathematical operators, Python follows mathematical convention. The acronym PEMDAS is a useful way to remember the rules:
- Parentheses have the highest precedence and can be used to force an expression to evaluate in the order you want. Since expressions in parentheses are evaluated first, 2 * (3-1) is 4, and (1+1)**(5-2) is 8. You can also use parentheses to make an expression easier to read, as in (minute * 100) / 60, even if it doesn’t change the result.
- Exponentiation has the next highest precedence, so 2**1+1 is 3, not 4, and 3*1**3 is 3, not 27.
- Multiplication and Division have the same precedence, which is higher than Addition and Subtraction, which also have the same precedence. So 2*3-1 is 5, not 4, and 6+4/2 is 8, not 5.
- Operators with the same precedence are evaluated from left to right (except expo­ nentiation). So in the expression degrees / 2 * pi, the division happens first and the result is multiplied by pi. To divide by 2π, you can use parentheses or write degrees / 2 / pi. 

I don’t work very hard to remember rules of precedence for other operators. If I can’t tell by looking at the expression, I use parentheses to make it obvious.