#[cfg(test)]
mod tests {
    use super::*;

    //core_tests() verifies the correct function and edge case handling for new(), append(), len(), get(), and remove().
    #[test]
    fn test_new() {
        let list = LinkedList::new();
        assert_eq!(0, list.len());
    }

    fn test_append() {
        let mut list = LinkedList::new();
        list.append(15);
        assert_eq!(1, list.len());
        list.append(20);
        assert_eq!(2, list.len());
        list.append(27);
        assert_eq!(3, list.len());
        assert_eq!(15, list.get(0));
        assert_eq!(20, list.get(1));
        assert_eq!(27, list.get(2));
    }

    //Seems redundant, cases are covered in test_new()
    fn test_len() {
        let mut list = LinkedList::new();
        assert_eq!(0, list.len());
        for i in 0..100 {
            list.append(i);
        }
        assert_eq!(100, list.len());
    }

    fn test_get() {
        let mut list = LinkedList::new();
        for i in 0..100 {
            list.append(i);
        }
        assert_eq!(99, list.get(99));
        assert_eq!(0, list.get(0));
        assert_eq!(50, list.get(50));
        #[should_panic]
        list.get(100);
        #[should_panic]
        list.get(-1);
    }

    fn test_remove() {
        let mut list = LinkedList::new();
        #[should_panic]
        list.remove(0);
        list.append(1);
        assert_eq!(1, list.len());
        list.remove(0);
        assert_eq!(0, list.len());
        for i in 0..100 {
            list.append(i);
        }
        assert_eq!(100, list.len());
        for i in 0..100 {
            list.remove(0);
        }
        assert_eq!(0, list.len());
    }

    fn test_insert() {
        let mut list = LinkedList::new();
        assert_eq!(0, list.len());
        list.insert(0, 0);
        assert_eq!(1, list.len());
        #[should_panic]
        list.insert(2, 0);
        for i in 1..50 {
            list.insert(i, i);
        }
        assert_eq!(50, list.len());
        for i in 0..50 {
            assert_eq!(i, list.get(i));
        }
        list.insert(40, 112);
        assert_eq!(51, list.len());
        assert_eq!(39, list.get(39));
        assert_eq!(112, list.get(40));
        for i in 41..51 {
            assert_eq!(i - 1, list.get(i));
        }

    }

    fn test_prepend() {
        let mut list = LinkedList::new();
        for i in 0..50 {
            list.prepend(i);
        }
        assert_eq!(49, list.get(0));
        assert_eq!(25, list.get(25));
        assert_eq!(0, list.get(49));
    }

    fn test_pop() {
        let mut list = LinkedList::new();
        #[should_panic]
        list.pop();
        for i in 0..50 {
            list.append(i);
        }
        list.pop();
        assert_eq!(48, list.get(48));
        assert_eq!(49, list.len());
        for i in 0..49 {
            list.pop();
        }
        assert_eq!(0, list.len());
    }

    fn basic_tests() {
        let mut list1 = LinkedList::new();
        assert_eq!(0, list1.len());
        list1.append(1);
        assert_eq!(1, list1.len());
        for i in 0..49 {
            list1.append(i);
        }
        assert_eq!(50, list1.len());
    }

    fn core_tests() {
        //Create empty list, length should be 0.
        let mut my_list = LinkedList::new();
        assert_eq!(0, l.len());
        //Append a node to the list, length should now be 1.
        my_list.append(12);
        assert_eq!(1, my_list.len());
        //Append a second node to list, len() should now return 2.
        my_list.append(15);
        assert_eq!(2, my_list.len());
        //Test of get(), should return i32 at index.
        assert_eq!(15, my_list.get(1));
        //Test of get() at an invalid index.
        #[should_panic]
            assert_eq!(1, my_list.get(2));
        my_list.remove(0);
        my_list.remove(0);
        //Test for append, to verify that when nodes are added, they are added to the end of the list.
        for i in 0..50 {
            my_list.append(i);
        }
        for i in 0..my_list.len() {
            assert_eq!(i, my_list.get(i));
        }
        //Test remove() on OoB index.
        #[should_panic]
            my_list.remove(50);
        //Remove nodes at index 0, each time a node is removed, the head should become the new first node.
        for i in 0..50 {
            my_list.remove(0);
        }
        assert_eq!(0, my_list.len());
    }

    //extended_tests() verifies the correct function and edge case handling for insert(), prepend() and pop().
    fn extended_tests() {
        let mut ext_list = LinkedList::new();
        //Test for insert at index 0.
        for i in 0..50 {
            ext_list.insert(0, i);
        }
        assert_eq!(50, ext_list.len());
        //In place insert (for a list with len > 2 at index > 0), the new node should clone the pointer for the node at its current index.
        // The new node should point to what the current node points at, and the current node should point at the new node.
        ext_list.insert(45, 112);
        assert_eq!(112, ext_list.get(45));
        assert_eq!(44, ext_list.get(44));
        assert_eq!(45, ext_list.get(46));
        assert_eq!(51, ext_list.len());
        assert_eq!(49, ext_list(50));
        for i in 0..51 {
            ext_list.remove(0);
        }
        assert_eq!(0, ext_list.len());
        //OoB index test for insert.
        #[should_panic]
        ext_list.insert(1, 2);
        //Tests for prepend, should create a new node which points to the head node, thus making the new node the head node.
        ext_list.prepend(0);
        assert_eq!(1, ext_list.len());
        ext_list.remove(0);
        for i in 0..50 {
            ext_list.prepend(i);
        }
        assert_eq!(50, ext_list.len());
        assert_eq!(49, ext_list.get(0));
        assert_eq!(0, ext_list.get(49));
        assert_eq!(25, ext_list.get(25));
        //Tests for pop(), should remove the last node in the list when called.
        ext_list.pop();
        #[should_panic]
        ext_list.get(49);
        for i in 0..49 {
            ext_list.pop();
        }
        assert_eq!(0, ext_list.len());
        #[should_panic]
        ext_list.pop();

    }
}

struct LinkedList {
    head: Option<Node>,
}

struct Node {
    val: i32,
    next: Option<Box<Node>>,
}

impl LinkedList {

    fn new() -> LinkedList { return LinkedList{ head: None};}

    fn len(&self) -> usize {
        let mut count: usize = 0;
        match self.head {
            None => count,
            _ => {
                let mut maybe_node = &self.head.as_ref().unwrap().next;
                while maybe_node.is_some() {
                    maybe_node = &maybe_node.as_ref().unwrap().next;
                    count += 1;
                }
            count
            }
        }
    }


    fn append(&mut self, int: i32) -> () {
        match self.head {
            None => self.head = Some(Node { val: int, next: None }),
            Some(ref n) => {
                let mut has_next = &self.head.as_ref().unwrap().next;
                while has_next.is_some() {
                    has_next = &has_next.as_ref().unwrap().next;
                }
                    has_next = Some(Node {val: int, next: None});
            }
        }
    }


    fn get(&self, index: usize) -> i32 {
        unimplemented!();
    }

    fn remove(&mut self, index: usize) -> () {}

    fn insert(&mut self, index: usize, int: i32) -> () {}

    fn prepend(&mut self, int: i32) -> () {}

    fn pop(&mut self) -> () {}

}



/*
impl LinkedList {
    fn new() -> LinkedList {
        return LinkedList{head: None};
    }
    fn len(&self) -> usize {
        match self.head {
            None => 0,
            _ => {
                //let mut maybe_node = self.head.as_ref().unwrap().next;
                let mut maybe_node = &self.head.as_ref().unwrap().next;
                let mut jmp_count = 1;
                while maybe_node.is_some() {
                    //maybe_node = maybe_node.as_ref().unwrap().next;
                    maybe_node = &maybe_node.as_ref().unwrap().next;
                    jmp_count += 1;
                }
                jmp_count
            }
        }
    
    }
    
    fn append(&mut self, int: i32) -> () {
        match self.head {
            None => self.head = Some(Node{ val: int, next: None }),
            Some(ref n) => {
                let mut has_next = &self.head.as_ref().unwrap().next;
                while has_next.is_some() { 
                    has_next = &has_next.as_ref().unwrap().next;
                }
                has_next.next = Some(Node { val: int, next: None });
                has_ne
            }
        }
    }
}




fn main() {

}
*/