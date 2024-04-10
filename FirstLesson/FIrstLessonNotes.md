# Lesson Notes

## first lesson 3.4

## Author's Note

This document was written by Yaniv Gabay. While every effort has been made to ensure the accuracy and completeness of this material, it is possible that it may contain errors or omissions. Readers are advised to use this material as a general guide and to verify information with appropriate professional sources.
in order to see the pictures taken from the presentation, please make sure you cloned the pictures themselves.

## SQL

- Declarative languange, was created at IBM at 1974
- CRUD - Create , Read, Update , Delete, 4 basic actions
we will focus on the READ almost soley, Read action has the most
logic on it (in actions we as programmers can do)
-Types of databases, there are plenty, many many types.
we will be able to work with all DB that support SQL
we need to notice, there is a small difference in syntax between those databases types.
- basic explanation about relations in databases, which are basiccly tables and how they are connected to each others
## SQL Cheat Sheet

- Reccomended to work with a sql Cheat sheet, will smooth thing.
- there are two links in the presentation

## SQLITE

- Very light,most used database engine in the world.
- very easy to learn with
- we will work with it.
- we will work with DB browser for SQLite
- we will play with the DB browser for sqlite, and we will actually
- write python code, with the quries as a string

## Page 7 of the Presentation
- We can use Pandas DF to connect to the sqlite
- We better install SQL alchemy

## Tables
- each table has row/tuple/record/observation
- of course we have cols/attributes (defines the values in the rows)
- each row is from cells\fields
- General notes: 
- We cannot know how the values are ordered (if you didnt sort it etc). that system will order it on its default values
- Results of a query is a table aswell. (empty table aswell)
- returning a bad amount of rows, is a mistake, (not more or less)
- returning more cols than needed, isnt a mistake, it is just a bad or different view from intended

## Data Types
- Null
- Integer
- Real (float)
- Text
- Blob - binary generic (use for images etc)

## Misc
- dont have bool, just 0 and 1 SQLITE does hae TRUE and FALSE
- if we want a col name with space etc, we will need "" etc.
- we dont allow spaces, so we will do family_name
- and if we want to reach for specific value, we will search with ''

## Conventions
- Languange keyword ALL UPPERCASE SELECT FROM JOIN etc...
- Table name prefer one word lowercase
- Col name lowcase with _ 

## SQL parts
- We will work with DQL - data query Languange, so we will work with
- selects