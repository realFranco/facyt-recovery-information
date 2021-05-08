# FaCyT - Information Recovery

![python3](https://img.shields.io/badge/python-3.8.x-blue.svg?style=for-the-badge&logo=appveyor )

Set of homeworks related wit the Courserwork (Academic Elective) - **Information Recovery**. 

The details about the activity are inside the next reference.

[ESP] Reference: [Manuel Montes-y-Gómez Ph.D Main/Recuperacion De Informacion](https://ccc.inaoep.mx/~mmontesg/pmwiki.php/Main/RecuperacionDeInformacion)

## Installation steps
```shell
// Tested on Ubuntu 20.04

// Create the virtual env.
python3 -m venv env

// Activate the virtual env. [Linux]
source env/bin/activate

// Activate the virtual env. [Windows] (Not tested yet).
env\Scripts\activate.bat

// Install dependencies
pip3 install -r requirements.txt

Probabbly you will seme "building error" but even with that error the depedency is installed.

// Turn off the virtual env.
deactivate
```

## Running steps
```shell
// Run the Homework number 1 & number 2!

python3 main.py > test/homework.out // Time elapsed on intel i3-3rd gen [~60, ~75] seconds.


/*
This will generate the next set of files:
tf = Term Frecuency

    out/tf-text.out
    out/tf-query.out
*/
```

**Note**: This time "could be improved" after implement the homework using Threads. That is a TODO not a MUST.

## Example of the output:

The test/homework.out will contain this format.


```shell
Homework #1 - Start

Length of documents to process: 423
...

Reduction text           #1: 0.24262524000698205
Reduction text (Porter)  #1: 0.013964042590329906
Length of the vocabulary #1: 419

...

Reduction query          #83: 0.10828025477707004
Reduction query (Porter) #83: 0.01273885350318471
Length of the vocabulary #83: 21

Homework #1 - End. Time elapsed: 72 second(s)


Homework #2 - Start

...

Homework #2 - End. Time elapsed: N second(s)
```

The tf-[query | text] will follow the requiremen from the homework, so is not need it explanation for it.

## Data structures defined

Text:
```json
{
    text: int,
    page: int,
    date: str,
    body: str,
    cleanBody: str,
    cleanBodyPorter: str
    termFrecuency: dict
}
```

Query:
```json
{
    query: int,
    body: str,
    cleanBody: str,
    cleanBodyPorter: str
    termFrecuency: dict
}
```
