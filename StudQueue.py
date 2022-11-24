import codecs
import string

# global
list_stud = [[] * 17] * 20
queue = []
q_id = 0


def load_students():
    with codecs.open("students.txt", 'r', encoding="utf-8") as fin:
        id = 1
        n = int(fin.readline())
        while id < n + 1:
            list_stud[id] = (fin.readline().strip().split(")"))
            if not list_stud[id][0]:
                break
            id += 1
    fin.close()
    return n


def from_file_queue():
    with open("queue.txt", 'r') as fin:
        pass


def add_person_in_queue(q_id):
    person = input("input person's id or name")
    # person = 2
    try:
        queue.append(str(q_id) + "| " + str(list_stud[int(person)][1]))
    except (Exception) as err:
        for i in range(1, stud_val + 1):
            if str(list_stud[i][1]).find(str(person)) == 0:
                # print(list_stud[i][1])
                queue.append(str(q_id) + "| " + str(list_stud[i][1]))


def remove_first(id):
    i = 0
    while i < id - 1:
        queue[i] = queue[i + 1]
        i += 1
    queue.remove(queue[id - 1])
    display_queue(id - 1)


def remove_person(who, id):
    while who < id - 1:
        queue[who] = queue[who + 1]
        who += 1
    queue.remove(queue[id - 1])
    display_queue(id - 1)


def exchange(a, b):
    aa = str(queue[a])
    bb = str(queue[b])
    l1 = list(aa)
    l2 = list(bb)
    p = l1[0]
    l1[0] = l2[0]
    l2[0] = p
    queue[a] = ''.join(l2)
    queue[b] = ''.join(l1)


def menu():
    print("choose option")
    print("1| add student into queue")
    print("2| NEEEEEEXT!!!")
    print("3| change student1 and student2 in queue(a-la ya ustupayu)")
    print("4| display current queue")
    print("5| i dont want to participate anymore! (remove from queue by id of queue)")
    print("r| i'm dumbass, destroyed queue, want to restore")


def display_queue(q_id):
    print()
    for i in range(q_id):
        if i == 0:
            print(queue[i] + " currently in service ")
        else:
            print(queue[i])
    print()


def restore():
    with codecs.open("queue.txt", 'r', encoding="utf-8") as fin:
        id = 0
        while 1:
            queue.append(fin.readline().strip())
            if not queue[id]:
                break
            id += 1

    fin.close()
    return id


# ---------------------------------------------------------------
stud_val = load_students()
# print(list_stud)
option = -1
menu()



while option != 0:
    if option == 6:
        q_id=restore()
    try:
        if option == 1:
            add_person_in_queue(q_id)
            q_id += 1
        elif option == 2:
            remove_first(q_id)
            q_id -= 1
        elif option == 3:
            a = int(input("id q 1 >> "))
            b = int(input("id q 2 >> "))
            exchange(a, b)
            print("successfully changed student " + queue[a] + " and " + queue[b])

        elif option == 4:
            display_queue(q_id)
        elif option == 5:
            remove_person(int(input("id participator >> ")), q_id)

        if option!=-1:
          with codecs.open("queue.txt", 'w', encoding="utf-8") as q:
            for i in range(q_id):
              q.writelines(queue[i] + '\n')
          q.close()
    except Exception as e:
        print(e)
        print("Oh, shit, i'm sorry")

    option = int(input("option index >> "))


print("Exiting...")
exit()
