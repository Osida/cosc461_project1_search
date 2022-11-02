<div align="center">
  <img width="400" alt="Work in progress" src="https://user-images.githubusercontent.com/51928654/194620578-542e19ba-15d5-405a-8e7d-b689358a70ff.png"/>
</div>

<h1 align="center" display="flex" justify-content="" align-items="center">
  Project 1: Search
</h1>

- [Tech](#tech)
- [Instructions](#instructions)
- [Questions](#questions)
  * [Autograder](#autograder)
  * [Question 1](#question-1)
  * [Question 2](#question-2)
  * [Question 3](#question-3)
  * [Question 4](#question-4)
- [Team Members](#team-members)

## Tech
- **Language**: [Python 2.7.18](https://www.python.org/downloads/release/python-2718/)
- **IDE**: [PyCharm](https://www.jetbrains.com/pycharm/)

## Instructions
[Project 1: Search](http://ai.berkeley.edu/search.html)

Complete questions 1, 2, 3 and 4 of the Pacman project which is described in the following page and submit search.py.
You only need to change search.py and this is the only file you should be submitting.

Each question has 25 points.

Please include the names of the group members in a code comment at the top of search.py.
One group member should submit search.py and the other should submit only a text submission with the name of their group member.


## Questions

### Autograder
```
python autograder.py
```
<img width="501" alt="image" src="https://user-images.githubusercontent.com/51928654/199377466-cb347ca8-f7b3-4f0d-84b6-f3eac3d9fc39.png">


### Question 1
<img width="500" alt="Q1" src="https://user-images.githubusercontent.com/51928654/194623423-b17ef90e-043a-44f9-acd1-fa1f912b3836.png"/>

```
python pacman.py -l tinyMaze -p SearchAgent
```
<img width="520" alt="image" src="https://user-images.githubusercontent.com/51928654/199374025-6406660c-4cff-4683-93ef-18f4216e98fa.png">

```
python pacman.py -l mediumMaze -p SearchAgent
```
<img width="521" alt="image" src="https://user-images.githubusercontent.com/51928654/199374130-64c613a9-e818-49e2-ad2b-098899f088ba.png">

```
python pacman.py -l bigMaze -z .5 -p SearchAgent
```
<img width="522" alt="image" src="https://user-images.githubusercontent.com/51928654/199374202-d143c722-e5a5-407c-a5e9-83c090f3a68d.png">


### Question 2
<img width="500" alt="Q2" src="https://user-images.githubusercontent.com/51928654/194623674-a7c643f4-d1be-4d02-9086-ff8b00ad7516.png">

```
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```
<img width="472" alt="image" src="https://user-images.githubusercontent.com/51928654/199375526-84e67c0a-f9c4-4884-8564-ba5f70e283d9.png">

```
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```
<img width="470" alt="image" src="https://user-images.githubusercontent.com/51928654/199375650-fe4f1297-eeba-4229-a92c-462f0dea953d.png">

```
python eightpuzzle.py
```
<img width="767" alt="image" src="https://user-images.githubusercontent.com/51928654/199375829-3a754735-4e50-479e-904a-bf0bb5178ea6.png">


### Question 3
<img width="500" alt="Q3" src="https://user-images.githubusercontent.com/51928654/194623761-45b9eb50-2676-4d9c-a4ce-84d38961353b.png">

```
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
```
<img width="464" alt="image" src="https://user-images.githubusercontent.com/51928654/199376113-4e1a80b5-7278-4a85-8b65-a8f9818ae0f4.png">

```
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
```
<img width="467" alt="image" src="https://user-images.githubusercontent.com/51928654/199376205-444804f3-b398-4f42-a4bd-03427cf145d8.png">

```
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```
<img width="467" alt="image" src="https://user-images.githubusercontent.com/51928654/199376249-a6a26080-dde1-4aaa-bcbe-101023072600.png">


### Question 4
<img width="500" alt="Q4" src="https://user-images.githubusercontent.com/51928654/194623880-cd42562a-3110-4e7b-b3f4-1ebe58949c45.png">

```
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
<img width="624" alt="image" src="https://user-images.githubusercontent.com/51928654/199376702-9145fd0b-0357-4402-bcc5-67ccbedb391f.png">



## Team Members
- [@Osida](https://github.com/Osida)
- [@Everett](https://github.com/Osida/cosc461_project1_search)
