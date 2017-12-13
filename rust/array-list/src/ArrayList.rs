struct ArrayList {
    capacity: usize,
    length: usize,
    data: Box<i32>,
}


impl ArrayList {
    fn new(capacity: usize) -> ArrayList {
        ArrayList {capacity: capacity, length: 0, data: [i32, capacity]}
    }

    fn insert(&self, index: usize, int: i32) {
        if index > self.length {
            println!("Index out of bounds.");
        }
        let temp = self.data[index];
        self.data[index] = int;
        if index < self.lens() - 1 {
            self.insert( index + 1, temp);
        }
    }

//    fn lens(&self) -> usize {
//        let mut i: usize = 0;
//        while i < self.capacity {
//            match &self.data[i] {
//                i32 => i += 1,
//                _ => break,
//            }
//        }
//        return i;
//    }
}



fn main() {
    let a = ArrayList::new(10);
    println!("{:?}", a);
}