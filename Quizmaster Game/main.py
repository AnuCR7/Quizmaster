import pgzrun
WIDTH=870
HEIGHT=670
TITLE='Quizmaster Game'

qfile='questions.txt'
questions=[]
question_count=0
question_index=0
time_left=10

mbox=Rect(0,0,880,80)
mbox.move_ip(0,0)

qbox=Rect(0,0,650,150)
qbox.move_ip(20,100)

tbox=Rect(0,0,150,150)
tbox.move_ip(700,100)

tibox=Rect(0,0,150,350)
tibox.move_ip(700,300)

abox1=Rect(0,0,300,150)
abox1.move_ip(20,300)

abox2=Rect(0,0,300,150)
abox2.move_ip(20,500)

abox3=Rect(0,0,300,150)
abox3.move_ip(370,300)

abox4=Rect(0,0,300,150)
abox4.move_ip(370,500)

answerbox=[abox1,abox2,abox3,abox4]

def draw ():
    global time_left
    screen.clear()
    screen.fill('blue')
    screen.draw.filled_rect(mbox,'blue')
    screen.draw.filled_rect(qbox,'orange')
    screen.draw.filled_rect(tibox,'dark green')
    screen.draw.filled_rect(tbox,'green')
    for i in answerbox:
        screen.draw.filled_rect(i,'yellow')
    m_message='Welcome to Quizmaster!'
    screen.draw.textbox(m_message,mbox,color='white')
    screen.draw.textbox('Skip',tibox,color='white',angle=-90)
    screen.draw.textbox(str(time_left),tbox,color='white',shadow=(0.5,0.5),scolor='black')
    screen.draw.textbox(qreturn[0],qbox,color='white')
    index=1
    for i in answerbox:
        screen.draw.textbox(qreturn[index],i,color='white')
        index=index+1
    
def move_message():
    mbox.x=mbox.x-2
    if mbox.right < 0:
        mbox.left=WIDTH

def read_questions():
    global question_count, question_index ,questions
    q=open(qfile,'r')
    for qu in q:
        questions.append(qu)
        question_count=question_count+1
    q.close()

def read_next_question():
    global question_index
    question_index=question_index+1
    return questions.pop(0).split(',')


def update():
    move_message()
read_questions()
qreturn=read_next_question()
pgzrun.go()