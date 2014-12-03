#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """

    # sakht list khottot
    listline =[]
    for line in filename:
        listline.append(line)
    print(listline)

    # sakht list khotoot namha
    list=[]
    year=''
    for line in listline:
        if line[0]=='<' and line[1]=='t' and line[2]=='r':
            list.append(line)
        elif line[0]=='<' and line[1]=='h' and line[2]=='3':
            year=line
    print(list)

    # sal
    y=''
    for i in year:
        if i=='/':
            year=y[-5:]
            year=year[:4]
        else:
            y+=i
    print(year)


    # sakht dict namha
    dict={}
    for line in list:
        adad=''
        boy=''
        girl=''
        ezaf=''
        j=0
        for i in line:
            if ezaf[-2:]=='d>':
                if i=='<' or i=='\n':
                    ezaf+=i
                    if j==0:
                        j=1
                    elif j==1:
                        j=2
                    else:
                        j=0
                else:
                    if j==0:
                        adad+=i
                    elif j==1:
                        girl+=i
                    else:
                        boy+=i
            else:
                ezaf+=i
        if adad!='' and boy!='' and girl!='':
            print('%-5s%-15s%s'%(adad,boy,girl))
            dict[boy]=adad
            dict[girl]=adad

    # chap dict namha ba rotbe
    print(dict.items())

    # list morattabe namha
    list1=[]
    list1=sorted(dict.keys())
    print(list1)

    # list morattabe namha ba rotbe
    flist=[]
    for i in list1:
        flist.append('%s %s'%(i,dict[i]))
    flist.insert(0,year)

  # +++your code here+++
    return flist




def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  # args = sys.argv[1:]
  # #
  # if not args:
  #   print ('usage: [--summaryfile] file [file ...]')
  #   sys.exit(1)
  # #
  # # # Notice the summary flag and remove it from args if it is present.
  # summary = False
  # if args[0] == '--summaryfile':
  #   summary = True
  #   del args[0]

  # f1990=open('baby1990.html','rU')
  # f1992=open('baby1992.html','rU')
  f1994=open('baby1994.html','rU')
  # f1996=open('baby1996.html','rU')
  # f1998=open('baby1998.html','rU')
  # f2000=open('baby2000.html','rU')
  # f2002=open('baby2002.html','rU')
  # f2004=open('baby2004.html','rU')
  # f2006=open('baby2006.html','rU')
  # f2008=open('baby2008.html','rU')
  # print(extract_names(f1990))
  # print(extract_names(f1992))
  print(extract_names(f1994))
  # print(extract_names(f1996))
  # print(extract_names(f1998))
  # print(extract_names(f2000))
  # print(extract_names(f2002))
  # print(extract_names(f2004))
  # print(extract_names(f2006))
  # print(extract_names(f2008))


  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
