use std::env;
use std::io;
use std::io::prelude::*;
use std::io::BufReader;
use std::fs::File;
fn tail(mut buffer_text: BufReader<File>) -> () {
    let mut buffer = String::new();
    let string = buffer_text.read_to_string(&mut buffer);
    let mut reversed = buffer.chars().rev();
    //TODO: Fix the program skipping the first line of text.
    let mut scanner = reversed.scan::<_, String, _>(String::new(), |state, c| {
        match c {
            '\n' => {
                let full_line = state.clone();
                state.clear();
                return Some(full_line);
            },
            _ => state.push(c),
        }
        Some(String::from(""))
    });
    let mut line_vec: Vec<String> = scanner.filter(|x| x != "").take(10).map(|x| x.chars().rev().collect()).collect();
    for i in line_vec.iter().rev() {
        println!("{}", i);
    }
}




fn main() {
    let file_name = env::args().nth(1).unwrap();
    let fh = match File::open(&file_name) {
        Err(_) => panic!("File name is incorrect."),
        Ok(t) => t,
    };
    let reader = BufReader::new(fh);
    tail(reader);
}