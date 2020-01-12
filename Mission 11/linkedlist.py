class LinkedList:

    def __init__(self, lst=[]):
        self.__length = 0
        self.__head = None
        for cargo in reversed(lst):
            self.add(cargo)

    # def __init__(self):
    #     """
    #     Initialises a new linked list object.
    #     @post: A new empty linked list object has been initialised.
    #     """
    #     self.__length = 0
    #     self.__head = None

    def size(self):
        """
        Returns the number of nodes contained in this linked list.
        @post: Returns the number of nodes (possibly zero) contained in this linked list.
        """
        return self.__length

    def first(self):
        return self.__head

    def add(self, cargo):
        """
        Adds a new Node with given cargo to the front of this linked list.
        @pre: self is a (possibly empty) LinkedList
        @post: A new Node object is created with the given cargo.
               This new Node is added to the front of the linked list.
               The length counter has been incremented.
               The head of the list now points to this new node.
        """
        node = self.Node(cargo, self.__head)
        self.__head = node
        self.__length += 1

    def get_reverse(self):
        current = self.__head
        msg = []
        while current != None:
            msg.append(current.value())
            current = current.next()
        return "".join(msg)

    def remove(self):
        if self.size() > 0:
            self.__head = self.first().next()
            self.__length -= 1

    def insert(self, s):
        if self.__head == None:
            self.add(s)
            return
        elif s < self.__head.value():
            self.add(s)
            return
        current = self.__head
        while current.next() is not None:
            if current.value() <= s <= current.next().value():
                node = self.Node(s, current.next())
                current.set_next(node)
                self.__length += 1
                return
            current = current.next()
        node = self.Node(s, None)
        current.set_next(node)
        self.__length += 1

    def remove_from_end(self):
        if self.__head is not None:
            current = self.__head
            if current.next() is None:
                self.__head = None
                self.__length -= 1
                return
            while current.next().next() is not None:
                current = current.next()
            current.set_next(None)
            self.__length -= 1

    def print(self):
        """
        Prints the contents of this linked list and its nodes.
        @pre:  self is a (possibly empty) LinkedList
        @post: Has printed a space-separated list of the form "[ a b c ... ]",
        """
        print("[", end=" ")
        if self.__head is not None:
            self.__head.print_list()
        print("]")

    def print_backward(self):
        """
        Prints the contents of this linked list and its nodes, back to front.
        @pre:  self is a (possibly empty) LinkedList
        @post: Has printed a space-separated list of the form "[ ... c b a ]",
        """
        print("[", end=" ")
        if self.__head is not None:
            self.__head.print_backward()
        print("]")

    class Node:

        def __init__(self, cargo=None, next=None):
            """
            Initialises a new Node object.
            @pre:  -
            @post: A new Node object has been initialised.
                A node can contain a cargo and a reference to another node.
                If none of these are given, a node with empty cargo (None) and no reference (None) is created.
            """
            self.__cargo = cargo
            self.__next = next

        def value(self):
            """
            Returns the value of the cargo contained in this node.
            @pre:  -
            @post: Returns the value of the cargo contained in this node, or None if no cargo  was put there.

            """
            return self.__cargo

        def next(self):
            return self.__next

        def set_next(self, node):
            self.__next = node

        def __str__(self):
            """
            Returns a string representation of the cargo of this node.
            @pre:  self is possibly empty Node object.
            @post: returns a print representation of the cargo contained in this Node.
            """
            return str(self.value())

        def print_list(self):
            """
            Prints the cargo of this node and then recursively of each node connected to this one.
            @pre:  self is a node (possibly connected to a next node).
            @post: Has printed a space-separated list of the form "a b c ... ",
                where "a" is the string-representation of this node,
                "b" is the string-representation of my next node, and so on.
                A space is printed after each printed value.
            """
            print(self, end="")   # print my head
            tail = self.__next    # go to my next node
            if tail is not None:  # as long as the end of the list has not been reached
                tail.print_list()  # recursively print remainder of the list

        def print_backward(self):
            """
            Recursively prints the cargo of each node connected to this node (in opposite order),
            and then prints the cargo of this node as last value.
            @pre:  self is a node (possibly connected to a next node).
            @post: Has printed a space-separated list of the form "... c b a",
                where a is my cargo (self), b is the cargo of the next node, and so on.
                The nodes are printed in opposite order: the last nodes' value is printed first.
            """
            tail = self.__next        # go to my next node
            if tail is not None:     # as long as the end of the list has not been reached
                tail.print_backward()  # recursively print remainder of the list backwards
