use std::env;
use std::io;
use std::io::prelude::*;
use std::io::BufReader;
use std::fs::File;
fn tail(mut buffer_text: BufReader<File>) -> () {
    let mut buffer = String::new();
    let string = buffer_text.read_to_string(&mut buffer);
    let mut reversed = buffer.chars().rev();
    let mut line_vec: Vec<usize> = Vec::new();
    for i in 0..10 {
        match reversed.position(|x| x == '\n') {
        None => (),
        Some(position) => line_vec.push(position)
        }
    }
    println!("{:?}", line_vec);
}



fn main() {
    let file_name = env::args().nth(1).unwrap();
    let fh = match File::open(&file_name){
        Err(_) => panic!("File name is incorrect."),
        Ok(t) => t,
    };
    let reader = BufReader::new(fh);
    let mut count = 0;
    tail(reader);
//    for i in reader.lines() {
//        if count < 10 {
//            if let Ok(line) = i {
//                println!("{}", line);
//                count += 1;
//            } else {
//                panic!("A line has failed to read.  File: {}, Error: {}", file_name, i.unwrap_err())
//            }
//        }
//    }
}