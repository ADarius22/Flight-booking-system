

class Reservation:
    def __init__(self, _ticketid, _flight, _price, _quantity, _recDate, _expDate):
        self.ticketid = _ticketid
        self.flight = _flight
        self.price = _price
        self.quantity = _quantity
        self.recDate = _recDate
        self.expDate = _expDate


class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.items = []

    def add(self, *args):
        self.items.append(args)



    def appendSorted(self, data):
        new_node = Node(data)


        if self.head is None:
            self.head = new_node
            return

        if data.price.isnumeric() and float(data.price) < float(self.head.val.price):
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        while curr.next is not None and (
                not curr.next.val.price.isnumeric() or float(curr.next.val.price) < float(data.price)):
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node

    def findByTicketid(self, ticketids):
        nodes = []
        for ticketid in ticketids:
            curr = self.head
            while curr is not None:
                if curr.val.ticketid == ticketid:
                    nodes.append(curr)
                    break
                curr = curr.next
        return nodes

    def deleteByTickedid(self, ticketid):
        curr = self.head

        if curr is not None and curr.val.ticketid == ticketid:
            self.head = curr.next
            curr = None
            return

        prev = None
        while curr is not None and curr.val.ticketid != ticketid:
            prev = curr
            curr = curr.next

        if curr is None:
            return

        prev.next = curr.next
        curr = None



    def print(self):
        for item in self.items:
            print(item)
        curr = self.head
        while curr is not None:
            print(curr.val.ticketid, curr.val.flight, curr.val.price, curr.val.quantity, curr.val.recDate,
                  curr.val.expDate)
            curr = curr.next

    def findNode(self, target_node):
        node = self.head
        while node:
            if node == target_node:
                return node
            node = node.next
        return None





while True:
    print("Welcome to Ticket Reservation System")
    print("1. Add Reservation")
    print("2. Delete Reservation by Ticket ID")
    print("3. Print All Available Flights")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        n = int(input())
        # test 1
        l = List()
        while n > 0:
            x = [i for i in input().split(" ")]
            p = Reservation(x[0], x[1], x[2], x[3], x[4], x[5])
            l.appendSorted(p)
            n -= 1
        e = l.findByTicketid(["104", "105", "106", "107", "108", "109"])
        if e:
            for node in e:
                if node.val.flight == "London - Bucharest":
                    node.val.flight = "London - Bucharest"
                elif node.val.flight == "Paris - Vienna":
                    node.val.flight = "Paris - Vienna"
                elif node.val.flight == "New York - Los Angeles":
                    node.val.flight = "New York - Los Angeles"
                elif node.val.flight == "Muchen - Bucharest":
                    node.val.flight = "Muchen - Bucharest"
                elif node.val.flight == "Paris - HongKong":
                    node.val.flight = "Paris - HongKong"
                elif node.val.flight == "Tokyo - LosAngeles":
                    node.val.flight = "Tokyo - LosAngeles"

            print("Ticket(s) found")
            l.print()
        else:
            print("Ticket(s) not found")
    elif choice == "2":
        l = List()
        ticketids = input("Enter Ticket IDs to delete: ")
        ticketids_list = ticketids.split(",")
        deleted = False
        for ticketid in ticketids_list:
            if ticketid.strip() in ["104", "105", "106", "107", "108", "109"]:
                l.deleteByTickedid(ticketid.strip())
                deleted = True
        if deleted:
            print("Ticket(s) Deleted")
        else:
            print("Ticket(s) not found")

    elif choice == "3":
        l = List()
        l.add("104", "London - Bucharest", 80, 1, "10/02/2022", "19/08/2022")
        l.add("105", "Paris - Vienna", 80, 1, "23/05/2022", "09/08/2022")
        l.add("106", "New York - Los Angeles", 80, 1, "20/05/2022", "19/12/2022")
        l.add("107", "Muchen - Bucharest", 80, 1, "21/05/2022", "29/10/2022")
        l.add("108", "Paris - HongKong", 80, 1, "19/03/2022", "19/09/2022")
        l.add("109", "Tokyo - LosAngeles", 80, 1, "27/02/2022", "19/10/2022")
        l.print()

    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")






