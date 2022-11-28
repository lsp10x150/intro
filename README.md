# Introduction to python and databases for data-science

# Dataset

[https://github.com/jOOQ/sakila](https://github.com/jOOQ/sakila)

# Curriculum

1. System Programming Basics
    1. Working with files
        1. Open
        2. Modify
        3. Close
        4. Search in text files
            
            Homework: *simple grep analogue, which prints every line of text which contains an argument substring*
            
    2. Regexes
        1. What is a regex
        2. Basic syntax (www.regex101.com) [https://habr.com/ru/post/545150/](https://habr.com/ru/post/545150/)
            1. Escape symbols (.+?\d\D\s\S\t\T\b…)
            2. Square brackets [abcd] [1..9]
            3. Figure brackets {1}
            4. Capture groups () and their replacements
        3. Python regex library
        
        Homework: *regex grep evolution*
        
    3. *Regex practice a special file — real-life example in my logs — &*
	   *Additional knowledge: grep, awk & sed*
        
        Homework: *grep a log and count few metrics*
        
    4. OOP Basics
        1. What is an object and why is it convenient to use objects in code?
        2. What is a class? 
        3. How to write classes? 
        4. Encapsulation (underscore — makes a field private) Why is it convenient?
        5. Inheritance and why is it convenient? 
        6. Polymorphism and why is it convenient? 
    5. OOP practice 
        1. Writing a console lungton’s ant
2. Databases
    1. RDBMS and NoSQL DBs overview
        1. SQL
            1. Postgres
            2. MySQL, MariaDB
            3. Sqlite
        2. NoSQL
            1. Document based
                1. MongoDB
            2. Key-Value pairs
                1. Kassandra 
        
        Homework: *Deploy a Postgres, sqlite and MongoDB (read json documentation)*
        
    2. Working with databases from cli-tools and python scripts
        1. SQL overview DDL and DML,
        2. cli tools for postgres, sqlite, mongodb
        3. python libraries for postgres, sqlite, mongodb
        
        Homework: *Create and fill databases with sakilla dataset*
        
    3. Practice on sql. How to fetch sensible data?
        
        Homework: *Fetch interesting data from sakilla*
        
    4. Relational databases theory 
        1. Normalization
        2. ORMs
        
        Practice: *Create and normalize a database for a zoo-store, create a simple cli-tool to fill a database*
        
3. Data-science block 
    1. NumPy
    2. Pandas
    3. Keras
