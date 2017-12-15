#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
        let mut a = ArrayList::new(10);
        for i in 0..10 {
            a.insert(i, i as i32);
        }
        println!("{:?}", a);
    }
}
#[derive(Debug)]
struct ArrayList {
    capacity: usize,
    length: usize,
    data: Box<[i32]>,
}

impl ArrayList {
    fn new(capacity: usize) -> ArrayList {
        ArrayList { capacity: capacity, length: 0, data: Box::new([0; 10]) }
    }

    fn insert(&mut self, index: usize, int: i32) {
        if index > self.length {
            panic!("Index out of bounds.");
        }
        let temp = self.data[index];
        self.data[index] = int;
        if index + 1 < self.length {
            self.insert(index + 1, temp);
        } else {
            self.length += 1;
        }
    }

    fn len(&self) -> usize {
        return self.length;
    }
}

