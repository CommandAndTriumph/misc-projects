struct ArrayList {
    capacity: usize,
    length: usize,
    data: Box<i32>,
}


impl ArrayList {
    fn new(capacity: usize) -> ArrayList {
        ArrayList { capacity: capacity, length: 0, data: [0, capacity] }
    }

    fn insert(&self, index: usize, int: i32) {
        if index > self.length {
            println!("Index out of bounds.");
        }
        let temp = self.data[index];
        self.data[index] = int;
        if index < self.lens() - 1 {
            self.insert(index + 1, temp);
        } else {
            self.length += 1;
        }
    }


    fn lens(&self) -> usize {
        return self.length;
    }
}


fn main() {
    let a = ArrayList::new(10);
    println!("{}", a);
}