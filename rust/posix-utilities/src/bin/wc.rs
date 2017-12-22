use std::env;
//use std::io;
use std::io::prelude::*;
use std::io::BufReader;
use std::fs::File;

fn wc(file_path: String) -> u32 {
    let fh = match File::open(&file_path) {
        Err(_) => panic!("File name or path is incorrect."),
        Ok(t) => t,
    };
    let mut text = BufReader::new(fh);
    let mut string = String::new();
    let _ = text.read_to_string(&mut string);
    let mut temp_str = String::new();
    let mut count: u32 = 0;
    for i in string.chars() {
        if !i.is_whitespace() {
            temp_str.push(i);
//            println!("{}", temp_str);
            if temp_str.len() == 1 {
                count += 1;
            }
        } else {
            temp_str.clear();
        }
    }

//    for i in string.chars() {
//        if i == ' ' {
//            if temp_str.len() > 0 {
//                temp_str.clear();
//                count += 1;
//            } else {
//                continue
//            }
//        } else{
//            temp_str.push(i)
//        }
//    }

    return count;
}

fn main() {
    let file_path = env::args().nth(1).unwrap();
    println!("Word Count: {}", wc(file_path));
}