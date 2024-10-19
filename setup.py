import os

# Define the chapters and their content
chapters = {
    "introduction.tex": r"""
\chapter{Introduction: The Beauty of Math for Everyone}
\section{Purpose of the Book}
Everyone can learn math. The purpose of this book is to simplify higher math and make it accessible to all learners, regardless of background or prior experience.
We will build from the foundations of basic math to the most advanced concepts, using clear explanations, real-life examples, and intuitive exercises.

\section{Overcoming Fear of Math}
Many people fear math because they think it’s too hard or that they’re just not good at it. This book takes a growth mindset approach, showing you that anyone can understand math by breaking down each concept step by step.

\section{The Language of Math}
We use math every day without even realizing it. This section will highlight how math is woven into our daily lives and why it’s an essential language for understanding the world around us.
""",
    "foundation.tex": r"""
\chapter{The Foundation of All Math – Addition and Subtraction}
\section{Why Start Here?}
Addition and subtraction are the building blocks of all mathematical concepts. If we think of math as a language, then addition and subtraction are the alphabet—simple yet powerful tools that help us solve problems, from everyday tasks to complex equations.
Let’s begin by understanding these basic operations deeply. Whether you’re managing your budget, dividing something between friends, or calculating distances, these two operations are always at play.

\section{What Is Addition?}
Addition is the process of combining two or more numbers to get a larger number. Think of it like this:
If you have 3 apples and someone gives you 2 more apples, how many apples do you have in total?
\begin{example}
You have 3 apples. Someone gives you 2 more apples. How many apples do you have now?
Solution: 3 apples + 2 apples = 5 apples.
\end{example}

\subsection{What Is Subtraction?}
Subtraction is the process of taking one number away from another. For example, if you have 5 apples and you give 2 away, how many apples do you have left?
\begin{example}
You have 5 apples. You give 2 apples away. How many apples do you have now?
Solution: 5 apples - 2 apples = 3 apples.
\end{example}

\subsection{Practice Makes Perfect: Let’s Try Some Exercises!}
Practice is key to mastering addition and subtraction. Here are some exercises to help you get started.

\subsection{Simple Addition:}
\begin{itemize}
  \item 1 + 1 = 2
  \item 4 + 3 = 7
  \item 10 + 20 = 30
\end{itemize}

\subsection{Simple Subtraction:}
\begin{itemize}
  \item 5 - 2 = 3
  \item 10 - 4 = 6
  \item 20 - 10 = 10
\end{itemize}

\section{Making It Real:}
Addition and subtraction are used in real-life scenarios, such as budgeting, shopping, and cooking.

\section{The Properties of Addition and Subtraction}
\subsection{Commutative Property of Addition}
The order in which you add numbers does not change the sum. For example, 2 + 3 is the same as 3 + 2.

\subsection{Associative Property of Addition}
The way in which numbers are grouped when adding does not change the sum. For example, (1 + 2) + 3 is the same as 1 + (2 + 3).

\subsection{Subtraction is not Commutative}
The order in which you subtract numbers does change the result. For example, 5 - 3 is not the same as 3 - 5.

\section{Breaking It Down: How to Approach Word Problems}
Word problems can be broken down into smaller, manageable steps.

\section{Solve it!}
\subsection{Step 1: Identify what we know.}
\subsection{Step 2: Write the math problem:}
\subsection{Step 3: Solve it. Sarah now has 8 marbles.}

\section{Summary}
Addition and subtraction are fundamental operations in math. Mastering these concepts is essential for progressing to more advanced topics.

\subsection{Challenge Question}
Try solving this challenge question to test your understanding.

\section{Overcoming Fear of Math}
Many people fear math because they think it’s too hard or that they’re just not good at it. This book takes a growth mindset approach, showing you that anyone can understand math by breaking down each concept step by step.

\section{The Language of Math}
We use math every day without even realizing it. This section will highlight how math is woven into our daily lives and why it’s an essential language for understanding the world around us.
""",
    "fractions_decimals_percentages.tex": r"""
\chapter{Fractions, Decimals, and Percentages}
\section{Fractions}
Fractions represent parts of a whole. This section will explain the different types of fractions and how to perform operations with them.

\section{Decimals}
Decimals are another way of expressing parts of a whole. We will cover how to convert between fractions and decimals and perform calculations with decimals.

\section{Percentages}
Percentages are everywhere in daily life—from discounts in stores to statistics. This section explains how percentages work and how to calculate them.
""",
    "algebra.tex": r"""
\chapter{Algebra: Solving for the Unknown}
\section{Introduction to Algebra}
Algebra is the branch of math that deals with finding unknown values. We will explore basic algebraic equations and how to solve for variables.

\section{Linear Equations}
Linear equations involve variables raised to the first power. This section will explain how to solve and graph linear equations.

\section{Quadratic Equations}
Quadratic equations are more complex, involving variables squared. We will cover different methods of solving them, including factoring and using the quadratic formula.
""",
    "geometry.tex": r"""
\chapter{Geometry: Shapes and Spaces}
\section{Basic Shapes}
In this section, we will review the properties of basic geometric shapes like squares, triangles, and circles.

\section{Perimeter, Area, and Volume}
Learn how to calculate the perimeter, area, and volume of different shapes, and why these measurements matter in real-world applications.

\section{Advanced Geometry: Circles and Polygons}
Advanced geometry delves into the properties of circles, polygons, and how these shapes interact in space.
""",
    "calculus.tex": r"""
\chapter{Calculus: Understanding Change}
\section{Derivatives}
Calculus helps us understand how things change. We will introduce derivatives, the concept of rates of change, and how they are used in everyday life.

\section{Integrals}
Integrals are about accumulation—finding the total amount of something over time. We will explore the basics of integrals and their applications.
""",
    "conclusion.tex": r"""
\chapter{Conclusion: A Journey Through Mathematics}
In this final chapter, we’ll review how we’ve progressed from simple addition and subtraction to advanced calculus and abstract concepts. You’ll see how mastering each step builds your understanding and appreciation for the beauty and power of math.
"""
}

# Create the chapters directory if it doesn't exist
os.makedirs("chapters", exist_ok=True)

# Create each chapter file and write the content
for filename, content in chapters.items():
    with open(os.path.join("chapters", filename), "w") as file:
        file.write(content.strip())

print("Chapter files created successfully.")